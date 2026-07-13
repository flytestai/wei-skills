# Method And Official APIs

## Official Sources

| Game | Operator | Endpoint | Result fields |
|---|---|---|---|
| 排列三 (`pl3`) | 中国体育彩票 | `https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry` with `gameNo=35` | `lotteryDrawNum`, `lotteryDrawTime`, `lotteryDrawResult` |
| 福彩3D (`fc3d`) | 中国福利彩票 | `https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice` with `name=3d` | `code`, `date`, `red` |

Fetch pages of at most 100 rows. Deduplicate by issue, sort newest first, and require exactly the requested count. Accept only results containing exactly three digits in the range `0-9`.

## Expected Next Issue

Increment the latest issue's final three-digit sequence. Preserve the game-specific year prefix: two digits for 排列三 and four digits for 福彩3D. Treat this as an estimate because holidays and operator scheduling remain authoritative.

## Numeric Plum Blossom Derivation

This skill uses a deterministic number-seed method so the specified history directly affects the result.

1. Let `A` be the numeric expected-next issue.
2. Order the fetched draws from oldest to newest. Convert each result to its numeric value `V_i = 100H + 10T + U`.
3. Compute the recency-weighted history seed:

   `B = sum(i * V_i for i = 1..N)`

   The newest draw has weight `N`; every requested draw contributes.
4. Compute the upper trigram as `A mod 8`, mapping zero to `8`.
5. Compute the lower trigram as `B mod 8`, mapping zero to `8`.
6. Compute the moving line as `(A + B) mod 6`, mapping zero to `6`.

Use the standard trigram numbers:

| Number | Trigram | Bottom-to-top lines |
|---:|---|---|
| 1 | 乾 | yang, yang, yang |
| 2 | 兑 | yang, yang, yin |
| 3 | 离 | yang, yin, yang |
| 4 | 震 | yang, yin, yin |
| 5 | 巽 | yin, yang, yang |
| 6 | 坎 | yin, yang, yin |
| 7 | 艮 | yin, yin, yang |
| 8 | 坤 | yin, yin, yin |

The base candidate is `upper + lower + moving-line`. Toggle the moving line to obtain the changed hexagram; the changed candidate is `changed-upper + changed-lower + moving-line`.

## History-Weighted Selection

Score both candidates against the fetched sample:

- `frequency_score`: sum of each candidate digit's occurrence count at its exact position.
- `omission_score`: sum of each candidate digit's current omission at its exact position.

Select the higher `frequency_score`; use `omission_score` only as a tie-breaker. If both tie, keep the base candidate. This is a deterministic selection convention, not a probability model.

## Statistical Limits

排列三 and 福彩3D are independent random three-digit draws. Every direct-order number has theoretical probability `1/1000` per draw. Historical frequency, omission, numerology, and checksum choices do not establish a predictive advantage. Present the result only as entertainment-oriented derivation.
