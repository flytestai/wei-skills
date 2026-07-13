#!/usr/bin/env python3
"""Fetch official three-digit lottery history and derive one deterministic number."""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Dict, Iterable, List, Sequence, Tuple


SHANGHAI_TZ = timezone(timedelta(hours=8))
POSITION_NAMES = ("hundreds", "tens", "units")
MAX_COUNT = 1000

PL3_ENDPOINT = (
    "https://webapi.sporttery.cn/gateway/lottery/"
    "getHistoryPageListV1.qry"
)
FC3D_ENDPOINT = (
    "https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/"
    "findDrawNotice"
)

GAME_CONFIG = {
    "pl3": {
        "display_name": "体育彩票排列三",
        "source_name": "中国体育彩票",
        "source_url": PL3_ENDPOINT,
        "year_prefix_width": 2,
    },
    "fc3d": {
        "display_name": "福彩3D",
        "source_name": "中国福利彩票",
        "source_url": FC3D_ENDPOINT,
        "year_prefix_width": 4,
    },
}

# Line tuples are ordered from bottom to top.
TRIGRAMS = {
    1: {"name": "乾", "lines": (1, 1, 1)},
    2: {"name": "兑", "lines": (1, 1, 0)},
    3: {"name": "离", "lines": (1, 0, 1)},
    4: {"name": "震", "lines": (1, 0, 0)},
    5: {"name": "巽", "lines": (0, 1, 1)},
    6: {"name": "坎", "lines": (0, 1, 0)},
    7: {"name": "艮", "lines": (0, 0, 1)},
    8: {"name": "坤", "lines": (0, 0, 0)},
}
LINES_TO_TRIGRAM = {
    value["lines"]: number for number, value in TRIGRAMS.items()
}


@dataclass(frozen=True)
class Draw:
    issue: str
    draw_date: str
    digits: Tuple[int, int, int]

    @property
    def number(self) -> str:
        return "".join(str(digit) for digit in self.digits)

    @property
    def numeric_value(self) -> int:
        return self.digits[0] * 100 + self.digits[1] * 10 + self.digits[2]

    def to_dict(self) -> Dict[str, object]:
        return {
            "issue": self.issue,
            "draw_date": self.draw_date,
            "number": self.number,
            "digits": list(self.digits),
        }


def _mod_index(value: int, modulus: int) -> int:
    remainder = value % modulus
    return modulus if remainder == 0 else remainder


def _extract_date(value: object) -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", str(value or ""))
    if not match:
        raise ValueError(f"invalid draw date: {value!r}")
    return match.group(0)


def _extract_digits(value: object) -> Tuple[int, int, int]:
    parts = re.findall(r"\d+", str(value or ""))
    if len(parts) != 3:
        raise ValueError(f"expected exactly three digits, got {value!r}")
    digits = tuple(int(part) for part in parts)
    if any(digit < 0 or digit > 9 for digit in digits):
        raise ValueError(f"digit outside 0-9: {value!r}")
    return digits  # type: ignore[return-value]


def _normalize_draw(issue: object, draw_date: object, result: object) -> Draw:
    normalized_issue = str(issue or "").strip()
    if not normalized_issue.isdigit():
        raise ValueError(f"invalid issue: {issue!r}")
    return Draw(
        issue=normalized_issue,
        draw_date=_extract_date(draw_date),
        digits=_extract_digits(result),
    )


def _request_json(
    endpoint: str,
    params: Dict[str, object],
    headers: Dict[str, str],
    timeout: float,
    retries: int = 3,
) -> Dict[str, object]:
    url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    context = ssl.create_default_context()
    last_error: Exception | None = None

    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(
                request, timeout=timeout, context=context
            ) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                body = response.read().decode(charset)
            payload = json.loads(body)
            if not isinstance(payload, dict):
                raise ValueError("API response is not a JSON object")
            return payload
        except (
            urllib.error.HTTPError,
            urllib.error.URLError,
            TimeoutError,
            UnicodeDecodeError,
            json.JSONDecodeError,
            ValueError,
        ) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(0.5 * attempt)

    raise RuntimeError(f"request failed after {retries} attempts: {last_error}")


