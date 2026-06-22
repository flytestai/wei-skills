# Saved Schemes

## Endpoints

- `GET /api/saved-schemes?limit=100`
- `POST /api/saved-schemes`
- `POST /api/saved-schemes/batch`
- `POST /api/saved-schemes/manual`
- `POST /api/saved-schemes/issues/{issue}/manual-result`
- `DELETE /api/saved-schemes/issues/{issue}/manual-result`
- `DELETE /api/saved-schemes/{saved_id}`
- `DELETE /api/saved-schemes/issues/{issue}`

## Workflow

1. Decide whether the source is generated, batch-generated, or manual.
2. Save through the matching endpoint.
3. For missing official results, upsert a manual draw result override.
4. Delete only when the user explicitly asks.

## Rules

- Preserve target issue exactly.
- Keep `multiple` and `is_additional` explicit when saving purchased tickets.
- Prefer batch save for multi-scheme runs.
