#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import random
import re
import sys
import urllib.parse
import urllib.request
import ssl
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
RECORDS_PATH = ROOT / "records.md"
STATE_PATH = ROOT / "state.md"
BETS_PATH = ROOT / "bets.md"
DRAW_RESULTS_PATH = ROOT / "draw_results.md"

FRONT_MIN, FRONT_MAX, FRONT_COUNT = 1, 35, 5
BACK_MIN, BACK_MAX, BACK_COUNT = 1, 12, 2


def setup_console_encoding() -> None:
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def fmt_num(n: int) -> str:
    return f"{n:02d}"


def normalize_group(front: List[int], back: List[int]) -> Tuple[List[int], List[int]]:
    if len(front) != FRONT_COUNT:
        raise ValueError(f"前区号码数量应为 {FRONT_COUNT} 个，实际为 {len(front)} 个")
    if len(back) != BACK_COUNT:
        raise ValueError(f"后区号码数量应为 {BACK_COUNT} 个，实际为 {len(back)} 个")
    if len(set(front)) != len(front):
        raise ValueError("前区存在重复号码")
    if len(set(back)) != len(back):
        raise ValueError("后区存在重复号码")
    for n in front:
        if not (FRONT_MIN <= n <= FRONT_MAX):
            raise ValueError(f"前区号码 {n} 超出范围 01-35")
    for n in back:
        if not (BACK_MIN <= n <= BACK_MAX):
            raise ValueError(f"后区号码 {n} 超出范围 01-12")
    return sorted(front), sorted(back)


def format_group(front: List[int], back: List[int]) -> str:
    return f"前区：{' '.join(fmt_num(n) for n in sorted(front))} 后区：{' '.join(fmt_num(n) for n in sorted(back))}"


def parse_number_blob(text: str) -> List[int]:
    return [int(x) for x in re.findall(r"\d{1,2}", text)]


def parse_groups(raw: str) -> Tuple[List[Tuple[List[int], List[int]]], List[str]]:
    text = raw.replace("\r\n", "\n").replace("，", ",").replace("：", ":")
    pattern = re.compile(r"前区\s*:?\s*(.*?)\s*后区\s*:?\s*(.*?)(?=(?:\n\s*\n)|(?:\n\s*前区)|\Z)", re.S)
    groups, errors = [], []
    matches = list(pattern.finditer(text))
    if not matches:
        return [], ["未识别到有效的‘前区/后区’号码组"]
    for idx, m in enumerate(matches, start=1):
        try:
            front = parse_number_blob(m.group(1))
            back = parse_number_blob(m.group(2))
            groups.append(normalize_group(front, back))
        except Exception as e:
            errors.append(f"第 {idx} 组解析失败：{e}")
    return groups, errors


def ensure_files() -> None:
    if not RECORDS_PATH.exists():
        RECORDS_PATH.write_text("# 大乐透历史号码记录\n\n## Records\n", encoding="utf-8")
    if not STATE_PATH.exists():
        STATE_PATH.write_text("# 大乐透统计状态\n\nversion: 1\nrecord_count: 0\nlast_added_count: 0\nlast_generated_count: 0\nlast_tracked_issue: \nlast_checked_issue: \nlast_front_stats_top:\nlast_back_stats_top:\nlast_generated:\n", encoding="utf-8")
    if not BETS_PATH.exists():
        BETS_PATH.write_text("# 大乐透已保存投注方案\n", encoding="utf-8")
    if not DRAW_RESULTS_PATH.exists():
        DRAW_RESULTS_PATH.write_text("# 大乐透开奖与核对结果\n", encoding="utf-8")


def load_record_lines() -> List[str]:
    ensure_files()
    return [line[2:].strip() for line in RECORDS_PATH.read_text(encoding="utf-8").splitlines() if line.startswith("- ")]


def load_records() -> List[Tuple[List[int], List[int]]]:
    records = []
    for line in load_record_lines():
        m = re.match(r"前区[:：](.*?)后区[:：](.*)$", line)
        if not m:
            continue
        front = [int(x) for x in re.findall(r"\d{2}", m.group(1))]
        back = [int(x) for x in re.findall(r"\d{2}", m.group(2))]
        if len(front) == 5 and len(back) == 2:
            records.append((front, back))
    return records


def append_records(groups: List[Tuple[List[int], List[int]]]) -> None:
    ensure_files()
    with RECORDS_PATH.open("a", encoding="utf-8") as f:
        for front, back in groups:
            f.write(f"- {format_group(front, back)}\n")


