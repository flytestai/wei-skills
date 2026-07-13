---
name: three-digit-lottery-divination
description: Fetch a user-specified number of official China Sports Lottery 排列三 or China Welfare Lottery 福彩3D draws, validate and summarize three-digit history, and derive one deterministic entertainment-only next-issue number with a documented Plum Blossom numerology method. Use when users ask for recent or specified draw counts, official-interface history, position frequency or omission analysis, or next-draw 梅花易数推演 for 排列三, 福彩3D, or both games.
---

# Three-Digit Lottery Divination

Use the bundled script as the source of truth for fetching, validation, statistics, and derivation. Do not manually reconstruct API data or invent missing draws.

## Run The Workflow

Run from this skill directory:

```bash
python scripts/lottery_divination.py --game pl3 --count 100
python scripts/lottery_divination.py --game fc3d --count 100
python scripts/lottery_divination.py --game both --count 100
```

Map user terms as follows:

- `排列三`, `体彩排列三`, `pl3` -> `--game pl3`
- `福彩3D`, `福彩3d`, `fc3d` -> `--game fc3d`
- both games in one request -> `--game both`

Use the requested draw count. Default to `100` only when the user does not specify one. Add `--include-draws` only when the user asks to see or export every fetched draw.

## Verify Before Reporting

1. Require `fetched_count` to equal `requested_count`.
2. Report the official source, oldest and latest fetched issue, latest result, and expected next issue.
3. Treat `expected_next_issue` as a sequential estimate until the lottery operator publishes it.
4. Report the divination seeds, base and changed candidates, history scores, selection rule, and one selected direct-order number.
5. Never describe the selected number as certain, high-probability, official, or capable of improving the mathematical odds.

If an API, schema, or count validation fails, report the exact failure and stop. Do not fill gaps from memory, prior conversation data, or another website unless the user authorizes a fallback source.

## Format The Answer

For each game, include:

- data source and fetched range
- latest draw and expected next issue
- concise position-frequency and current-omission evidence relevant to the selected digits
- the numeric Plum Blossom derivation and candidate comparison
- exactly one selected three-digit direct-order number unless the user asks for more
- an entertainment-only notice and the `1/1000` direct-order probability

Keep 排列三 and 福彩3D results in separate labeled sections when processing both.

## Read The Method Reference

Read [references/method-and-apis.md](references/method-and-apis.md) when explaining the API mappings, checksum, trigram conversion, moving line, candidate scoring, or limitations.

## Boundaries

- Do not place bets, save tickets, purchase entries, or claim guaranteed returns.
- Do not interpret hot numbers, cold numbers, or omissions as evidence that a digit is due.
- Do not silently switch from official interfaces to cached or user-provided data.
- Preserve the script's deterministic result for the same game, draw count, and API snapshot.
