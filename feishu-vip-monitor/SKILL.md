---
name: feishu-vip-monitor
description: "Use when monitoring Feishu groups for VIP keywords."
version: 2.0.0
author: Hermes
license: MIT
metadata:
  hermes:
    tags: [feishu, lark, wechat, monitoring, forwarding]
    related_skills: [lark-cli-setup, lark-im, hermes-runtime-config]
---

# Feishu Group VIP Monitor & Forwarder

## When to Use

- 用户要求监控某个飞书群，把带关键词的消息（如 `【仅TA的真爱粉可见】`）即时转发到微信
- 排查“监控进程在跑但收不到消息 / 水位不推进”
- 需要让飞书 `user_access_token` 长期不过期
- 调整微信推送的文本排版、分割线、换行

不适用：能自主拉 bot 进群的场景应优先用 WebSocket/Webhook 事件监听，轮询是退化方案。

监听飞书群（外部群 / 个人账号加入的群 / 机器人所在群），按关键词识别 VIP 消息，联动转发随附图片到微信，用 `message_position` 水位杜绝重复消费。同时覆盖 lark-cli 环境陷阱、token 保活、微信气泡排版。

**生产实例**：`/home/ubuntu/wu2198_vip_monitor/`，群 `oc_59301fc3e11c6e131f31ffb8acd4125a`（wu2198五号群），关键词 `【仅TA的真爱粉可见】`，目标 `o9cq803YeAtzv-XTkS_2UNUqS_JM@im.wechat`。

## 文件结构

| 文件 | 职责 |
|---|---|
| `monitor.py` | 主轮询循环：拉消息 → 过滤 → 推送 → 推进水位 |
| `token_keeper.py` | token 保活：无参单次执行，`--loop` 常驻 |
| `start.sh` | 启停：flock 单实例锁 + pgrep 判活 + 清残留 + nohup 拉起 |
| `crontab_check.sh` | cron 每分钟巡检：进程存活 + token 保活补跑 |
| `state.json` | 水位：`last_position` / `last_msg_id` / `last_create_time` / `last_is_vip` / `last_alert_ts` / `last_cache_sweep` / `push_stats` |
| `monitor_heartbeat.json` | 活性：`last_poll_ts` / `last_poll_at` / `pid` / `fail_count` / `pushed` / `push_failed` / `last_position` / `today`（cron 据此识别假死） |
| `token_heartbeat.json` | 保活心跳：`last_keepalive` / `refreshed` / `before` / `after` / `days_left` |
| `cache/<msg_id>.png` | 配图缓存（已存在且非空则直接复用） |
| `monitor.log` / `token_keeper.log` / `crontab_check.log` | 运行、保活、巡检日志（monitor 内置轮转 5MB×3） |

crontab 实际条目：`*/1 * * * * /home/ubuntu/wu2198_vip_monitor/crontab_check.sh`（**每分钟**）。

## 头号陷阱：`HERMES_HOME` 缺失导致静默失败

lark-cli 配置根 = `~/.lark-cli/<basename($HERMES_HOME)>/`。当前 `HERMES_HOME=/home/ubuntu/hermes` → 实际读 `~/.lark-cli/hermes/`。

`nohup` / `cron` / systemd 拉起的进程不继承该变量，lark-cli 去找 `~/.lark-cli/`（不存在）→ 返回 `{"ok": false, "type": "config", "subtype": "not_configured"}`。进程看着在跑、日志也不崩，但**一条消息都收不到，水位永久卡死**。

**必须做的**：所有 `subprocess.run` 都传 `env=`，至少含 `HOME`、`HERMES_HOME`、带 node 的 `PATH`、`USER`、`LOGNAME`、`LANG`：

```python
def build_cli_env():
    env = dict(os.environ)
    env["HOME"] = "/home/ubuntu"
    env["HERMES_HOME"] = "/home/ubuntu/hermes"   # 缺这行 → not_configured
    env.setdefault("USER", "ubuntu")
    env.setdefault("LOGNAME", "ubuntu")
    env.setdefault("LANG", "C.UTF-8")
    env["PATH"] = ":".join([
        "/home/ubuntu/hermes/node/bin",           # lark-cli 是 `#!/usr/bin/env node`
        "/home/ubuntu/.local/bin", "/usr/local/bin", "/usr/bin", "/bin"])
    return env
