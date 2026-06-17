---
name: caipiao-analyzer
description: Logic-preserving wrapper around the flytestai/caipiao FastAPI backend. All prediction, backtest, analytics, and sync logic comes from the original repo implementation — this skill orchestrates startup, health checks, parameter mapping, natural-language entry, and result formatting.
---

# Caipiao Analyzer

## Purpose

This skill is a **logic-preserving wrapper** around the original `flytestai/caipiao` backend, a Super Lotto (大乐透) analysis platform.

**Core principle**: Do not re-implement or fake the original prediction logic. All lottery analysis, divination, backtest, sync, and scheme-management results must come from the original backend implementation. This skill is responsible for:

- starting the backend
- verifying readiness
- translating natural-language requests into correct API calls
- formatting and explaining results

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

## Natural Language → API Mapping (Full)

| User says | API + params |
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

---

## Error Handling Rules

| Error | Cause | Action |
|---|---|---|
| Backend unreachable | Service not started | Tell user to run `uvicorn app.main:app --port 8000` |
| `400 AIConfigurationError` | Missing/invalid AI config | Tell user to configure AI provider |
| `502 AIGenerationError` | AI call failed | Retry or suggest checking API key/model |
| `409 cache stale` | Cache outdated | Instruct user to rebuild cache |
| `404` on job/scheme | Object not found | Return clear not-found message |

---

## Output Style

- Lottery numbers: `前区 01 12 23 34 35 | 后区 06 12`
- Hot numbers: highlight with count
- Predictions: show confidence, strategy, and rationale
- Backtest: show hit count, hit rate, per-issue detail
- Always separate front (前区) and back (后区) numbers clearly
- Chinese output for Chinese-language requests

---

## Boundary

This skill is **not** a reimplementation of the caipiao engine.  
It is a stable, documented wrapper around the original `flytestai/caipiao` backend.  
All prediction, analysis, backtest, sync, and scheme-management logic is executed by the original code.
