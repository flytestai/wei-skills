---
name: caipiao-analyzer
description: Unified 大乐透 skill: preserves the original flytestai/caipiao backend wrapper for prediction/backtest/sync, and adds local aggregation/statistics/regeneration/save/check workflow for merging backend-generated schemes with externally collected number groups.
---

# Caipiao Analyzer

## Purpose

This skill is now a **unified 大乐透工作流 skill** with two coordinated capability lines:

### 能力线 A：原始 `flytestai/caipiao` backend 包装层
继续保持 **logic-preserving wrapper** 原则：
- 不重写原项目的推算 / 回测 / 分析 / 同步逻辑
- 原始预测、回测、分析、同步结果仍以 backend 为准
- 本 skill 只负责启动、健康检查、参数映射、自然语言路由、结果格式化

### 能力线 B：本地汇总统计 / 二次重组 / 保存投注 / 开奖核对
用于承接用户的真实使用流程：
- 先通过 `caipiao-analyzer` backend 生成若干组大乐透组合
- 再把这些组合与**其他来源收集的号码组合**一起汇总
- 统一做前区 / 后区频次统计
- 基于累计统计结果重新生成用户要的参考组合
- 仅在用户明确要求时保存投注
- 开奖后按期号自动核对、判断奖级、估算可精确奖金

**合并后的核心原则**：
- **生成能力** 优先来自原 `flytestai/caipiao` backend
- **汇总、频次统计、重组、保存、核对** 由本 skill 的本地流程负责
- 不把本地频次重组伪装成 backend 原始预测

## Backend Source-of-Truth

The skill depends on the following original modules:

| Module | Role |
|---|---|
| `backend/app/services/meihua.py` | 梅花易数推算引擎 |
| `backend/app/services/backtest_service.py` | 历史回测引擎 |
| `backend/app/services/analytics.py` | 频率、遗漏、奇偶分析 |
| `backend/app/services/repository.py` | 数据存取层 |
| `backend/app/services/official_source.py` | 官方开奖数据源 |
| `backend/app/services/ai_gateway.py` | AI 模型网关 |
| `backend/app/models.py` | Pydantic 数据模型 |
| `backend/app/api/routes.py` | FastAPI 路由定义 |

---

## Backend Startup Workflow

```
1. cd <caipiao-repo-clone>/backend
2. pip install -r requirements.txt
3. uvicorn app.main:app --reload --port 8000
4. curl http://localhost:8000/health  → {"status":"ok"}
```

Default API base: `http://localhost:8000`

The backend auto-runs initial data sync and starts a scheduler for periodic sync on startup.

---

## Readiness Checks (Before Calling Analysis Endpoints)

Before the skill calls any analysis endpoint, it should check:

1. **Backend reachable**: `GET /health`
2. **Sync status**: `GET /api/sync/status` — ensure data is not empty
3. **Cache state** (for backtest/divination): `GET /api/full-history-cache/status`

If any check fails, tell the user what to fix before proceeding.

---

## Unified Workflow

当用户的目标是：
1. 先生成几组大乐透组合
2. 再把这些组合和别处拿到的号码混在一起
3. 做统一频次统计
4. 再重新生成自己最终要买的组合

优先按下面流程处理：

### 第一步：先调用原 backend 生成候选组合
适用表达：
- `先帮我推 5 组大乐透`
- `先生成几组参考号码`
- `先用 caipiao 出 3 组`

行为：
- 先走原 backend 的 `POST /api/divination`
- 返回原始推算组合
- 明确说明：这是 backend 原始生成结果

### 第二步：把 backend 组合与外部组合一起汇总
适用表达：
- `把我这几组也一起加进去统计`
- `和其他地方的号码一起汇总`
- `把这些组合都作为样本`

行为：
- 将 backend 生成结果和用户补充的号码组都按统一格式整理
- 追加到本地样本记录中
- 作为后续频次统计基础

### 第三步：做统一频次统计
行为：
- 统计前区 `01-35` 频次
- 统计后区 `01-12` 频次
- 支持高频 / 中频 / 低频分层
- 排序规则：**频次降序，频次相同则号码升序**

### 第四步：基于累计样本重新生成参考组合
行为：
- 使用本地脚本按累计频次做“重组参考”
- 这是**二次重组结果**，不是 backend 原始预测
- 输出时要明确区分：
  - `原始推算结果`
  - `汇总统计后二次重组结果`

### 第五步：明确保存边界
- 生成组合 ≠ 自动保存投注
- 只有当用户明确说 `保存` / `按每注 X 倍保存` / `保存成下一期方案` 才能写入投注记录

### 第六步：开奖后核对
行为：
- 查询目标期号开奖结果
- 核对本地保存投注
- 输出奖级、倍数后奖金、可精确汇总奖金
- 若涉及浮动奖 / 追加奖 / 派奖，明确提示仍以官方公告为准