def _dedupe_and_sort(draws: Iterable[Draw]) -> List[Draw]:
    by_issue: Dict[str, Draw] = {}
    for draw in draws:
        existing = by_issue.get(draw.issue)
        if existing and existing != draw:
            raise ValueError(f"conflicting API rows for issue {draw.issue}")
        by_issue[draw.issue] = draw
    return sorted(by_issue.values(), key=lambda draw: int(draw.issue), reverse=True)


def fetch_pl3(count: int, timeout: float = 30.0) -> List[Draw]:
    page_size = min(100, count)
    page_no = 1
    collected: List[Draw] = []
    seen = set()
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/136.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://static.sporttery.cn/",
    }

    while len(collected) < count:
        payload = _request_json(
            PL3_ENDPOINT,
            {
                "gameNo": "35",
                "provinceId": "0",
                "pageSize": page_size,
                "isVerify": "1",
                "pageNo": page_no,
            },
            headers,
            timeout,
        )
        if payload.get("success") is not True:
            raise RuntimeError(
                f"sporttery API error: {payload.get('errorMessage') or payload}"
            )
        value = payload.get("value")
        items = value.get("list") if isinstance(value, dict) else None
        if not isinstance(items, list) or not items:
            break

        before = len(collected)
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("sporttery API returned a non-object row")
            draw = _normalize_draw(
                item.get("lotteryDrawNum"),
                item.get("lotteryDrawTime"),
                item.get("lotteryDrawResult"),
            )
            if draw.issue not in seen:
                seen.add(draw.issue)
                collected.append(draw)
        if len(collected) == before:
            break
        page_no += 1

    draws = _dedupe_and_sort(collected)
    if len(draws) < count:
        raise RuntimeError(
            f"sporttery returned {len(draws)} unique draws; {count} requested"
        )
    return draws[:count]


def fetch_fc3d(count: int, timeout: float = 30.0) -> List[Draw]:
    page_size = min(100, count)
    page_no = 1
    collected: List[Draw] = []
    seen = set()
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/136.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.cwl.gov.cn/ygkj/wqkjgg/3d/",
    }

    while len(collected) < count:
        payload = _request_json(
            FC3D_ENDPOINT,
            {
                "name": "3d",
                "issueCount": count,
                "issueStart": "",
                "issueEnd": "",
                "dayStart": "",
                "dayEnd": "",
                "pageNo": page_no,
                "pageSize": page_size,
                "week": "",
                "systemType": "PC",
            },
            headers,
            timeout,
        )
        if str(payload.get("state")) != "0":
            raise RuntimeError(
                f"welfare lottery API error: {payload.get('message') or payload}"
            )
        items = payload.get("result")
        if not isinstance(items, list) or not items:
            break

        before = len(collected)
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("welfare lottery API returned a non-object row")
            draw = _normalize_draw(
                item.get("code"), item.get("date"), item.get("red")
            )
            if draw.issue not in seen:
                seen.add(draw.issue)
                collected.append(draw)
        if len(collected) == before:
            break
        page_no += 1

    draws = _dedupe_and_sort(collected)
    if len(draws) < count:
        raise RuntimeError(
            f"welfare lottery returned {len(draws)} unique draws; {count} requested"
        )
    return draws[:count]


def expected_next_issue(issue: str, year_prefix_width: int) -> str:
    expected_width = year_prefix_width + 3
    if len(issue) != expected_width or not issue.isdigit():
        raise ValueError(
            f"issue {issue!r} does not match expected width {expected_width}"
        )
    prefix = issue[:year_prefix_width]
    sequence = int(issue[year_prefix_width:]) + 1
    if sequence <= 999:
        return f"{prefix}{sequence:03d}"
    next_year = int(prefix) + 1
    return f"{next_year:0{year_prefix_width}d}001"