def compute_stats(records: List[Tuple[List[int], List[int]]]) -> Tuple[Counter, Counter]:
    front_counter, back_counter = Counter(), Counter()
    for front, back in records:
        front_counter.update(front)
        back_counter.update(back)
    return front_counter, back_counter


def top_items(counter: Counter, limit: int) -> List[str]:
    items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:limit]
    return [f"{fmt_num(k)}: {v}" for k, v in items]


def render_stats(counter: Counter, start: int, end: int) -> List[str]:
    items = [(n, counter.get(n, 0)) for n in range(start, end + 1) if counter.get(n, 0) > 0]
    items.sort(key=lambda x: (-x[1], x[0]))
    return [f"{fmt_num(n)}({cnt}次)" for n, cnt in items]


def split_frequency_layers(counter: Counter, start: int, end: int) -> Dict[str, List[int]]:
    items = [(n, counter.get(n, 0)) for n in range(start, end + 1) if counter.get(n, 0) > 0]
    items.sort(key=lambda x: (-x[1], x[0]))
    nums = [n for n, _ in items]
    total = len(nums)
    if total == 0:
        return {"high": [], "mid": [], "low": []}
    high_end = max(1, round(total * 0.3))
    mid_end = min(total, high_end + max(1, round(total * 0.4)))
    return {"high": nums[:high_end], "mid": nums[high_end:mid_end], "low": nums[mid_end:]}


def weighted_pick(candidates: List[int], counter: Counter, used: set, k: int, boost_top: int = 0) -> List[int]:
    picked = []
    available = [n for n in candidates if n not in used]
    while len(picked) < k and available:
        weighted = []
        for n in available:
            w = counter.get(n, 0) + 1
            if boost_top and n in candidates[:boost_top]:
                w += 1
            weighted.extend([n] * max(w, 1))
        choice = random.choice(weighted)
        picked.append(choice)
        used.add(choice)
        available = [n for n in candidates if n not in used]
    return sorted(picked)


def generate_groups(records: List[Tuple[List[int], List[int]]], count: int, seed: int = 42) -> List[str]:
    random.seed(seed)
    front_counter, back_counter = compute_stats(records)
    front_rank = [n for n, _ in sorted(front_counter.items(), key=lambda x: (-x[1], x[0]))]
    back_rank = [n for n, _ in sorted(back_counter.items(), key=lambda x: (-x[1], x[0]))]
    for n in range(1, 36):
        if n not in front_rank:
            front_rank.append(n)
    for n in range(1, 13):
        if n not in back_rank:
            back_rank.append(n)
    top_front, mid_front, low_front = front_rank[:10], front_rank[10:22], front_rank[22:]
    top_back, mid_back, low_back = back_rank[:5], back_rank[5:9], back_rank[9:]
    strategies = [(3, 2, 0), (2, 2, 1), (2, 3, 0), (3, 1, 1), (1, 3, 1)]
    seen, results = set(), []
    attempts = 0
    while len(results) < count and attempts < count * 50:
        attempts += 1
        hf, mf, lf = strategies[len(results) % len(strategies)]
        used = set()
        front = []
        front += weighted_pick(top_front, front_counter, used, hf, boost_top=5)
        front += weighted_pick(mid_front, front_counter, used, mf)
        front += weighted_pick(low_front, front_counter, used, lf)
        if len(front) < 5:
            front += weighted_pick(front_rank, front_counter, used, 5 - len(front))
        front = sorted(front[:5])
        used_back = set()
        if len(results) % 3 == 0:
            back = weighted_pick(top_back, back_counter, used_back, 2, boost_top=3)
        elif len(results) % 3 == 1:
            back = weighted_pick(top_back, back_counter, used_back, 1, boost_top=3) + weighted_pick(mid_back or top_back, back_counter, used_back, 1)
        else:
            back = weighted_pick(mid_back or top_back, back_counter, used_back, 1) + weighted_pick(low_back or top_back, back_counter, used_back, 1)
        if len(back) < 2:
            back += weighted_pick(back_rank, back_counter, used_back, 2 - len(back))
        back = sorted(back[:2])
        group = format_group(front, back)
        if group not in seen:
            seen.add(group)
            results.append(group)
    return results