---

## Wrapped Capability Areas

### 1. History & Data Sync

#### Query draws
- Request: "最近开奖历史" / "查看第xxx期" / "近N期开奖"
- API: `GET /api/history?limit=N`
- Returns: list of `LottoDraw` with issue, draw_date, front_numbers, back_numbers

#### Sync status
- Request: "数据同步状态" / "数据是否最新"
- API: `GET /api/sync/status`

#### Manual sync
- Request: "同步最新数据" / "刷新开奖数据"
- API: `POST /api/sync/run?full_refresh=true`

---

### 2. Analytics

- Request: "分析一下" / "数据分析" / "热号冷号" / "频率统计"
- API: `GET /api/analytics?limit=N`
- Returns: `AnalyticsResponse` with front/back frequency, omission, odd/even stats

**Result formatting rules:**
- Highlight top-5 hot front numbers and top-3 hot back numbers
- Show longest-omission numbers
- Present odd/even ratio clearly
- Mention total draws analyzed

---

### 3. Divination / Prediction (推算)

- Request: "帮我推算" / "预测下期号码" / "占卜" / "推荐号码"
- API: `POST /api/divination`
- Params:

| Param | Type | Range | Default | Description |
|---|---|---|---|---|
| `issue` | string | 如 "25065" | None | 目标期号 |
| `timestamp` | ISO string | - | None | 自定义时间戳 |
| `scheme_count` | int | 1-50 | 3 | 返回方案数 |
| `strategy_mode` | string | `multi_cover` / `single_hit` / `smart_balance` | `smart_balance` | 策略模式 |
| `ai_config` | AIConfigRequest | - | None | AI 模型配置 |

**Strategy modes:**
- `multi_cover` — 多区覆盖，生成号码尽可能覆盖不同区段
- `single_hit` — 单点击中，聚焦高概率点位
- `smart_balance` — 智能平衡（默认），兼顾覆盖率和命中率

**AI config** (required for AI-enhanced predictions):
```json
{
  "enabled": true,
  "base_url": "https://api.openai.com/v1",
  "api_key": "sk-xxx",
  "model": "gpt-4o",
  "system_prompt": "You are a lottery analysis expert..."
}
```

**Result formatting rules:**
- Show the divination seed (issue/timestamp)
- Show the hexagram chain (本卦/互卦/变卦)
- Split front/back recommendations clearly
- Per scheme: show label, confidence, front_numbers, back_numbers, strategy, rationale
- Highlight AI analysis when present

---

### 4. Backtesting

#### Direct backtest
- Request: "回测最近N期" / "回测" / "测试策略准确率"
- API: `POST /api/backtest`
- Params:

| Param | Type | Default | Description |
|---|---|---|---|
| `recent_issues` | int | 100 | 回测最近N期 |
| `scheme_count` | int | 3 | 每期生成方案数 |
| `strategy_mode` | string | `multi_cover` | 策略模式 |
| `ticket_mode` | string | `basic` | `basic` / `additional` |
| `compare_modes` | bool | false | 是否对比多策略 |
| `ai_config` | AIConfigRequest | None | AI 配置 |

#### Async backtest jobs
- Create: `POST /api/backtest/jobs` (same params as direct)
- List: `GET /api/backtest/jobs`
- Get: `GET /api/backtest/jobs/{job_id}`
- Cancel: `POST /api/backtest/jobs/{job_id}/cancel`

**Flow guidance:**
- For small ranges (<50): use direct `/api/backtest`
- For large ranges: use async jobs → poll → get result

---

### 5. Full History Cache

The cache pre-computes backtest data for fast queries. Required before backtesting with AI.

- Status: `GET /api/full-history-cache/status?scheme_count=3&ticket_mode=basic`
- Rebuild: `POST /api/full-history-cache/rebuild?scheme_count=3&ticket_mode=basic&force=true`
- Job status: `GET /api/full-history-cache/jobs/{job_id}`

**Flow guidance:**
1. Check status first
2. If stale or missing, start rebuild
3. Wait for rebuild to complete
4. Then run backtest

---

### 6. Saved Schemes

- List: `GET /api/saved-schemes?limit=100`
- Save one: `POST /api/saved-schemes`
- Batch save: `POST /api/saved-schemes/batch`
- Manual ticket: `POST /api/saved-schemes/manual`
- Delete: `DELETE /api/saved-schemes/{id}`
- Delete by issue: `DELETE /api/saved-schemes/issues/{issue}`

---

## Local Aggregation / Regeneration Layer

除了 backend 包装能力外，本 skill 还内置本地大乐透汇总流程。

### 本地数据文件
- `records.md`：累计样本号码组
- `bets.md`：用户明确保存的投注方案
- `draw_results.md`：开奖核对结果
- `state.md`：统计摘要、最近跟踪期号、最近核对期号、最近生成组合
- `scripts/parse_and_stats.py`：本地汇总、统计、重组、保存、核对脚本