```

同一组变量也要写进 `start.sh` 与 `crontab_check.sh` 顶部的 `export`。

### 二分定位法

```bash
# 1. 最小环境复现
env -i HOME=/home/ubuntu PATH=/usr/local/bin:/usr/bin:/bin <venv>/python3 -c "..."
# 2. 逐个回加变量，看哪个让结果翻转
env -i HOME=... PATH=... HERMES_HOME=/home/ubuntu/hermes <venv>/python3 -c "..."
```

**不要先怀疑 PATH**——本例 PATH 一直是对的，缺的只有 `HERMES_HOME`。Go 二进制里 `strings` 搜不到配置路径，别浪费时间扒二进制。

### 目录别找错

- 配置：`~/.lark-cli/hermes/{config.json, logs/, locks/, cache/}`
- **加密凭证：`~/.local/share/lark-cli/*.enc` + `master.key`**（`credentialSource: local` 指这里，不在 `~/.lark-cli` 下）

## monitor.py 实现要点

### run_cli：stdout/stderr 双读

失败时 lark-cli 把 JSON 错误体打到 **stderr**。只看 stdout 只会得到 `empty output`，丢掉 `subtype: not_configured` 这类关键线索。

```python
def run_cli(args, timeout=45):
    """返回 (ok, data, err)；失败时错误 JSON 可能在 stderr。"""
    try:
        p = subprocess.run([LARK_CLI] + args, capture_output=True, text=True,
                           timeout=timeout, env=CLI_ENV, cwd="/home/ubuntu")
    except subprocess.TimeoutExpired:
        return False, None, "timeout"
    except Exception as e:
        return False, None, str(e)

    payload = (p.stdout or "").strip() or (p.stderr or "").strip()
    if not payload:
        return False, None, f"empty output rc={p.returncode}"
    try:
        data = json.loads(payload)
    except Exception:
        m = re.search(r"\{.*\}", payload, re.S)      # 混了进度行时兜底提取
        if not m:
            return False, None, payload[:300]
        data = json.loads(m.group(0))
    if isinstance(data, dict) and data.get("ok") is False:
        return False, data, json.dumps(data.get("error", {}), ensure_ascii=False)[:300]
    return True, data, ""
```

### fetch_recent_messages：失败返回 `None`，并支持多页回溯

```python
MAX_FETCH_PAGES = 5          # 单轮最多回溯 5 页 = 100 条

def fetch_recent_messages():
    all_msgs, page_token = [], None
    for page in range(MAX_FETCH_PAGES):
        args = ["im", "+chat-messages-list", "--chat-id", CHAT_ID,
                "--as", "user", "--page-size", "20", "--json"]
        if page_token:
            args += ["--page-token", page_token]
        ok, data, err = run_cli(args)
        if not ok:
            logging.error(f"lark-cli 拉取失败(page {page+1}): {err}")
            return None if not all_msgs else all_msgs   # 关键：区分「失败」与「空」
        d = data.get("data") or {}
        all_msgs.extend(d.get("messages") or [])
        if not d.get("has_more") or not d.get("page_token"):
            break
        page_token = d.get("page_token")
    # 各页可能重叠，按 message_id 去重
    seen, uniq = set(), []
    for m in all_msgs:
        if m.get("message_id") in seen:
            continue
        seen.add(m.get("message_id")); uniq.append(m)
    return uniq
```

两个要点：

1. **失败必须 `return None`**。写成 `return []` 会让拉取失败看起来像“暂时没有新消息”，水位永远不动而无人察觉。
2. **`has_more` 已实测为 `True`**（页大小 50 仍是 True），说明单页不够就永远有旧消息在更深处。交易活跃期 27~47s 一轮 + 每页 20 条，理论上有极端刷屏漏消息风险；多页回溯 + `message_id` 去重把这个窗口封死，同时限制 `MAX_FETCH_PAGES` 防无限翻页。

```python
VIP_KEYWORD = "【仅TA的真爱粉可见】"
# 不带书名号的写法同样算 VIP（群主常漏打开头的「【」）
VIP_KEYWORDS = (VIP_KEYWORD, "仅TA的真爱粉可见")
```

**匹配必须用最短完整词 `仅TA的真爱粉可见`，不能用带括号的整串。** 实测群主会漏打开头的 `【`，产出 `仅TA的真爱粉可见】` —— 带 `【` 的字面匹配直接落空，那条消息被当成公开消息静默跳过。`【仅TA的真爱粉可见】` 是 `仅TA的真爱粉可见` 的超集，所以短串同时覆盖两种写法。

命中判定与正文清洗都用元组遍历，两种写法都要从正文里剥掉：

```python
if any(k in content for k in VIP_KEYWORDS):
    body = content
    for k in VIP_KEYWORDS:
        body = body.replace(k, "")
    body = body.strip().lstrip("】").strip()   # 去掉漏打左括号残留的孤立「】」
```

**改关键字规则后用真实历史消息回放验证，不要只跑构造用例**：

```python
msgs = fetch_recent_messages(0) or []          # 拉到当前水位为止的全部历史
hit, miss = [], []
for m in msgs:
    c = (m.get("content") or "").replace("\\n", "\n")
    if m.get("msg_type") != "text":
        continue
    (hit if any(k in c for k in VIP_KEYWORDS) else miss).append(
        (m.get("message_position"), c[:40]))
print(len(hit), len(miss))
```

重点看 `miss` 里开头几个字是 `仅TA` / `TA的真爱粉` 的条目——那些才是旧规则的漏网之鱼。这一步能立刻证明规则改动值不值得。

```python
def save_state(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    os.replace(tmp, STATE_FILE)          # 原子替换，被 kill 也不会写坏
```

### poll_once 主流程

1. 读 `state`；`last_position == 0` 视为**首次运行**：只登记最新 `position`，不补发历史，直接 return。
2. `fetch_recent_messages()` 返回 `None` → `_fail_count += 1`；达到 `ALERT_THRESHOLD(3)` 时 `send_alert()`（`ALERT_COOLDOWN=1800s`）。恢复后写日志并清零。
3. 按 `message_position` 升序，逐条处理 `pos > last_position`：
   - `text` 且含任一 `VIP_KEYWORDS`（`【仅TA的真爱粉可见】` 或裸写法 `仅TA的真爱粉可见`）→ 剥掉关键字得 `body` → `build_vip_text()` → 推送；`last_is_vip = 推送是否成功`
   - `text` 不含关键词 → `last_is_vip = False`
   - `image` 且 `last_is_vip` → 正则 `img_v3_[A-Za-z0-9_-]+` 提 key → `download_image()` → 以纯图推送；失败只记日志
   - `image` 且非 VIP → 跳过；其他类型（sticker/file 等）→ `last_is_vip = False`
4. **每条消息处理完立即 `save_state()`**，不是整批处理完才存——中途崩溃只会重发一条，不会丢一批。

**注意**：图片仅靠 `last_is_vip` 标记判断是否随附，**没有时间窗口限制**（旧文档写的“10 分钟内”是错的）。`last_is_vip` 是**单条记忆的状态机**，语义就是“VIP 之后的图片继续转发，直到遇见一条公开消息为止”：VIP 文本 → `True`；其后图片跟随；中间任何一条非 VIP 文本立刻置 `False`，再往后的图片不再转发。

VIP 文本推送失败时 `last_is_vip=False`，其配图也就不转发——有意为之：正文没送到，单发图没意义。

### `send_to_wechat` / `send_alert`（实现在 monitor.py 内，gateway 延迟 import）

```python
async def send_to_wechat(text, media_files=None):
    if not WEIXIN_TOKEN or not WEIXIN_ACCOUNT_ID:
        logging.error("未找到 WEIXIN_TOKEN / WEIXIN_ACCOUNT_ID，无法转发")
        return False
    try:
        res = await send_weixin_direct(
            extra={"account_id": WEIXIN_ACCOUNT_ID},
            token=WEIXIN_TOKEN,
            chat_id=TARGET_WEIXIN_CHAT,
            message=text,
            media_files=media_files,      # ← 图片随文本一起传，不要自己再拼
        )
        ok = bool(res.get("success"))     # ← 必须看 success，不是 ok
        logging.info(f"微信推送: ok={ok} id={res.get('message_id')}")
        return ok
    except Exception as e:
        logging.error(f"微信推送异常: {e}")
        return False
```

- `WEIXIN_TOKEN` / `WEIXIN_ACCOUNT_ID` 从 `/home/ubuntu/hermes/.env` 自己读（`load_env_file()` 逐行 `split("=", 1)`，跳过 `#`），**不能依赖环境变量**。
- 返回体字段是 `success`（不是 `ok`），误写 `res.get("ok")` 会把成功当失败。
- **推送带指数退避重试 3 次**（等待 2s / 4s）：网络抖动或网关瞬时不可用不应直接丢消息。
- `send_alert()` 的冷却时间 **持久化在 `state.json` 的 `last_alert_ts`**，不是进程内存变量——否则进程一重启冷却就清零，故障持续时会在重启瞬间再告一次。
- 告警文本用 `\n\n`，与正常推送同渠道；告警也走单气泡。
- ⚠️ **`message=""` + `media_files` 不行**：实测空 message 时网关仍走 media 分支，但 `format_message("")` 返回空串、文本被跳过，行为依赖网关实现细节。**纯图必须发一条只有空格的 `" "`**，或保持与文本同发。

### 图片下载（`download_image`）

```python
def download_image(msg_id, file_key):
    out_path = os.path.join(CACHE_DIR, f"{msg_id}.png")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        return out_path                       # 幂等：已缓存直接复用，重放不会重复下载
    run_cli(["im", "+messages-resources-download",
             "--message-id", msg_id, "--file-key", file_key,
             "--type", "image", "--as", "user", "--output", out_path])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        return out_path
    logging.error(f"图片下载失败: {err}")
    return None
```

`file_key` 从消息体正则提取：`img_v3_[A-Za-z0-9_-]+`。下载后**以文件落盘为准**判成败（重定向/编码问题会让 CLI 返回 ok 而文件为空）。

### `main_loop`：启动即检 token + 每小时巡检

```python
async def main_loop():
    health = check_token_health()                 # 启动先查一次
    if health and health["days_left"] < 2:
        await send_alert("⚠️ 飞书授权即将过期 ...")
    await poll_once()                             # 先跑一轮，不等第一个 sleep
    last_health_check = time.time()
    while True:
        delay, period = next_interval()
        await asyncio.sleep(delay)
        if time.time() - last_health_check > 3600: # 每小时
            last_health_check = time.time()
            h = check_token_health()
            if h and h["days_left"] < 2:
                await send_alert(...)
        try:
            await poll_once()
        except Exception as e:
            logging.exception(f"轮询异常: {e}")     # 单轮异常不能打死主循环
```

三个要点：**先轮询再 sleep**（否则启动后要白白等 9~12 分钟）、**每小时加了一次 token 巡检**（`token_keeper.py` 是另一层）、**`poll_once` 整体 try/except**（异常只记日志，循环不死）。

### 动态轮询间隔

```python
def next_interval():
    now8 = datetime.now(timezone(timedelta(hours=8)))
    workday = now8.weekday() < 5
    t = now8.hour * 100 + now8.minute
    if workday and (915 <= t <= 1135 or 1255 <= t <= 1510):
        return 35 + random.uniform(-8, 12), "交易活跃期"     # 27~47s
    if 830 <= t <= 2200:
        return 120 + random.uniform(-25, 35), "白天非交易期"   # 95~155s
    return 600 + random.uniform(-60, 120), "夜间休眠期"        # 9~12min
```

| 时段 | 基础 | 抖动 | 实际范围 |
|---|---|---|---|
| 工作日 9:15–11:35 / 12:55–15:10 | 35s | −8~+12s | 27~47s |
| 8:30–22:00（其余） | 120s | −25~+35s | 95~155s |
| 22:00–次日 8:30 | 600s | −60~+120s | 9~12min |

抖动是**防风控**的必需品：固定秒数 24h 轮询是最典型的脚本指纹。

### 周期补偿（重要）

上表是**目标周期**，不是 sleep 时长。真实延迟 = 设计间隔 + 拉取耗时，直接 `sleep(target)` 会让交易期多出 8~14 秒。

```python
MIN_SLEEP = 5.0      # 单轮耗时超过目标周期时的兜底下限，防忙转

t0 = time.time()
await poll_once()
elapsed = time.time() - t0

target, period = next_interval()
delay = max(MIN_SLEEP, target - elapsed)
await asyncio.sleep(delay)
```

实测：早停生效后单轮耗时 1.2~1.6s（旧实现固定翻 5 页要 6.6s），补偿后“开始→开始”的真实间隔与设计值偏差 <1s。

## WeChat 投递格式（用户已定型，勿改）

```text
👑 VIP 尊享 · 仅 TA 的真爱粉可见：

📅 星期二 2026-10-20 14:18

- - - - - -

<正文>
```

```python
def build_vip_text(create_time, body):
    return ("👑 VIP 尊享 · 仅 TA 的真爱粉可见：\n\n"
            f"📅 {format_vip_time(create_time)}\n\n"
            "- - - - - -\n\n"
            f"{body}")
```

- **单气泡不碎发**：微信网关 `weixin.py` 有 `_should_split_short_chat_block_for_weixin`，2~6 行短句且首行无块头冒号时会被切成多个气泡。首行末尾的**全角冒号 `：`** 命中保护规则，保证 100% 单气泡送达。
- **双换行 `\n\n`**：单 `\n` 在**电脑版微信**会被渲染器压缩掉；必须空行分段。
- **分割线选型表**（已定型，别回头再试）：

| 方案 | 结果 |
|---|---|
| `────────`（8个实心） | ❌ 太长太实 |
| `~~~~~~~~` | ❌ 波浪线太吵 |
| `············` | ❌ 点线太密 |
| 纯留白 | 备选 |
| **`- - - - - -`** | ✅ **已选定**：疏朗、通透、手机端不折行 |

- **为什么不能用原生细线**：个人微信文本气泡是原生 Text 控件（非 Webview），不渲染 Markdown `<hr>`，也不支持 1px `#D8D8D8` Hairline；键盘符号一律渲染成与正文同色的深色。用户截图里的“原生浅灰细线”来自支持 Markdown 的客户端（企业微信/钉钉/飞书），**个人微信无法复现，不要再尝试**。
- **文字与图片分开投递**：VIP 文本一个气泡发完，配图随后单独作为纯图发送，不混排。
- **`format_vip_time`** 兼容 `%Y-%m-%d %H:%M`、`%Y-%m-%d %H:%M:%S`、ISO8601（`T`/`Z`）三种输入，输出 `星期X YYYY-MM-DD HH:mm`；中文星期数组 `["星期一".."星期日"]` 用 `dt.weekday()` 索引；解析失败原样返回。
- **正文清洗**：`content.replace("\\n", "\n")` 先还原 JSON 转义换行，再遍历 `VIP_KEYWORDS` `replace(k, "").strip()`（两种关键字写法都要剥，否则裸写法会留在正文里），最后 `lstrip("】").strip()` 去掉漏打左书名号残留的孤立右括号。群主实际产出 `仅TA的真爱粉可见】` 时，剥掉裸写法后正文开头会剩一个 `】`，不清会跟着气泡发出去。

## Token 保活（`token_keeper.py`）

**原理**：`access_token` ~2h、`refresh_token` 7 天且**一次性**（用过即换新）。lark-cli 在 access 过期后首次调用自动 refresh 并把新 refresh_token 落盘，7 天窗口整体前移。只要**永不出现连续 7 天无 API 调用**，token 就不会死。

**做法**：每 6h 打一次真实 API 强制走鉴权链路（光看一眼 `auth status` 不会触发 refresh）。

```python
def keepalive_once():
    before = run_cli(["auth", "status"])                        # 1. 记录前值
    run_cli(["im", "+chat-messages-list", "--chat-id", CHAT_ID,
             "--as", "user", "--page-size", "1", "--json"])    # 2. 真实调用触发 refresh
    after = run_cli(["auth", "status"])                         # 3. 记录后值
    refreshed = before["expiresAt"] != after["expiresAt"]       # 4. 比对判断是否续期
```

- **两种用法**：无参 = 单次执行（cron 用）；`--loop` = 常驻 6h 周期。
- **心跳文件** `token_heartbeat.json`：`last_keepalive` / `refreshed` / `before` / `after` / `days_left`。cron 靠 `last_keepalive` 决定是否补跑。
- **cron 双保险**：`crontab_check.sh` 读心跳，`now - last_keepalive > 10800s(3h)` 才补跑，避免每分钟一个 cron 把保活器刷成高频异常。
- **兜底告警**：`days_left < 2.0` → 微信推 `⚠️ 飞书授权即将过期`，提示 `lark-cli auth login` 重新扫码。`monitor.py` 内也有一套每小时巡检（`last_health_check`）作双重保险。
- **验证技巧**：不必等 token 真过期，看 `expiresAt` 是否跳变即可。实测 `tokenStatus: needs_refresh` 时首次调用返回 `ok: true`，`expiresAt` 13:21→16:21、`refreshExpiresAt` 10-20→10-27。
- **告警通道**：`notify_wechat()` 动态 import `gateway.platforms.weixin.send_weixin_direct`，失败只记日志不影响保活流程。

## 守护与判活

### start.sh

```bash
PATTERN="wu2198_vip_monitor/monitor\.py"      # 不要写成 "[w]u2198_..."

# 列出真正在跑 monitor.py 的 python3 进程（排除自身）
live_pids() {
    for p in $(pgrep -f "$PATTERN"); do
        [ "$p" = "$$" ] && continue
        tr '\0' ' ' < "/proc/$p/cmdline" 2>/dev/null \
            | grep -q "python3.*monitor\.py" && echo "$p"
    done
}

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
    # 不要直接 exit 0！持锁者可能就是本脚本拉起的 monitor 进程。
    sleep 3
    if ! flock -n 9; then
        LIVE=$(live_pids | head -1)
        [ -n "${LIVE:-}" ] && { echo "$LIVE" > "$PID_FILE"; exit 0; }
        exit 1
    fi
fi
```

之后 `live_pids` 判活 → 有则写 pid 退出；无则 `kill -TERM` → `sleep 1` → `kill -KILL` 清残留 → `nohup <venv>/python3 monitor.py >> monitor.log 2>&1 &` → 写 pid → `sleep 2` 验 `kill -0`。

#### 两个致命坑（都实际踩过）

1. **`[w]u2198_...` 方括号技巧对 `pgrep -f` 无效**。它是给 `ps | grep` 用的（防 grep 自身），而 `pgrep -f` 把 `[w]` 当作**字面量字符类**，永不会匹配到 `wu2198`。后果：判活恒为假 → 每次都以为没进程在跑。
2. **`flock -n 9` 失败时不能直接 `exit 0` 当“已在运行”**。`monitor.py` 继承了 fd 9，所以**持锁者就是 monitor 本身**；直接退出就等于“永远不再重启”。正确做法是短暂重试 + 用 `live_pids` 确认。

**判活必须限定 python3 解释器**：`bash -c "... bash start.sh"` 这类 wrapper 的命令行里也含脚本路径串，只看 `pgrep -f <路径>` 会误判“已在运行”。

### crontab_check.sh（每分钟）

1. **找真正持锁者**：`pgrep -f` 拿到候选 pid → 过滤 `$$` 自身 → 读 `/proc/$p/cmdline` 必须含 `python3.*monitor\.py` → 再看 `/proc/$p/fd` 里是否有 `monitor.lock`：
   ```bash
   for p in $(pgrep -f "wu2198_vip_monitor/monitor\.py"); do
       [ "$p" = "$$" ] && continue
       tr '\0' ' ' < "/proc/$p/cmdline" 2>/dev/null | grep -q "python3.*monitor\.py" || continue
       ls -l "/proc/$p/fd" 2>/dev/null | grep -q "monitor\.lock" && HOLDER="$p" && break
   done
   ```
2. **无 HOLDER** → `/bin/bash start.sh`；
3. **有 HOLDER** → 写 `monitor.pid`，再检查 **心跳新鲜度**（见下）；
4. 读 `token_heartbeat.json`，`now - last_keepalive > 10800s` 则补跑 `token_keeper.py`。

#### 心跳假死检测（关键）

`pgrep` 只能看到进程**存在**，看不到进程**还活着在干活**。卡在 `subprocess` 超时、死锁、await 卡死的进程 `pgrep` 照样能查到，cron 会一直认为健康。

解法：`monitor.py` 每轮 `poll_once()` 结束写 `monitor_heartbeat.json`（`last_poll_ts` / `last_poll_at` / `pid` / `fail_count` / `pushed` / `last_position`），cron 按**当前时段最长休眠**算阀值：

| 时段 | 阀值 | 依据 |
|---|---|---|
| 交易期（工作日 9:15-11:35 / 12:55-15:10） | **180s** | 设计周期 27~47s + 耗时 ~2s，留 3.5 倍余量 |
| 白天 8:30-22:00 | **600s** | 设计周期 95~155s，留 ~4 倍 |
| 夜间 22:00-8:30 | **1200s** | 设计周期 9~12min，留 ~2 倍 |

超阀 → `kill -TERM` → `sleep 2` → `kill -KILL` → `start.sh`。**阀值必须大于该时段最长休眠**，否则正常休眠中的进程会被误杀重启；也不能统一放大——早期用 600s/1800s 的写法会让白天卡死要 30 分钟才被发现。

**心跳文件缺失也要分情况**：首次部署后 monitor 还没跑满一轮时文件本来就不存在，给 5 分钟宽限（按 `monitor.pid` 的 mtime 算）；超 5 分钟仍无心跳 -> 视为“启动即假死”，强杀重启。

`start.sh` 用 `pgrep + cmdline` 粗判、`crontab_check.sh` 用 `/proc/<pid>/fd` 精确认锁——两者互补：前者防重复启动，后者确认锁真被持有。

## 故障排查顺序

“监控在跑但收不到消息”时按序查：

1. `tail -30 monitor.log` 找 `not_configured` / `node: No such file` → 环境变量问题
2. `cat state.json` 与群里最新 `message_position` 对比 → 水位卡死即拉取失败
3. `env -i HOME=... PATH=... HERMES_HOME=... <venv>/python3 -c "...fetch_recent_messages()"` 最小环境复现
4. `lark-cli auth status` 看 `tokenStatus` / `expiresAt` / `refreshExpiresAt`
5. `pgrep -af "python3 .*monitor.py"` 确认只有一个实例
6. 记录日志里**最后一条 `VIP 命中 pos=` 与当前 `last_position` 的差值**。差值 > 1 不一定是漏推（中间夹着公开消息很正常），但水位已经越过、且内容开头就是 `仅TA的真爱粉可见` 的条目，就是关键字规则漏掉的真实 VIP——要么补发，要么确认无需补发并告诉用户。

### 水位回退补发

停摆后回退 `last_position` 重放前，**必须先逐条打印这段时间的消息内容 + 是否命中 VIP**，确认无误再推进。否则会把历史普通消息当新消息重推给用户。补发完手动 `save_state()` 对齐最新 `position`。

## 频控与配额

配额按「应用 × 租户 × API」计算，**与调用身份无关**——用户身份与应用身份共用同一份配额，不存在“用户态限得更死”的独立规则。

| 等级 | 限制 |
|---|---|
| 1 | 10 次/分 |
| 3 | 100 次/分 |
| 4 | 1000 次/分且 50 次/秒 |
| 6–10 | 5–50 次/秒 |
| 21 | 3 次/秒 |

超限：HTTP 429 + `{"code": 99991400}`，响应头 `x-ogw-ratelimit-reset` 给出建议等待秒数。`im/v1/messages` 未公开标注等级。

当前最密 27s（≈2.2 次/分），距最低档 10 次/分仍有 4 倍余量，**真实风险在 token 续期而非频率**。

**用户身份硬约束**（比频控更重要）：access_token 2h 有效；refresh_token 一次性；权限随人走（只能读该用户本人可见资源）；需 `offline_access` 才发 refresh_token。

## 上线自检清单

1. **最小环境**启动：`env -i HOME=/home/ubuntu PATH=/usr/local/bin:/usr/bin:/bin <venv>/python3 -c "..."` 必须拿到条数而非 `not_configured`
2. `state.json` 的 `last_position` 与群内最新 `message_position` 对齐
3. `token_keeper.py` 单次执行返回 `{"ok": true}`，`token_heartbeat.json` 的 `last_keepalive` 刷新
4. 用 `build_vip_text()` 真推一条，日志出现 `微信推送: ok=True`
5. `pgrep -af "python3 .*monitor.py"` 只有一个进程；`tail monitor.log` 确认按预期时段休眠
6. 隔一轮再看 `state.json`，`last_position` 已自动推进

## 运维建议（已完成加固 + 仍存限制）

### 已完成的加固（勿回退）

| 项 | 做法 | 验证方式 |
|---|---|---|
| 日志轮转 | `RotatingFileHandler(maxBytes=5MB, backupCount=3)`；**只挂文件 handler** | 看 `monitor.log` 单行不重复 |
| 缓存回收 | 每 24h `sweep_cache()` 删 7 天前配图（由 `state.last_cache_sweep` 控制频率） | 造 8 天前文件 → 跑一次 → 文件消失 |
| 告警冷却持久化 | `state.json` 的 `last_alert_ts`，重启不清零 | 重启后立即再触发失败，应无重复告警 |
| 假死检测 | 每轮写 `monitor_heartbeat.json`，cron 按时段阈值判（交易期 180s / 白天 600s / 夜间 1200s） | 交易期伪造 200s 前心跳 → cron 应强杀重启并换 pid |
| 多页早停 | 首页最旧 `position <= last_pos` 立即 break，最多 5 页 | 单轮请求数 = 1，而不是固定 5 页 |
| 推送重试 | 指数退避 3 次（2s/4s） | 日志出现 `第 1/3 次` 警告后才成功 |
| 启动即轮询 | `main_loop` 先 `poll_once()` 再进 sleep | 重启后 2s 内即出现拉取日志 |
| 周期补偿 | `sleep(max(5, target - elapsed))` | 日志一对“目标周期/本轮耗时/休眠”相加等于目标值 |
| 告警带原因 | `_last_cli_error` 存最近一次 `run_cli` 失败原因，写进告警正文 | 手动断开 token → 告警里应直接看到 `not_configured` 等关键字 |
| 送达统计 | `state.push_stats = {date, pushed, failed}`，每日滚动 | `cat state.json` 能看到今日推送/失败计数 |
| 关键字双写法 | `VIP_KEYWORDS` 元组同时认 `【仅TA的真爱粉可见】` 与裸写法 | 历史回放里 `仅TA的真爱粉可见】` 开头那条应命中 |
| 残留括号清理 | 剥完关键字再 `lstrip("】")`，去掉漏打左括号留下的孤立右括号 | pos=1435 回放 → 正文应以「在10月9日」开头，而不是「】」 |
| 心跳分时段阀值 | 交易期 180s / 白天 600s / 夜间 1200s | 伪造 200s 前心跳且在交易期 → cron 应强杀重启 |
| 心跳缺失宽限 | 无心跳且 pid 文件存在 <5min 不重启 | 首次部署不被误杀 |

#### 日志双写坑

如果同时挂 `StreamHandler(sys.stdout)` + `RotatingFileHandler(same file)`，而 `start.sh` 又把 stdout `>>` 重定向到同一个 `monitor.log`，**每行日志会出现两次**。只挂文件 handler 即可（stdout 重定向保留，兼顾前台调试）。

### 仍存在的限制

1. **`last_position == 0` 首次运行不补发**：有意为之，但意味着首次部署前已存在的 VIP 消息永不转发，部署后需人工回查。
2. **图片链路未获真实验证**：本群 50 条采样全部 `text`，`img_v3` 零命中。`img_v3_` 正则与 `messages-resources-download` 参数照 CLI 文档写，待真图出现时才能确认。
3. **纯图推送传 `" "`（单个空格）**：`message=""` 会走文本分支被判空，只发 media 不一定能成气泡。
4. **硬编码常量**：`CHAT_ID` / `VIP_KEYWORDS` / 微信目标均写在文件头，换群需改代码。要复用需外提 `config.json`。
5. **`crontab_check.log` 只截断不全轮转**：超 1MB 时保留尾部 200KB，不保留历史段。

### 可选的下一步

| 优先级 | 改动 | 收益 |
|---|---|---|
| 中 | 配置外部化（`config.json`） | 一套代码多群复用 |
| 中 | VIP 正文分段重排（按句号/分号） | 手机端可读性 |
| 低 | 群消息关键词可多个 + 各自目标通道 | 复用性 |
| 低 | 心跳文件加 `last_fetch_ok_ts` 与 `api_latency_ms` | 提前发现飞书变慢 |

### 改代码时的硬约束

- 不要把 `send_weixin_direct` 改成自己调 HTTP：`media_files` 与单气泡逻辑都在网关里。
- 不要改 `WEIXIN_TOKEN` 的读取方式：网关 `.env` 是唯一源。
- 不要给 `fetch_recent_messages` 加缓存：水位机制已保证幂等，缓存会引入水位错位。
- 不要在 `poll_once` 里 `await` 阻塞型操作后忘记 `save_state()`：每条消息处理完立即存。
- 不要把假死阀值改得比该时段最长休眠还小：正常休眠会被误杀。
- 不要在 `start.sh` 里用 `flock -n 9 || exit 0`：持锁者就是 monitor，会让守护永远不再重启。

## 已知限制

- 个人微信私聊不支持原生富文本卡片（仅企业微信/服务号支持），只能用「高对比度文本排版 + 原生高清图片」
- 外部群无法拉 bot 时只能轮询；能自拉 bot 的群优先用 WebSocket/Webhook 事件监听（0 轮询开销）
- `crontab_check.sh` 的保活补跑与 `token_keeper.py --loop` 二选一，同时跑会重复调用
- 解释器固定为 `/home/ubuntu/hermes/hermes-agent/venv/bin/python3`（**不是** `~/hermes/venv/bin/python3`，后者不存在）
