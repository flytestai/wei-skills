#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查询全量分级题库。

用法：
  python query_bank.py stats
  python query_bank.py domains
  python query_bank.py topics --domain 功能测试
  python query_bank.py random --domain 功能测试 --topic 测试用例 --count 3
  python query_bank.py show Q000001
  python query_bank.py search --keyword 接口 --limit 10
  python query_bank.py list --domain 数据库 --limit 20 --offset 0

所有命令都支持 --json，输出机器可读 JSON。
"""
import argparse
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "bank.json")


def load():
    with open(BANK, encoding="utf-8") as f:
        return json.load(f)


def all_questions(bank):
    for d in bank["domains"]:
        for t in d["topics"]:
            for q in t["questions"]:
                yield q


def dedupe(items):
    seen = set()
    out = []
    for q in items:
        key = re.sub(r"\s+", "", q["question"])
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


def filter_questions(bank, domain=None, topic=None, qtype=None, difficulty=None):
    rows = []
    for q in all_questions(bank):
        if domain and q["domain"] != domain:
            continue
        if topic and q["topic"] != topic:
            continue
        if qtype and q["type"] != qtype:
            continue
        if difficulty and q["difficulty"] != difficulty:
            continue
        rows.append(q)
    return rows


def format_question(q, show_analysis=True):
    lines = [
        f"[{q['id']}] {q['domain']} / {q['topic']} · {q['type']} · {q['difficulty']}",
        "",
        "题目：",
        q["question"],
    ]
    if q.get("options"):
        lines += ["", "选项："] + list(q["options"])
    lines += ["", "答案：", q["answer"]]
    if q.get("answer_detail"):
        lines += ["", "正确选项：", q["answer_detail"]]
    if show_analysis:
        lines += ["", "解析：", q["analysis"]]
    return "\n".join(lines)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="查询 Python 测试开发全量分级题库")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("stats", help="题库统计")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("domains", help="列出领域")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("topics", help="列出专题")
    p.add_argument("--domain", required=True)
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("random", help="随机抽题")
    p.add_argument("--domain")
    p.add_argument("--topic")
    p.add_argument("--type")
    p.add_argument("--difficulty")
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--dedupe", action="store_true", help="按题干去重")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("show", help="按编号查看题目")
    p.add_argument("id")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("search", help="全文搜索")
    p.add_argument("--keyword", required=True)
    p.add_argument("--domain")
    p.add_argument("--topic")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--dedupe", action="store_true")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("list", help="按顺序列出题目")
    p.add_argument("--domain")
    p.add_argument("--topic")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--dedupe", action="store_true")
    p.add_argument("--json", action="store_true")

    args = parser.parse_args()
    bank = load()

    if args.cmd == "stats":
        data = bank["meta"]
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
            return
        print(f"题库：{data['name']}")
        print(f"题目：{data['total_questions']} 道")
        print(f"领域：{data['domains']} 个 · 专题：{data['topics']} 个")
        print("题型：" + "，".join(f"{k} {v}" for k, v in data["types"].items()))
        print("难度：" + "，".join(f"{k} {v}" for k, v in data["difficulties"].items()))
        print(f"AI 补全答案：{data['generated_answers']} 道")
        print(f"AI 补全解析：{data['generated_analyses']} 道")
        return

    if args.cmd == "domains":
        rows = [{"domain": d["name"], "question_count": d["question_count"], "topic_count": len(d["topics"])} for d in bank["domains"]]
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=2))
            return
        for r in rows:
            print(f"{r['domain']:<12} {r['question_count']:>5} 题  {r['topic_count']:>2} 个专题")
        return

    if args.cmd == "topics":
        d = next((x for x in bank["domains"] if x["name"] == args.domain), None)
        if not d:
            raise SystemExit("未找到领域：" + args.domain)
        rows = [{"topic": t["name"], "question_count": t["question_count"], "parts": t["parts"]} for t in d["topics"]]
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=2))
            return
        for r in rows:
            print(f"{r['topic']:<16} {r['question_count']:>5} 题")
        return

    if args.cmd == "show":
        q = next((x for x in all_questions(bank) if x["id"] == args.id), None)
        if not q:
            raise SystemExit("未找到题目：" + args.id)
        if args.json:
            print(json.dumps(q, ensure_ascii=False, indent=2))
        else:
            print(format_question(q))
        return

    rows = filter_questions(bank, getattr(args, "domain", None), getattr(args, "topic", None),
                            getattr(args, "type", None), getattr(args, "difficulty", None))
    if args.cmd == "search":
        kw = args.keyword.lower()
        rows = [q for q in rows if kw in (q["question"] + "\n" + q["answer"] + "\n" + q["analysis"]).lower()]
        rows = rows[: args.limit]
    elif args.cmd == "list":
        rows = rows[args.offset: args.offset + args.limit]
    elif args.cmd == "random":
        if args.dedupe:
            rows = dedupe(rows)
        if not rows:
            raise SystemExit("没有匹配的题目")
        rows = random.SystemRandom().sample(rows, min(args.count, len(rows)))
    if args.dedupe and args.cmd != "random":
        rows = dedupe(rows)
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    if not rows:
        print("没有匹配的题目")
        return
    for i, q in enumerate(rows):
        if i:
            print("\n" + "=" * 60 + "\n")
        print(format_question(q))


if __name__ == "__main__":
    main()