def write_state(record_count: int, last_added_count: int, last_generated: List[str], front_counter: Counter, back_counter: Counter, last_tracked_issue: str = "", last_checked_issue: str = "") -> None:
    lines = [
        "# 大乐透统计状态",
        "",
        "version: 1",
        f"record_count: {record_count}",
        f"last_added_count: {last_added_count}",
        f"last_generated_count: {len(last_generated)}",
        f"last_tracked_issue: {last_tracked_issue}",
        f"last_checked_issue: {last_checked_issue}",
        "last_front_stats_top:",
    ]
    for item in top_items(front_counter, 10):
        lines.append(f"  - {item}")
    lines.append("last_back_stats_top:")
    for item in top_items(back_counter, 10):
        lines.append(f"  - {item}")
    lines.append("last_generated:")
    for item in last_generated:
        lines.append(f"  - {item}")
    STATE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_saved_bets(issue: str, multiple: int, groups: List[str], bet_type: str = "普通") -> None:
    ensure_files()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = ["", f"## Issue: {issue}", f"- 保存时间：{ts}"]
    for g in groups:
        lines.append(f"- 类型：{bet_type}")
        lines.append(f"- 倍数：{multiple}")
        lines.append(f"- {g}")
    with BETS_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def parse_saved_bets(issue: str) -> List[Dict[str, object]]:
    ensure_files()
    text = BETS_PATH.read_text(encoding="utf-8")
    pattern = re.compile(rf"## Issue: {re.escape(issue)}\n(.*?)(?=\n## Issue: |\Z)", re.S)
    m = pattern.search(text)
    if not m:
        return []
    block = m.group(1)
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    bets = []
    current_multiple = 1
    current_type = '普通'
    for line in lines:
        if line.startswith("- 类型："):
            current_type = line.split("：", 1)[1].strip() or '普通'
        elif line.startswith("- 倍数："):
            current_multiple = int(re.findall(r"\d+", line)[0])
        elif line.startswith("- 前区："):
            bet_text = line[2:].strip()
            mm = re.match(r"前区[:：](.*?)后区[:：](.*)$", bet_text)
            if mm:
                front = [int(x) for x in re.findall(r"\d{2}", mm.group(1))]
                back = [int(x) for x in re.findall(r"\d{2}", mm.group(2))]
                bets.append({"issue": issue, "multiple": current_multiple, "bet_type": current_type, "front": front, "back": back, "text": bet_text})
    return bets


