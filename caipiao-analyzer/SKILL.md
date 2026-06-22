---
name: caipiao-analyzer
description: Full-system operator skill for the flytestai/caipiao lottery platform. Use when an agent needs to run, inspect, troubleshoot, or operate the original caipiao backend and frontend across live divination, official-data sync, full-history cache rebuilds, backtests, saved schemes, replay logs, or local service management. This skill preserves the original repo logic and only wraps startup, readiness checks, parameter mapping, and result formatting.
---

# Caipiao Analyzer

Operate the original `flytestai/caipiao` system as a logic-preserving wrapper skill.

## Core rule

Do not re-implement the lottery engine. Use the original repository services and APIs as the source of truth for:

- live divination
- sync status and official-data refresh
- analytics
- full-history cache
- backtests and tuning
- saved schemes and manual ticket records
- replay logs

## Start here

1. Read `references/system-map.md`.
2. Match the user request to one of these workflows:
   - live divination
   - history sync / analytics
   - full-history cache
   - backtest analysis
   - saved schemes
   - replay / frontend ops
3. Read the matching reference file before acting.

## Default local runtime

- Backend repo source: original `flytestai/caipiao`
- Backend URL: `http://127.0.0.1:8011`
- Frontend URL: `http://127.0.0.1:5180`
- Backend health: `GET /health`
- API base: `http://127.0.0.1:8011/api`

## Readiness checks

Before calling analysis endpoints:

1. confirm backend health
2. confirm sync status is readable
3. confirm full-history cache status is readable for the requested `scheme_count`

If any check fails, explain the failure and fix the runtime before proceeding.

## Runtime expectations

- Backend is FastAPI and serves under `/api`.
- Frontend is Vite + React.
- Backend startup triggers a recent official sync automatically.
- Full-history cache is persistent and should be updated incrementally rather than rebuilt blindly.
- `should_observe` is a risk label, not proof that returned schemes are unavailable.

## Task routing

- For current-number generation: read `references/live-divination.md`
- For latest draw or refresh requests: read `references/history-sync.md`
- For cache rebuild / stale cache / missing issues: read `references/full-history-cache.md`
- For optimization and historical evaluation: read `references/backtest-analysis.md`
- For save/delete/manual ticket flows: read `references/saved-schemes.md`
- For browser-visible bugs and replay checks: read `references/replay-and-frontend-ops.md`

## Guardrails

- Do not delete saved schemes, manual results, or cache artifacts unless the user explicitly asks.
- Do not force a full cache rebuild when missing-period catch-up is enough.
- For backtest optimization requests, preserve the user's requested scheme count and strategy mode.
- For frontend issues, verify both API reachability and visible UI behavior.
