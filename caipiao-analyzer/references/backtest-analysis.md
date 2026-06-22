# Backtest Analysis

## Endpoints

- `POST /api/backtest`
- `POST /api/backtest/jobs`
- `GET /api/backtest/jobs`
- `GET /api/backtest/jobs/{job_id}`
- `POST /api/backtest/jobs/{job_id}/cancel`

## Request themes

- `recent_issues`
- `scheme_count`
- `strategy_mode`
- `ticket_mode`
- `ai_replay_mode`
- `compare_modes`
- `tuning_profile_override`
- `multiple`

## Workflow

1. Decide whether the run should be synchronous or job-based.
2. Submit the backtest request.
3. Read profile, threshold, and stability metrics from the result.
4. Compare issue hit rate, overall win rate, drawdown, and miss streak before recommending changes.

## Reporting priorities

- overall win rate
- issue hit rate
- threshold selection reason
- selected profile or mode
- max drawdown
- max miss streak

## Use job mode when

- the run is large
- the user wants progress polling
- the frontend should remain responsive
