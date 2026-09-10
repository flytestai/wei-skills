#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""python-testdev-drill 状态同步脚本

统一管理刷题状态，替代手工 Edit，杜绝状态错乱。
用法（在 skill 目录下执行，或用绝对路径）：
  python sync_state.py switch --module Python基础手写代码题 --mode brush --batch 1   切换模块/模式/批量
  python sync_state.py issue --module M --questions "51. a,52. b" --mode brush        出题后同步
  python sync_state.py answer --module M --question 51 --result correct               记录作答正确
  python sync_state.py answer --module M --question 51 --result wrong --note "原因"   记录作答错误进错题本
  python sync_state.py reset --module M                                              清空模块进度
  python sync_state.py report                                                        全模块统计报表
  python sync_state.py wrong-list --module M                                         列出错题
  python sync_state.py review --module M                                             列出到期该复习的错题（艾宾浩斯 1/3/7/15 天）
"""
import argparse
import io
import os
import re
import sys
from datetime import date, datetime, timedelta

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SKILL_DIR, "state.md")
HISTORY_FILE = os.path.join(SKILL_DIR, "history.md")

# 艾宾浩斯复习周期（天）
REVIEW_INTERVALS = [1, 3, 7, 15]


def read_file(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(content)


def find_module_section(content, module_name):
    """返回 (start, end) 字符偏移，定位 '## Module: <name>' 段落。找不到返回 None。"""
    header = "## Module: " + module_name
    start = content.find(header)
    if start == -1:
        return None
    nxt = content.find("\n## Module: ", start + 1)
    nxt2 = content.find("\n# ", start + 1)  # 兼容一级标题结尾
    ends = [p for p in (nxt, nxt2) if p != -1]
    end = min(ends) + 1 if ends else len(content)
    return start, end


def parse_module_fields(section):
    """把模块段落解析为 dict：单值键 -> str，列表键 -> [str]。"""
    fields = {}
    current_list_key = None
    for line in section.splitlines():
        m = re.match(r"^(\w+):(.*)$", line)
        if m and not line.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                fields[key] = []
            else:
                fields[key] = val
            current_list_key = key if isinstance(fields[key], list) else None
        elif line.startswith("  - ") and current_list_key:
            fields[current_list_key].append(line[4:].strip())
    return fields


def rebuild_module_section(module_name, fields, order):
    """按固定键顺序重建模块段落文本。"""
    lines = ["## Module: " + module_name, "", "module_name: " + module_name]
    for key in order:
        if key == "module_name":
            continue
        val = fields.get(key, [])
        if isinstance(val, list):
            if not val:
                lines.append(key + ":")
            else:
                lines.append(key + ":")
                lines.extend("  - " + v for v in val)
        else:
            lines.append(key + ": " + str(val))
    return "\n".join(lines) + "\n\n"


FIELD_ORDER = [
    "module_name", "completed_through", "next_question", "asked_questions",
    "mistakes", "answer_given_questions", "history_questions",
    "favorite_questions", "custom_questions", "current_mode",
    "current_batch_size", "last_round_questions", "last_round_results",
]


def load_module(content, module_name):
    pos = find_module_section(content, module_name)
    if not pos:
        return None, None
    s, e = pos
    return parse_module_fields(content[s:e]), (s, e)


def save_module(content, module_name, fields):
    pos = find_module_section(content, module_name)
    if not pos:
        raise SystemExit("模块不存在: " + module_name)
    s, e = pos
    return content[:s] + rebuild_module_section(module_name, fields, FIELD_ORDER) + content[e:]


def bank_file_questions(module_name):
    """统计模块题库文件中的题目总数。"""
    bank_map = {
        "Python基础手写代码题": "module_python_basic_code.md",
        "Python编程基础理论面试题": "MODULE_PYTHON_THEORY.md",
        "Python高阶编程": "MODULE_ADVANCED_PYTHON.md",
        "自动化测试题": "MODULE_AUTOMATION_TEST.md",
        "Pytest框架": "MODULE_PYTEST_FRAMEWORK.md",
        "测试开发面试题": "MODULE_TESTDEV_INTERVIEW.md",
        "测试工程化与CI/CD": "MODULE_CICD_ENGINEERING.md",
        "性能测试面试题": "MODULE_PERFORMANCE_TEST.md",
        "中间件面试题": "MODULE_MIDDLEWARE_INTERVIEW.md",
        "数据库面试题": "MODULE_DATABASE_INTERVIEW.md",
        "Linux面试题": "MODULE_LINUX_INTERVIEW.md",
    }
    fname = bank_map.get(module_name)
    if not fname:
        return None
    path = os.path.join(SKILL_DIR, fname)
    if not os.path.exists(path):
        return None
    text = read_file(path)
    # 兼容两种题目标题格式：'### 1. x' 与 '## 1. x'
    n1 = len(re.findall(r"^### ", text, re.M))
    n2 = len(re.findall(r"^## \d+\. ", text, re.M))
    return n1 + n2


def cmd_switch(args):
    content = read_file(STATE_FILE)
    # 全局状态
    if args.module:
        content = re.sub(r"last_active_module: .*", "last_active_module: " + args.module, content)
    if args.mode:
        content = re.sub(r"last_active_mode: .*", "last_active_mode: " + args.mode, content)
    if args.batch:
        content = re.sub(r"last_batch_size: \d+", "last_batch_size: %d" % args.batch, content)
        fields, _ = load_module(content, args.module)
        if fields is None:
            raise SystemExit("模块不存在: " + args.module)
        fields["current_mode"] = args.mode if args.mode else fields.get("current_mode", "brush")
        fields["current_batch_size"] = str(args.batch)
        content = save_module(content, args.module, fields)
    write_file(STATE_FILE, content)
    print("switched: module=%s mode=%s batch=%s" % (args.module, args.mode, args.batch))


def cmd_issue(args):
    content = read_file(STATE_FILE)
    fields, _ = load_module(content, args.module)
    if fields is None:
        raise SystemExit("模块不存在: " + args.module)
    qs = [q.strip() for q in args.questions.split(",") if q.strip()]
    for q in qs:
        if q not in fields["asked_questions"]:
            fields["asked_questions"].append(q)
        if q not in fields["history_questions"]:
            fields["history_questions"].append(q)
    last_num = 0
    for q in fields["asked_questions"]:
        m = re.match(r"^(\d+)\.", q)
        if m:
            last_num = max(last_num, int(m.group(1)))
    # 若无编号（自定义题），用数量兜底
    fields["completed_through"] = str(max(last_num, len(fields["asked_questions"])))
    fields["next_question"] = str(int(fields["completed_through"]) + 1)
    fields["last_round_questions"] = qs
    fields["last_round_results"] = ["question_issued_in_" + ("brush" if args.mode == "brush" else "do") + "_mode"]
    content = save_module(content, args.module, fields)
    # 同步 history.md
    hist = read_file(HISTORY_FILE)
    header = "## " + args.module
    hpos = hist.find(header)
    if hpos == -1:
        raise SystemExit("history.md 缺少模块段落: " + args.module)
    hnext = hist.find("\n## ", hpos + 1)
    hnext = hnext + 1 if hnext != -1 else len(hist)
    seg = hist[hpos:hnext]
    add = ""
    for q in qs:
        # 只保留 "编号. 名称" 中的全行
        if ("\n- " + q + "\n") not in seg:
            add += "- " + q + "\n"
    if add:
        if not seg.endswith("\n"):
            seg += "\n"
        hist = hist[:hpos] + seg + add + hist[hnext:]
        write_file(HISTORY_FILE, hist)
    write_file(STATE_FILE, content)
    print("issued %d questions, next_question=%s" % (len(qs), fields["next_question"]))


def q_key(q):
    """题目归一化键：去掉 "N. " 编号前缀，用于错题本与 asked 列表的匹配。
    兼容错题本中不带编号的旧条目（如 dedup_list）与带编号的写法（如 3. dedup_list）。"""
    return re.sub(r"^\d+\.\s*", "", q).strip()


def parse_mistake_line(line):
    """解析错题行，兼容新旧两种格式：
    新: - 题目 | 原因 | YYYY-MM-DD | 错N次 | 复习:YYYY-MM-DD,YYYY-MM-DD
    旧: - 题目（原因文字）  或  - 题目
    """
    line = line.lstrip("- ").strip()
    today = date.today().isoformat()
    if "|" in line:
        parts = [p.strip() for p in line.split("|")]
        q = parts[0]
        reason = parts[1] if len(parts) > 1 else ""
        d = parts[2] if len(parts) > 2 else today
        cnt = parts[3] if len(parts) > 3 else "错1次"
        review = parts[4] if len(parts) > 4 and parts[4].startswith("复习") else "复习:"
        return {"q": q, "reason": reason, "date": d, "count": cnt, "review": review}
    m = re.match(r"^(.+?)（(.+?)）$", line)
    if m:
        return {"q": m.group(1), "reason": m.group(2), "date": today, "count": "错1次", "review": "复习:"}
    return {"q": line, "reason": "", "date": today, "count": "错1次", "review": "复习:"}


def format_mistake_line(mk):
    # 注意：rebuild_module_section 写入列表项时会自动加 "  - " 前缀，
    # 这里不能再加 "- "，否则会写成 "- - 题目" 的双横线。
    return "%s | %s | %s | %s | %s" % (mk["q"], mk["reason"], mk["date"], mk["count"], mk["review"])


def cmd_answer(args):
    content = read_file(STATE_FILE)
    fields, _ = load_module(content, args.module)
    if fields is None:
        raise SystemExit("模块不存在: " + args.module)
    # 找到该编号的题目全名
    target = None
    for q in fields["asked_questions"]:
        if q.startswith(args.question + ".") or q == args.question:
            target = q
            break
    if target is None:
        target = args.question
    # answer_given 记录
    if args.result == "correct":
        if target not in fields["answer_given_questions"]:
            fields["answer_given_questions"].append(target)
        result_line = "user_answered_correctly"
    else:
        result_line = "user_answered_wrongly_added_to_mistakes"
        if args.result == "reveal":  # 直接看答案也计为薄弱点
            result_line = "answer_revealed_added_to_mistakes"
        # 更新/新增错题（结构化格式）
        parsed = [parse_mistake_line(x) for x in fields["mistakes"]]
        found = False
        for mk in parsed:
            if q_key(mk["q"]) == q_key(target):
                n = re.sub(r"\D", "", mk["count"]) or "0"
                mk["count"] = "错%d次" % (int(n) + 1)
                mk["reason"] = args.note or mk["reason"]
                mk["date"] = date.today().isoformat()
                mk["q"] = target  # 统一升级为带编号的写法
                # 追加下一个复习日
                mk["review"] = add_review_date(mk["review"])
                found = True
                break
        if not found:
            mk = {"q": target, "reason": args.note or "", "date": date.today().isoformat(),
                  "count": "错1次", "review": add_review_date("复习:")}
            parsed.append(mk)
        fields["mistakes"] = [format_mistake_line(x) for x in parsed]
    fields["last_round_results"] = [result_line]
    content = save_module(content, args.module, fields)
    write_file(STATE_FILE, content)
    print("answer recorded: %s -> %s" % (target, args.result))


def add_review_date(review_str):
    """追加下一个复习日期（1/3/7/15 天周期）。"""
    dates = [d for d in review_str.replace("复习:", "").split(",") if d]
    intervals_left = [i for i in REVIEW_INTERVALS if len(dates) < REVIEW_INTERVALS.index(i) + 1]
    # 周期: 第 len(dates) 个复习点
    idx = len(dates)
    if idx >= len(REVIEW_INTERVALS):
        return "复习:" + ",".join(dates)  # 周期走完不再追加
    nxt = (date.today() + timedelta(days=REVIEW_INTERVALS[idx])).isoformat()
    dates.append(nxt)
    return "复习:" + ",".join(dates)


def cmd_reset(args):
    content = read_file(STATE_FILE)
    fields, _ = load_module(content, args.module)
    if fields is None:
        raise SystemExit("模块不存在: " + args.module)
    keep_mode = fields.get("current_mode", "brush")
    keep_batch = fields.get("current_batch_size", "1")
    blank = {k: ([] if isinstance(fields.get(k), list) else "") for k in FIELD_ORDER}
    blank["module_name"] = args.module
    blank["completed_through"] = "0"
    blank["next_question"] = "1"
    blank["current_mode"] = keep_mode
    blank["current_batch_size"] = keep_batch
    content = save_module(content, args.module, blank)
    write_file(STATE_FILE, content)
    # 清空 history.md 对应段落
    hist = read_file(HISTORY_FILE)
    hpos = hist.find("## " + args.module)
    if hpos != -1:
        hnext = hist.find("\n## ", hpos + 1)
        hnext = hnext + 1 if hnext != -1 else len(hist)
        hist = hist[:hpos] + "## " + args.module + "\n\n" + hist[hnext:]
        write_file(HISTORY_FILE, hist)
    print("module reset: " + args.module)


def cmd_report(args):
    content = read_file(STATE_FILE)
    print("=" * 62)
    print("刷题进度总报表  (%s)" % date.today().isoformat())
    print("=" * 62)
    for m in re.finditer(r"^## Module: (.+)$", content, re.M):
        name = m.group(1)
        fields, _ = load_module(content, name)
        total = bank_file_questions(name)
        done = len(fields.get("asked_questions", []))
        wrong = len(fields.get("mistakes", []))
        mode = fields.get("current_mode", "-")
        batch = fields.get("current_batch_size", "-")
        bar_len = 20
        pct = (done / total * 100) if total else 0
        filled = int(done / total * bar_len) if total else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print("\n[%s]  模式:%s 批量:%s" % (name, mode, batch))
        print("  进度  %s %d/%d (%.0f%%)   错题:%d" % (bar, done, total or 0, pct, wrong))
    print("\n" + "-" * 62)
    print("指令提示: review --module <模块> 查看到期复习错题")


def cmd_wrong_list(args):
    content = read_file(STATE_FILE)
    fields, _ = load_module(content, args.module)
    if fields is None:
        raise SystemExit("模块不存在: " + args.module)
    mistakes = fields.get("mistakes", [])
    if not mistakes:
        print("该模块暂无错题 ✅")
        return
    print("== %s 错题集（%d 题）==" % (args.module, len(mistakes)))
    for line in mistakes:
        mk = parse_mistake_line(line)
        print("  ● %s\n    原因: %s\n    %s | %s | %s" % (
            mk["q"], mk["reason"] or "-", mk["date"], mk["count"], mk["review"] or "复习:未安排"))


def cmd_review(args):
    content = read_file(STATE_FILE)
    fields, _ = load_module(content, args.module)
    if fields is None:
        raise SystemExit("模块不存在: " + args.module)
    today = date.today()
    due = []
    for line in fields.get("mistakes", []):
        mk = parse_mistake_line(line)
        dates = [d for d in mk["review"].replace("复习:", "").split(",") if d]
        for d in dates:
            try:
                if date.fromisoformat(d) <= today:
                    due.append((mk, d))
                    break
            except ValueError:
                continue
    if not due:
        print("今天没有到期需要复习的错题 ✅（艾宾浩斯周期 1/3/7/15 天）")
        return
    print("== %s 今日到期复习错题（艾宾浩斯）==" % args.module)
    for mk, d in due:
        print("  ● %s  (应复习日 %s)\n    原因: %s | %s" % (mk["q"], d, mk["reason"] or "-", mk["count"]))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("switch")
    p.add_argument("--module", required=True)
    p.add_argument("--mode", default=None)
    p.add_argument("--batch", type=int, default=None)

    p = sub.add_parser("issue")
    p.add_argument("--module", required=True)
    p.add_argument("--questions", required=True, help="逗号分隔的题目列表，如 '51. a,52. b'")
    p.add_argument("--mode", default="brush")

    p = sub.add_parser("answer")
    p.add_argument("--module", required=True)
    p.add_argument("--question", required=True, help="题号或题目全名")
    p.add_argument("--result", required=True, choices=["correct", "wrong", "reveal"])
    p.add_argument("--note", default="")

    p = sub.add_parser("reset")
    p.add_argument("--module", required=True)

    sub.add_parser("report")

    p = sub.add_parser("wrong-list")
    p.add_argument("--module", required=True)

    p = sub.add_parser("review")
    p.add_argument("--module", required=True)

    args = ap.parse_args()
    {"switch": cmd_switch, "issue": cmd_issue, "answer": cmd_answer,
     "reset": cmd_reset, "report": cmd_report, "wrong-list": cmd_wrong_list,
     "review": cmd_review}[args.cmd](args)


if __name__ == "__main__":
    main()