### 本地脚本能力
- `add`：追加样本号码
- `stats`：统计前后区频次，支持完整频次与高/中/低频分层
- `generate`：按累计样本重组生成参考组合
- `fetch-issue`：查询最近已开奖期号与下一期期号
- `save-bets`：按期号、倍数、普通/追加类型保存投注方案
- `check-draw`：按期号自动查询开奖结果并核对已保存投注，也支持 `--draw` 手动覆盖开奖号码

### 合并后推荐使用方式

#### 场景 1：只想用原 backend 推算
直接走 backend 能力，不强行使用本地统计层。

#### 场景 2：想把 backend 结果和外部结果混合后再重组
优先走：
1. backend 生成候选组合
2. 将候选组合与外部组合一起写入 `records.md`
3. 运行本地统计
4. 再用 `generate` 输出最终参考组合

#### 场景 3：想长期追踪、保存、开奖核对
在本地汇总层继续使用：
- `save-bets`
- `check-draw`

### 关键边界
- backend 原始推算结果 ≠ 本地频次重组结果
- 本地重组只是一种“样本汇总后的二次整理参考”
- 不能把频次重组说成官方预测、精准预测或保证中奖

---

## Natural Language → API / Workflow Mapping

| User says | Action |
|---|---|
| 最近开奖历史 | `GET /api/history?limit=20` |
| 最近N期 | `GET /api/history?limit=N` |
| 分析/统计/热号 | `GET /api/analytics` |
| 推算/预测/占卜 | `POST /api/divination` with defaults |
| 推算N个方案 | `POST /api/divination` with `scheme_count=N` |
| 用multi_cover推算 | `POST /api/divination` with `strategy_mode=multi_cover` |
| 带AI推算 | `POST /api/divination` with `ai_config` |
| 回测 | `POST /api/backtest` |
| 回测最近N期 | `POST /api/backtest` with `recent_issues=N` |
| 异步回测 | `POST /api/backtest/jobs` |
| 查看回测任务 | `GET /api/backtest/jobs` |
| 查看保存的方案 | `GET /api/saved-schemes` |
| 保存这个方案 | `POST /api/saved-schemes` |
| 数据同步状态 | `GET /api/sync/status` |
| 同步数据 | `POST /api/sync/run` |
| 缓存状态 | `GET /api/full-history-cache/status` |
| 重建缓存 | `POST /api/full-history-cache/rebuild` |
| 列出AI模型 | `POST /api/ai/models` |
| 把这些号码都汇总统计 | 本地 `records.md` + `stats` |
| 把 backend 结果和外部号码一起重组 | backend 生成 → 本地 `add` / `stats` / `generate` |
| 保存成下一期投注方案 | 本地 `save-bets` |
| 帮我核对上一期保存的号码 | 本地 `check-draw` |

---

## Error Handling Rules

| Error | Cause | Action |
|---|---|---|
| Backend unreachable | Service not started | Tell user to run `uvicorn app.main:app --port 8000` |
| `400 AIConfigurationError` | Missing/invalid AI config | Tell user to configure AI provider |
| `502 AIGenerationError` | AI call failed | Retry or suggest checking API key/model |
| `409 cache stale` | Cache outdated | Instruct user to rebuild cache |
| `404` on job/scheme | Object not found | Return clear not-found message |
| 开奖接口字段不完整 | 浮动奖 / 派奖信息缺失 | 只输出基础奖级与可精确金额，并注明以官方公告为准 |

---

## Output Style

- Lottery numbers: `前区 01 12 23 34 35 | 后区 06 12`
- Hot numbers: highlight with count
- Predictions: show confidence, strategy, and rationale
- Backtest: show hit count, hit rate, per-issue detail
- Always separate front (前区) and back (后区) numbers clearly
- Chinese output for Chinese-language requests

### 合并 skill 的额外输出要求
当同一次任务里既有 backend 原始推算结果，又有本地汇总后二次重组结果时，要明确分区输出：

1. `原始推算结果（来自 caipiao backend）`
2. `汇总统计后二次重组结果（来自本地频次重组）`

避免让用户误以为两者是同一种来源。

---

## Boundary

This skill still **must not re-implement or fake** the original `flytestai/caipiao` prediction engine.  
All backend prediction, analysis, backtest, sync, and scheme-management logic still comes from the original code.  

At the same time, this merged skill now additionally owns the **local aggregation / frequency-stat / regeneration / save / draw-check** workflow for 大乐透 usage after numbers are generated.

### 最终边界总结
- **推算 / 回测 / 同步 / 原始分析** → 以 backend 为准
- **汇总外部号码、统一频次统计、二次重组、保存投注、开奖核对** → 以本地 workflow 为准
- 两者可以串联，但不能混淆来源