def analyze_draws(draws: Sequence[Draw]) -> Tuple[Dict[str, object], List[List[int]], List[List[int]]]:
    if not draws:
        raise ValueError("at least one draw is required")

    counts = [[0] * 10 for _ in range(3)]
    omissions = [[0] * 10 for _ in range(3)]
    sum_counter: Counter[int] = Counter()
    form_counter: Counter[str] = Counter()

    for draw in draws:
        for position, digit in enumerate(draw.digits):
            counts[position][digit] += 1
        sum_counter[sum(draw.digits)] += 1
        distinct = len(set(draw.digits))
        form_counter[
            "triple" if distinct == 1 else "pair" if distinct == 2 else "all_distinct"
        ] += 1

    for position in range(3):
        for digit in range(10):
            omission = 0
            for draw in draws:
                if draw.digits[position] == digit:
                    break
                omission += 1
            omissions[position][digit] = omission

    summary: Dict[str, object] = {
        "position_frequency": {
            POSITION_NAMES[position]: {
                str(digit): counts[position][digit] for digit in range(10)
            }
            for position in range(3)
        },
        "current_omission": {
            POSITION_NAMES[position]: {
                str(digit): omissions[position][digit] for digit in range(10)
            }
            for position in range(3)
        },
        "top_sums": [
            {"sum": value, "count": count}
            for value, count in sorted(
                sum_counter.items(), key=lambda item: (-item[1], item[0])
            )[:10]
        ],
        "forms": {
            name: form_counter.get(name, 0)
            for name in ("all_distinct", "pair", "triple")
        },
    }
    return summary, counts, omissions


def changed_trigrams(upper: int, lower: int, moving_line: int) -> Tuple[int, int]:
    if upper not in TRIGRAMS or lower not in TRIGRAMS:
        raise ValueError("trigram number must be in 1-8")
    if moving_line < 1 or moving_line > 6:
        raise ValueError("moving line must be in 1-6")

    lower_lines = list(TRIGRAMS[lower]["lines"])
    upper_lines = list(TRIGRAMS[upper]["lines"])
    if moving_line <= 3:
        lower_lines[moving_line - 1] ^= 1
    else:
        upper_lines[moving_line - 4] ^= 1

    return (
        LINES_TO_TRIGRAM[tuple(upper_lines)],
        LINES_TO_TRIGRAM[tuple(lower_lines)],
    )


def _candidate_score(
    digits: Sequence[int], counts: Sequence[Sequence[int]], omissions: Sequence[Sequence[int]]
) -> Dict[str, int]:
    frequency_score = sum(counts[position][digit] for position, digit in enumerate(digits))
    omission_score = sum(
        omissions[position][digit] for position, digit in enumerate(digits)
    )
    return {
        "frequency_score": frequency_score,
        "omission_score": omission_score,
    }


def derive_number(
    draws: Sequence[Draw],
    next_issue: str,
    counts: Sequence[Sequence[int]],
    omissions: Sequence[Sequence[int]],
) -> Dict[str, object]:
    history_seed = sum(
        index * draw.numeric_value
        for index, draw in enumerate(reversed(draws), start=1)
    )
    issue_seed = int(next_issue)
    upper = _mod_index(issue_seed, 8)
    lower = _mod_index(history_seed, 8)
    moving_line = _mod_index(issue_seed + history_seed, 6)
    changed_upper, changed_lower = changed_trigrams(upper, lower, moving_line)

    base_digits = (upper, lower, moving_line)
    changed_digits = (changed_upper, changed_lower, moving_line)
    base_score = _candidate_score(base_digits, counts, omissions)
    changed_score = _candidate_score(changed_digits, counts, omissions)

    base_rank = (base_score["frequency_score"], base_score["omission_score"])
    changed_rank = (
        changed_score["frequency_score"],
        changed_score["omission_score"],
    )
    use_changed = changed_rank > base_rank
    selected_digits = changed_digits if use_changed else base_digits

    def trigram(number: int) -> Dict[str, object]:
        return {
            "number": number,
            "name": TRIGRAMS[number]["name"],
            "lines_bottom_to_top": list(TRIGRAMS[number]["lines"]),
        }

    return {
        "method": "numeric Plum Blossom with recency-weighted history seed",
        "issue_seed": issue_seed,
        "history_seed": history_seed,
        "upper_trigram": trigram(upper),
        "lower_trigram": trigram(lower),
        "moving_line": moving_line,
        "changed_upper_trigram": trigram(changed_upper),
        "changed_lower_trigram": trigram(changed_lower),
        "base_candidate": "".join(str(digit) for digit in base_digits),
        "changed_candidate": "".join(str(digit) for digit in changed_digits),
        "candidate_scores": {
            "base": base_score,
            "changed": changed_score,
        },
        "selection_rule": (
            "higher exact-position frequency score; current omission breaks ties; "
            "base candidate wins a complete tie"
        ),
        "selected_candidate_type": "changed" if use_changed else "base",
        "selected_number": "".join(str(digit) for digit in selected_digits),
    }


