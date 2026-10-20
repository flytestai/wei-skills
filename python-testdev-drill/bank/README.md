# 全量分级题库

本目录是 `python-testdev-drill` 的全量题库，按「领域 → 专题/知识点」组织，共 **7,478 道题**、**18 个领域**、**102 个专题**。

## 目录结构

```text
bank/
├── README.md              本说明
├── index.md               领域/专题索引（带题目文件链接）
├── index.json             轻量索引（领域、专题、题数、文件路径）
├── bank.json              完整结构化题库（适合程序查询）
├── query_bank.py          命令行查询工具
└── domains/
    └── <领域>/
        ├── README.md      该领域的专题清单
        └── <专题>/
            ├── part-01.md
            ├── part-02.md
            └── ...
```

每个专题按难度从低到高排列；单个 Markdown 文件最多 150 题，超过后自动分 `part-02.md`、`part-03.md`。每道题包含：

- 题目编号（`Q000001` 起）
- 题型、难度
- 题目
- 选项（选择题）
- 答案 / 正确选项
- 解析（核心考点、题目解析、答题要点、面试提示）

## 使用方法

在 `bank/` 目录下执行：

```bash
# 总览
python query_bank.py stats

# 列出领域
python query_bank.py domains

# 列出某领域的专题
python query_bank.py topics --domain 功能测试

# 随机抽题（可叠加领域、专题、题型、难度）
python query_bank.py random --domain 功能测试 --topic 测试用例 --count 3
python query_bank.py random --domain 数据库 --difficulty 中等 --count 5

# 按编号查看
python query_bank.py show Q000001

# 全文搜索
python query_bank.py search --keyword 接口 --limit 10

# 按顺序浏览
python query_bank.py list --domain 自动化 --topic Selenium --limit 20 --offset 0

# 机器可读输出
python query_bank.py random --domain 算法 --count 2 --json
```

随机抽题默认允许同一题干在不同专题中重复出现；加 `--dedupe` 可按题干去重。`--json` 输出完整字段，便于接入其他脚本。

## 数据说明

- 7,478 道题均包含答案和解析；没有空答案、空解析。
- **43 道题**的文字答案由 AI 补全（原数据只有图片答案、解析要点或完全缺失），在 Markdown 中标注「答案：AI 补全」，在 `bank.json` 中对应 `answer_generated: true`。
- **371 道题**的解析由 AI 补全（原数据未提供解析），在 Markdown 中标注「解析：AI 补全」，在 `bank.json` 中对应 `analysis_generated: true`。
- 其余答案和解析保留原始内容，仅做格式清洗、术语统一和重复记录保留。
- 题干完全相同的记录未删除，因为同一道题可能同时属于多个专题；需要去重时使用 `--dedupe`。
- 题库不包含任何外部文章链接、机构标识、品牌名、原始题目 ID 或来源字段。

## 与刷题流程的关系

`bank/` 是**全量分级题库/查询池**，不替代 `SKILL.md` 中已注册的 15 个专项模块。默认刷题仍按原模块和 `state.md` 进度执行；当用户要求「按领域刷题」「按专题刷题」「从全量题库抽题」时，使用本目录和 `query_bank.py`。
