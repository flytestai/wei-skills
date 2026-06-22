# Live Divination

## Endpoint

`POST /api/divination`

## Request fields

- `issue` optional
- `timestamp`
- `scheme_count`
- `strategy_mode`
- `ai_config` optional

## Strategy modes

- `single_hit`: prioritize single-ticket strength
- `smart_balance`: auto-select between live short-window and long-window profiles
- `multi_cover`: prioritize at-least-one-hit coverage

## Output fields to surface

- `final_schemes`
- `should_observe`
- `decision_reason`
- `tuning_profile`
- `issue_confidence`
- `calibrated_confidence`
- `applied_threshold`
- `front_confidence`
- `front_gate`
- `back_confidence`
- `back_gate`

## Workflow

1. Read `/api/sync/status` to resolve `next_issue`.
2. Read `/api/full-history-cache/status` for the requested `scheme_count`.
3. If cache is invalid, rebuild or poll the active cache job first.
4. Call `/api/divination`.
5. Return both schemes and the live gate explanation.

## Important behavior

- `should_observe` is a risk signal, not a reason to hide `final_schemes`.
- Preserve the returned order of `final_schemes` in any copy/share output.
- If the user asks for current exact numbers, quote the returned groups directly instead of recomputing.