def build_result(
    game: str,
    count: int,
    timeout: float,
    include_draws: bool,
) -> Dict[str, object]:
    config = GAME_CONFIG[game]
    fetcher = fetch_pl3 if game == "pl3" else fetch_fc3d
    draws = fetcher(count=count, timeout=timeout)
    if len(draws) != count:
        raise RuntimeError(f"fetched {len(draws)} draws; expected exactly {count}")

    next_issue = expected_next_issue(
        draws[0].issue, int(config["year_prefix_width"])
    )
    statistics, counts, omissions = analyze_draws(draws)
    divination = derive_number(draws, next_issue, counts, omissions)
    result: Dict[str, object] = {
        "game": game,
        "game_name": config["display_name"],
        "source": {
            "name": config["source_name"],
            "url": config["source_url"],
        },
        "requested_count": count,
        "fetched_count": len(draws),
        "oldest": draws[-1].to_dict(),
        "latest": draws[0].to_dict(),
        "expected_next_issue": next_issue,
        "statistics": statistics,
        "divination": divination,
        "notices": [
            "The next issue is a sequential estimate until the operator publishes it.",
            "This deterministic derivation is for entertainment only and does not improve odds.",
            "A direct-order three-digit entry has theoretical probability 1/1000.",
        ],
    }
    if include_draws:
        result["draws_newest_first"] = [draw.to_dict() for draw in draws]
    return result


def _count_value(value: str) -> int:
    try:
        count = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("count must be an integer") from exc
    if count < 1 or count > MAX_COUNT:
        raise argparse.ArgumentTypeError(f"count must be between 1 and {MAX_COUNT}")
    return count


def _text_output(payload: Dict[str, object]) -> str:
    lines = []
    for result in payload["results"]:  # type: ignore[index]
        game = result["game_name"]
        oldest = result["oldest"]
        latest = result["latest"]
        divination = result["divination"]
        lines.extend(
            [
                f"[{game}]",
                (
                    f"Fetched {result['fetched_count']}/{result['requested_count']} draws: "
                    f"{oldest['issue']} {oldest['number']} -> "
                    f"{latest['issue']} {latest['number']}"
                ),
                f"Expected next issue: {result['expected_next_issue']}",
                (
                    f"Base {divination['base_candidate']} vs changed "
                    f"{divination['changed_candidate']} -> "
                    f"{divination['selected_number']}"
                ),
                "Entertainment only; direct-order probability is 1/1000.",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch official 排列三/福彩3D history and derive one deterministic "
            "entertainment-only next-issue number."
        )
    )
    parser.add_argument(
        "--game", choices=("pl3", "fc3d", "both"), required=True
    )
    parser.add_argument("--count", type=_count_value, default=100)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--include-draws", action="store_true")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.timeout <= 0:
        print("error: timeout must be positive", file=sys.stderr)
        return 2

    games = ("pl3", "fc3d") if args.game == "both" else (args.game,)
    try:
        results = [
            build_result(game, args.count, args.timeout, args.include_draws)
            for game in games
        ]
    except (RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    payload: Dict[str, object] = {
        "generated_at": datetime.now(SHANGHAI_TZ).isoformat(timespec="seconds"),
        "results": results,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(_text_output(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
