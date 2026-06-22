# System Map

## Source-of-truth modules

- `backend/app/main.py`
- `backend/app/api/routes.py`
- `backend/app/services/backtest_service.py`
- `backend/app/services/meihua.py`
- `backend/app/services/analytics.py`
- `backend/app/services/repository.py`
- `backend/app/services/official_source.py`
- `backend/app/services/sync_service.py`
- `frontend/src/pages/HomePage.tsx`
- `frontend/src/components/RecommendationPanel.tsx`
- `frontend/src/components/DivinationReplayPanel.tsx`
- `frontend/src/lib/api.ts`

## Main capability areas

- Live divination: `/api/divination`
- Replay: `/api/divination-runs`
- Official data sync: `/api/sync/status`, `/api/sync/run`
- History and analytics: `/api/history`, `/api/analytics`
- Full-history cache: `/api/full-history-cache/status`, `/api/full-history-cache/rebuild`, `/api/full-history-cache/jobs/{job_id}`
- Backtests: `/api/backtest`, `/api/backtest/jobs`, `/api/backtest/jobs/{job_id}`, `/api/backtest/jobs/{job_id}/cancel`
- Saved schemes: `/api/saved-schemes`, `/api/saved-schemes/batch`, `/api/saved-schemes/manual`
- Manual draw overrides: `/api/saved-schemes/issues/{issue}/manual-result`

## Frontend tabs

- 推演中心
- 保存方案
- 实盘复盘
- 历史回测
- 历史数据
