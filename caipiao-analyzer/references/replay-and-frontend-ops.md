# Replay and Frontend Ops

## Default local URLs

- Frontend: `http://127.0.0.1:5180/`
- Backend: `http://127.0.0.1:8011/`
- Backend health: `/health`

## Replay endpoint

- `GET /api/divination-runs?limit=100`

## Workflow

1. Confirm backend health.
2. Confirm frontend reachability.
3. Reproduce the user flow in the browser.
4. Read replay logs or logged divination runs when history matters.
5. Verify visible UI state after any restart or code change.

## Common issue patterns

- frontend shows stale fetch errors right after backend restart
- cache blocks live divination with `409`
- copy/share behavior diverges from the visible scheme list
- UI says no schemes were generated even though the API returned groups

## Rules

- After backend restarts, refresh the frontend and retry once before declaring failure.
- When checking copy behavior, verify exact line formatting and scheme order.
