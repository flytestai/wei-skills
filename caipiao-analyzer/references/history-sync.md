# History Sync and Analytics

## Endpoints

- `GET /api/sync/status`
- `POST /api/sync/run?full_refresh=false`
- `GET /api/history?limit=5000`
- `GET /api/analytics?limit=5000`

## Workflow

1. Read sync status first.
2. If the user wants a refresh, call sync.
3. Read history rows or analytics summary next.

## Report these fields when relevant

- latest issue
- next issue
- total history count
- last sync timestamp
- whether a refresh inserted or updated records

## Rules

- When the user says "latest" or "today", report exact issue ids and timestamps.
- Prefer incremental sync before suggesting unrelated rebuilds.