def fetch_issue_stub() -> Dict[str, str]:
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'
    params = {
        'gameNo': '85',
        'provinceId': '0',
        'pageSize': '30',
        'isVerify': '1',
        'termLimits': '0',
        'pageNo': '1',
    }
    url = base_url + '?' + urllib.parse.urlencode(params)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Referer': 'https://static.sporttery.cn/res_1_0/jcw/default/html/kj/dlt.html?url=//www.lottery.gov.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://static.sporttery.cn',
    }
    req = urllib.request.Request(url, headers=headers)
    payload = json.loads(urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore'))
    value = payload.get('value') or {}
    last_draw = value.get('lastPoolDraw') or {}
    latest_issue = str(last_draw.get('lotteryDrawNum') or '').strip() or '[未获取到]'
    draw_date = str(last_draw.get('lotteryDrawTime') or '').strip() or '[未获取到]'
    next_issue = '[待确认规则后计算]'
    if latest_issue.isdigit() and len(latest_issue) >= 5:
        yy = int(latest_issue[:2])
        seq = int(latest_issue[2:])
        if seq < 999:
            next_issue = f'{yy:02d}{seq + 1:03d}'
    return {
        'latest_issue': latest_issue,
        'next_issue': next_issue,
        'draw_date': draw_date,
        'source': base_url,
    }


def fetch_draw_by_issue(issue: str) -> Dict[str, object]:
    ssl._create_default_https_context = ssl._create_unverified_context
    base_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'
    params = {
        'gameNo': '85',
        'provinceId': '0',
        'pageSize': '5',
        'isVerify': '1',
        'termLimits': '0',
        'pageNo': '1',
        'startTerm': issue,
        'endTerm': issue,
    }
    url = base_url + '?' + urllib.parse.urlencode(params)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Referer': 'https://static.sporttery.cn/res_1_0/jcw/default/html/kj/dlt.html?url=//www.lottery.gov.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://static.sporttery.cn',
    }
    req = urllib.request.Request(url, headers=headers)
    payload = json.loads(urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore'))
    value = payload.get('value') or {}
    last_draw = value.get('lastPoolDraw') or {}
    draw_issue = str(last_draw.get('lotteryDrawNum') or '').strip()
    draw_result = str(last_draw.get('lotteryDrawResult') or '').strip()
    draw_time = str(last_draw.get('lotteryDrawTime') or '').strip()
    if not draw_issue or draw_issue != issue or not draw_result:
        raise ValueError(f'未查到期号 {issue} 的开奖结果')
    nums = [int(x) for x in re.findall(r'\d{2}', draw_result)]
    if len(nums) != 7:
        raise ValueError(f'期号 {issue} 的开奖号码格式异常：{draw_result}')
    front, back = nums[:5], nums[5:]
    prize_levels = last_draw.get('prizeLevelList') or []
    return {
        'issue': draw_issue,
        'draw_time': draw_time,
        'front': front,
        'back': back,
        'draw_text': format_group(front, back),
        'prize_levels': prize_levels,
        'source': base_url,
    }


def prize_level_by_hits(front_hits: int, back_hits: int) -> str:
    mapping = {
        (5, 2): "一等奖", (5, 1): "二等奖", (5, 0): "三等奖", (4, 2): "四等奖",
        (4, 1): "五等奖", (3, 2): "五等奖", (4, 0): "六等奖", (3, 1): "六等奖",
        (2, 2): "六等奖", (3, 0): "七等奖", (2, 1): "七等奖", (1, 2): "八等奖",
        (2, 0): "八等奖", (0, 2): "九等奖", (1, 1): "九等奖", (0, 1): "九等奖",
    }
    return mapping.get((front_hits, back_hits), "未中奖")


def build_prize_amount_map(prize_levels: List[Dict[str, object]]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in prize_levels:
        sort_val = str(item.get('sort') or '')
        amount_text = str(item.get('stakeAmountFormat') or item.get('stakeAmount') or '').replace(',', '').strip()
        if not sort_val or not amount_text.isdigit():
            continue
        if len(sort_val) >= 1:
            level_num = sort_val[0]
            mapping = {
                '1': '一等奖', '2': '一等奖_追加',
                '3': '二等奖', '4': '二等奖_追加',
                '5': '三等奖',
                '6': '四等奖',
                '7': '五等奖',
                '8': '六等奖',
                '9': '七等奖',
            }
            level_name = mapping.get(level_num)
            if level_name and level_name not in result:
                result[level_name] = int(amount_text)
    fixed_map = {
        '八等奖': 15,
        '九等奖': 5,
    }
    result.update({k: v for k, v in fixed_map.items() if k not in result})
    return result


def compute_bonus(level: str, multiple: int, bet_type: str, prize_amount_map: Dict[str, int]) -> Tuple[int, str, bool]:
    if level == '未中奖':
        return 0, '未中奖', False
    if level in ('一等奖', '二等奖'):
        base_amount = prize_amount_map.get(level)
        append_amount = prize_amount_map.get(f'{level}_追加', 0) if bet_type == '追加' else 0
        if base_amount is None:
            return 0, '浮动奖或金额待官方公告确认', True
        total_single = base_amount + append_amount
        total_bonus = total_single * multiple
        if append_amount > 0:
            return total_bonus, f'单注基础{base_amount}元 + 追加{append_amount}元，合计{total_bonus}元', False
        return total_bonus, f'单注{base_amount}元，合计{total_bonus}元', False
    amount = prize_amount_map.get(level)
    if amount is None:
        return 0, '浮动奖或金额待官方公告确认', True
    total_bonus = amount * multiple
    return total_bonus, f'单注{amount}元，合计{total_bonus}元', False


def append_draw_check_result(issue: str, draw_text: str, lines_out: List[str], summary: List[str] = None) -> None:
    ensure_files()
    block = ["", f"## Issue: {issue}", f"- 开奖号码：{draw_text}"]
    if summary:
        block.extend([f"- {line}" for line in summary])
    block.extend([f"- {line}" for line in lines_out])
    with DRAW_RESULTS_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(block) + "\n")


def cmd_add(args) -> int:
    raw = Path(args.input).read_text(encoding="utf-8") if args.input else args.text
    groups, errors = parse_groups(raw)
    if groups:
        append_records(groups)
    records = load_records()
    front_counter, back_counter = compute_stats(records)
    write_state(len(records), len(groups), [], front_counter, back_counter)
    print(f"已新增 {len(groups)} 组，当前累计 {len(records)} 组。")
    for front, back in groups:
        print(format_group(front, back))
    for e in errors:
        print(f"- {e}")
    return 0


def cmd_stats(args) -> int:
    records = load_records()
    front_counter, back_counter = compute_stats(records)
    write_state(len(records), 0, [], front_counter, back_counter)
    print(f"累计记录：{len(records)} 组")
    front_top = "、".join([f"{fmt_num(k)}({v}次)" for k, v in sorted(front_counter.items(), key=lambda x: (-x[1], x[0]))[:args.top]])
    back_top = "、".join([f"{fmt_num(k)}({v}次)" for k, v in sorted(back_counter.items(), key=lambda x: (-x[1], x[0]))[:args.top]])
    print(f"前区高频号码：{front_top}")
    print(f"后区高频号码：{back_top}")
    if args.full:
        print("前区完整频次：")
        print("、".join(render_stats(front_counter, 1, 35)))
        print("后区完整频次：")
        print("、".join(render_stats(back_counter, 1, 12)))
        front_layers = split_frequency_layers(front_counter, 1, 35)
        back_layers = split_frequency_layers(back_counter, 1, 12)
        print("前区高频：" + " ".join(fmt_num(x) for x in front_layers["high"]))
        print("前区中频：" + " ".join(fmt_num(x) for x in front_layers["mid"]))
        print("前区低频：" + " ".join(fmt_num(x) for x in front_layers["low"]))
        print("后区高频：" + " ".join(fmt_num(x) for x in back_layers["high"]))
        print("后区中频：" + " ".join(fmt_num(x) for x in back_layers["mid"]))
        print("后区低频：" + " ".join(fmt_num(x) for x in back_layers["low"]))
    return 0


def cmd_generate(args) -> int:
    records = load_records()
    if not records:
        print("当前还没有历史记录，无法生成组合。")
        return 1
    front_counter, back_counter = compute_stats(records)
    results = generate_groups(records, args.count, seed=args.seed)
    write_state(len(records), 0, results, front_counter, back_counter)
    if not args.only:
        print("以下组合仅基于你提供号码的频次统计做重组参考，不代表实际预测结果。")
    for item in results:
        print(item)
    return 0


def cmd_fetch_issue(args) -> int:
    try:
        info = fetch_issue_stub()
    except Exception as e:
        print(f"查询失败：{e}")
        return 1
    records = load_records()
    front_counter, back_counter = compute_stats(records)
    write_state(len(records), 0, [], front_counter, back_counter, last_tracked_issue=info["next_issue"])
    print("下期信息查询结果：")
    print(f"最新已开奖期号：{info['latest_issue']}")
    print(f"下一期期号：{info['next_issue']}")
    print(f"开奖日期：{info['draw_date']}")
    print(f"数据源：{info['source']}")
    print("说明：当前已接入体彩前端真实公开接口；下一期期号暂按最新期号顺延 1 期推算，正式期号仍建议以官方实际公布为准。")
    return 0


def cmd_save_bets(args) -> int:
    raw = Path(args.input).read_text(encoding="utf-8") if args.input else args.text
    groups, errors = parse_groups(raw)
    lines = [format_group(front, back) for front, back in groups]
    bet_type = '追加' if args.append_mode else '普通'
    if lines:
        append_saved_bets(args.issue, args.multiple, lines, bet_type=bet_type)
    print(f"已保存 {len(lines)} 组到期号 {args.issue}，每注 {args.multiple} 倍，类型：{bet_type}。")
    for line in lines:
        print(line)
    for e in errors:
        print(f"- {e}")
    return 0


def cmd_check_draw(args) -> int:
    if args.draw:
        draw_groups, errors = parse_groups(args.draw)
        if not draw_groups:
            print("未能解析开奖号码。")
            for e in errors:
                print(f"- {e}")
            return 1
        draw_front, draw_back = draw_groups[0]
        draw_issue = args.issue
        draw_text = format_group(draw_front, draw_back)
        draw_source = 'manual'
        draw_time = ''
    else:
        try:
            draw_info = fetch_draw_by_issue(args.issue)
        except Exception as e:
            print(f"获取期开奖结果失败：{e}")
            return 1
        draw_front = draw_info['front']
        draw_back = draw_info['back']
        draw_issue = draw_info['issue']
        draw_text = draw_info['draw_text']
        draw_source = draw_info['source']
        draw_time = str(draw_info.get('draw_time') or '')
    bets = parse_saved_bets(args.issue)
    if not bets:
        print(f"未找到期号 {args.issue} 的已保存投注。")
        return 1
    prize_amount_map = build_prize_amount_map(draw_info.get('prize_levels', []) if not args.draw else [])
    outputs = []
    total_confirmed_bonus = 0
    has_dynamic_bonus_level = False
    hit_count = 0
    for idx, bet in enumerate(bets, start=1):
        front_hits = len(set(bet["front"]) & set(draw_front))
        back_hits = len(set(bet["back"]) & set(draw_back))
        level = prize_level_by_hits(front_hits, back_hits)
        multiple = int(bet['multiple'])
        bet_type = str(bet.get('bet_type') or '普通')
        line_bonus, bonus_text, need_official = compute_bonus(level, multiple, bet_type, prize_amount_map)
        if level != '未中奖':
            hit_count += 1
        if line_bonus > 0:
            total_confirmed_bonus += line_bonus
        if need_official:
            has_dynamic_bonus_level = True
        outputs.append(f"第{idx}组：{bet['text']} | 类型：{bet_type} | 命中：前区{front_hits}个，后区{back_hits}个 | 结果：{level} | 倍数：{multiple}倍 | 奖金：{bonus_text}")
    summary_lines = [
        f"数据源：{draw_source}",
        f"中奖注数：{hit_count}/{len(bets)}",
        f"当前可精确汇总奖金：{total_confirmed_bonus}元",
    ]
    if has_dynamic_bonus_level:
        summary_lines.append("存在浮动奖或追加/派奖待确认项")
    append_draw_check_result(draw_issue, draw_text, outputs, summary=summary_lines)
    records = load_records()
    front_counter, back_counter = compute_stats(records)
    write_state(len(records), 0, [], front_counter, back_counter, last_checked_issue=draw_issue)
    print(f"开奖期号：{draw_issue}")
    if draw_time:
        print(f"开奖日期：{draw_time}")
    print(f"开奖号码：{draw_text}")
    print(f"数据源：{draw_source}")
    for line in outputs:
        print(line)
    print(f"中奖注数：{hit_count}/{len(bets)}")
    print(f"当前可精确汇总奖金：{total_confirmed_bonus}元")
    if has_dynamic_bonus_level:
        print("说明：涉及浮动奖、追加奖或派奖时，当前仅保守汇总可精确部分，最终金额仍应以官方公告为准。")
    else:
        print("说明：当前奖金按官方返回单注金额 × 倍数计算；若涉及派奖或特殊规则，仍应以官方公告为准。")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="大乐透号码记录、统计、保存投注、开奖核对")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="新增号码组")
    p_add.add_argument("--text", help="原始号码文本")
    p_add.add_argument("--input", help="从文件读取原始号码文本")
    p_add.set_defaults(func=cmd_add)

    p_stats = sub.add_parser("stats", help="统计频次")
    p_stats.add_argument("--top", type=int, default=10, help="展示前后区 Top N")
    p_stats.add_argument("--full", action="store_true", help="输出完整频次与分层")
    p_stats.set_defaults(func=cmd_stats)

    p_gen = sub.add_parser("generate", help="生成组合")
    p_gen.add_argument("count", type=int, help="生成组数")
    p_gen.add_argument("--seed", type=int, default=42, help="随机种子")
    p_gen.add_argument("--only", action="store_true", help="只输出最终号码")
    p_gen.set_defaults(func=cmd_generate)

    p_fetch = sub.add_parser("fetch-issue", help="查询最新期开奖与下一期期号")
    p_fetch.set_defaults(func=cmd_fetch_issue)

    p_save = sub.add_parser("save-bets", help="保存指定期号投注方案")
    p_save.add_argument("issue", help="目标期号")
    p_save.add_argument("multiple", type=int, help="每注倍数")
    p_save.add_argument("--text", help="原始号码文本")
    p_save.add_argument("--input", help="从文件读取原始号码文本")
    p_save.add_argument("--append-mode", action="store_true", help="按追加投注保存")
    p_save.set_defaults(func=cmd_save_bets)

    p_check = sub.add_parser("check-draw", help="根据开奖号码核对指定期号投注")
    p_check.add_argument("issue", help="目标期号")
    p_check.add_argument("--draw", help="开奖号码文本，例如：前区：07 10 18 30 32 后区：04 08；不传则自动按期号查询")
    p_check.set_defaults(func=cmd_check_draw)

    return parser


def main() -> int:
    setup_console_encoding()
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
