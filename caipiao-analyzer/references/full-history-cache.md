# Full-History Cache

## Endpoints

- `GET /api/full-history-cache/status?scheme_count=3&ticket_mode=basic`
- `POST /api/full-history-cache/rebuild?scheme_count=3&ticket_mode=basic&force=false`
- `GET /api/full-history-cache/jobs/{job_id}`

## Workflow

1. Read status.
2. If already valid, do not rebuild.
3. If stale or incomplete, start a rebuild job.
4. Poll the job until completion.
5. Prefer missing-period extension instead of destructive full regeneration.

## Explain progress using

- latest official issue
- latest cached issue
- replayable issue count
- finished profile count
- active job state

## Important behavior

- Cache is persistent.
- Live divination may return `409` if the cache is stale enough to block analysis.
- Always respect the requested `scheme_count` and `ticket_mode`.
