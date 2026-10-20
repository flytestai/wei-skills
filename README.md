# Wei Skills

OpenClaw / Hermes 技能集合，聚焦 **刷题、课程教学、业务分析、彩票数据、图片生成、消息监控** 六类可复用技能。

## 技能总览

| 技能 | 定位 | 运行依赖 |
| --- | --- | --- |
| `python-testdev-drill` | Python 测试开发面试刷题 + 全量分级题库 | Python 3 |
| `chat-course-coach` | 聊天式课程教学与进度管理 | OpenClaw |
| `caipiao-analyzer` | 大乐透历史、分析、推算与回测 | `flytestai/caipiao` FastAPI 后端 |
| `three-digit-lottery-divination` | 排列三 / 福彩3D 官方数据与娱乐推演 | Python 3、官方开奖接口 |
| `openai-image-generate` | 根据提示词生成并直接返回图片 | OpenAI 兼容图片接口 |
| `feishu-vip-monitor` | 飞书群关键词监控并转发微信 | `lark-cli`、Hermes |

---

## 1. python-testdev-drill

Python 测试开发工程师面试刷题系统，包含 **15 个专项模块** 和 **7,478 道全量分级题库**。

### 专项模块

- Python基础手写代码题
- Python编程基础理论面试题
- Python高阶编程
- 自动化测试题
- Pytest框架
- 测试开发面试题
- 测试工程化与 CI/CD
- 性能测试
- 中间件
- 数据库
- Linux
- HTTP 协议与接口测试
- Selenium 与 UI 自动化
- 测试理论与用例设计
- 测试场景与排查

### 全量分级题库

按「领域 → 专题/知识点」组织，共 **7,478 道题、18 个领域、102 个专题**：

- 每题包含：题目、选项、答案、正确选项、解析、题型、难度
- 无空答案、无空解析
- 43 道缺失文字答案的题目已补全
- 371 道缺失解析的题目已补全解析
- 123 个 Markdown 题目文件，单文件最多 150 题
- 提供 `bank/bank.json` 结构化数据与 `bank/query_bank.py` 查询工具
- 已清除机构名、品牌名、原始题目 ID、来源字段和外部文章链接

题库入口：[python-testdev-drill/bank/index.md](python-testdev-drill/bank/index.md)

查询示例：

```bash
python python-testdev-drill/bank/query_bank.py stats
python python-testdev-drill/bank/query_bank.py domains
python python-testdev-drill/bank/query_bank.py topics --domain 功能测试
python python-testdev-drill/bank/query_bank.py random --domain 功能测试 --topic 测试用例 --count 5
python python-testdev-drill/bank/query_bank.py search --keyword 接口 --limit 10
```

### 其他能力

- 支持一次刷多题
- 支持按模块刷题 / 随机刷题 / 按领域或专题刷全量题库
- 支持错题集、收藏题库、自建题库
- 刷题历史自动沉淀，模块内优先去重
- 支持收藏题目、保存自建题目、持久化进度
- 错题按 1 / 3 / 7 / 15 天间隔复习

### 典型用法

- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`
- `随机刷 4 道题`
- `从功能测试领域随机抽 10 道题`
- `按专题刷 接口测试`
- `刷错题集`
- `保存这道题到 测试开发面试题`

---

## 2. chat-course-coach

聊天式课程教学系统。

**能力特性**
- 自然语言描述学习目标，自动生成课程目录
- 微信聊天风格逐课教学
- 细粒度进度跟踪（模块 → 课 → 段）
- 掌握度分层、复盘机制、回顾机制
- 项目主线贯穿
- 支持系统模式 / 面试模式 / 实战模式
- 支持跨会话续学

**典型用法**
- `我想系统学 FastAPI`
- `继续学习 FastAPI`
- `查看当前学习进度`

---

## 3. caipiao-analyzer

大乐透分析 skill（逻辑封装型 wrapper）。

**能力特性**
- 依赖原 `flytestai/caipiao` FastAPI 后端
- 完整映射：
  - 历史查询
  - 数据分析
  - 梅花推算
  - AI 预测
  - 回测
  - 方案管理
- 不重新实现逻辑，原仓库代码作为唯一逻辑源
- 包含后端启动流程、健康检查、参数映射、错误处理规则

**典型用法**
- `最近开奖历史`
- `帮我推算号码`
- `回测最近100期`

---

## 4. three-digit-lottery-divination

排列三 / 福彩3D 官方开奖数据查询与娱乐推演。

**能力特性**
- 拉取指定期数的官方开奖历史并校验数量
- 汇总号码频次、遗漏、位置分布
- 使用固定规则的梅花易数推演下一期候选号码
- 排列三与福彩3D 可分开或同时处理
- 输出数据来源、期号范围、最新开奖、推演过程和娱乐提示
- 不投注、不购彩、不承诺收益，明确直选概率为 `1/1000`

**典型用法**
- `查最近 100 期排列三`
- `福彩3D 最近 50 期数据分析`
- `排列三和福彩3D 各推演一个号码`

---

## 5. openai-image-generate

根据自然语言提示词调用 OpenAI 兼容图片接口生成图片，并直接返回本地图片文件。

**能力特性**
- 接收提示词、尺寸、风格、张数等参数
- 从本地私有配置读取接口地址、密钥和模型
- 默认 `1024x1024`、1 张，优先高质量输出
- 生成结果直接发送本地文件，不发送外链
- 首次超时可自动做一次保守参数重试
- 不在文档或脚本中硬编码敏感信息

**典型用法**
- `帮我生成一张赛博朋克风格的城市夜景`
- `画一只在敲代码的柴犬`
- `做一张适合做公众号封面的测试主题插画`

---

## 6. feishu-vip-monitor

飞书群 VIP 关键词监控转发。轮询指定飞书群，识别带关键词的消息，连同配图转发到微信，并用消息水位杜绝重复消费。

**能力特性**
- 用 `message_position` 水位消费消息，重启、崩溃都不会重复推送
- 三档抖动轮询，避开飞书风控：交易期 27~47s / 白天 95~155s / 夜间 9~12min
- 多页回溯**按水位早停**——飞书 `has_more` 恒为 `true`，不能当停止条件
- 周期补偿 `sleep(max(5, target - elapsed))`，拉取耗时不会累积成轮询漂移
- cron 每分钟巡检，心跳分时段阈值（180s / 600s / 1200s），超时强杀重启
- token 保活常驻：`refresh_token` 只能用一次，必须提前轮换
- 推送重试、告警冷却持久化、日志轮转、配图缓存回收
- 文本气泡排版：标题 + 图标 + 浅色短虚线 + 正文，手机/电脑版微信均正确换行

**主要踩坑（已在实现中修复）**
- `HERMES_HOME` 未注入 → `lark-cli` 返回 `not_configured`，进程在跑但一条收不到
- `pgrep -f '[w]u2198'` 方括号被当字面字符类，既防不了自匹配也匹配不到进程
- `flock -n || exit 0` 导致：持锁者正是本脚本拉起的进程时误判为“已在运行”
- `RotatingFileHandler` + `StreamHandler` + `nohup` 同文件，每条日志写两遍

**典型用法**
- `监控这个飞书群，有真爱粉可见的消息就转发给我`
- `看看监控进程是不是假死了`
- `飞书 token 快过期了，帮我保活`

---

## 安装方式

```bash
git clone https://github.com/flytestai/wei-skills.git

# OpenClaw 技能
cp -r wei-skills/python-testdev-drill ~/.openclaw-autoclaw/skills/
cp -r wei-skills/chat-course-coach ~/.openclaw-autoclaw/skills/
cp -r wei-skills/caipiao-analyzer ~/.openclaw-autoclaw/skills/
cp -r wei-skills/three-digit-lottery-divination ~/.openclaw-autoclaw/skills/
cp -r wei-skills/openai-image-generate ~/.openclaw-autoclaw/skills/

# Hermes 技能
cp -r wei-skills/feishu-vip-monitor ~/hermes/shared/skills/
```

> `feishu-vip-monitor` 是 Hermes skill，装到 Hermes 的 skills 目录；其余装到 OpenClaw。`caipiao-analyzer` 使用前需先启动 `caipiao` 后端；`openai-image-generate` 需先在本地私有配置中填写图片接口信息。

## 使用说明

安装后直接在对话中调用对应能力，无需额外命令前缀。

### 刷题

- `继续 Python基础手写代码题`
- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`
- `从数据库领域随机抽 5 道题`
- `刷错题集`
- `刷收藏题`

### 学习课程

- `我想系统学 FastAPI`
- `继续学习 FastAPI`
- `查看学习进度`

### 大乐透分析

> 使用前需先启动 `caipiao` 后端

- `最近开奖历史`
- `帮我推算号码`
- `回测最近100期`

### 排列三 / 福彩3D

- `查最近 100 期排列三`
- `福彩3D 最近 50 期数据分析`

### 图片生成

- `生成一张赛博朋克风格的城市夜景`
- `画一只在敲代码的柴犬`

### 飞书群监控

> 依赖已授权的 `lark-cli`，且必须注入 `HERMES_HOME`

- `监控这个飞书群，有 VIP 消息就转发给我`
- `监控进程还在跑吗`

## 仓库结构

```text
wei-skills/
├── python-testdev-drill/           # 刷题系统 + 全量分级题库
│   ├── bank/                       # 7,478 题，按领域/专题组织
│   ├── SKILL.md
│   └── MODULE_*.md
├── chat-course-coach/              # 聊天式课程教学
├── caipiao-analyzer/               # 大乐透分析
├── three-digit-lottery-divination/ # 排列三 / 福彩3D
├── openai-image-generate/          # 图片生成
└── feishu-vip-monitor/             # 飞书群监控
```

## 仓库定位

这个仓库主要维护可复用的 OpenClaw / Hermes skills，强调：

- 可持久化
- 可续用
- 面向真实工作流
- 兼顾说明文档与可直接使用的技能结构
- 数据、脚本、状态和说明放在同一个 skill 内，安装后即可运行
