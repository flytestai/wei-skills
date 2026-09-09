---
name: python-testdev-drill
description: Reusable module-based drill workflow for Python test-development engineer interview practice, with batch drilling, per-module history, wrong-book with spaced review, favorites, custom bank, non-repeating extraction, report, and multiple drill modes.
---

# Python TestDev Drill

为 Python 测试开发工程师面试准备提供**长期刷题系统**：模块化练习、进度持久化、错题本（含艾宾浩斯复习）、收藏夹、自建题库、统计报表、批量刷题、做题评分。

## 模块清单

- Python基础手写代码题（100 题，13 分类）
- Python编程基础理论面试题（100 题）
- Python高阶编程
- 自动化测试题
- Pytest框架
- 测试开发面试题
- 测试工程化与CI/CD
- 性能测试面试题
- 中间件面试题
- 数据库面试题
- Linux面试题

以上均为独立一等模块，**禁止互相合并**。性能/中间件/数据库/Linux 题不得路由进「自动化测试题」。

## 触发场景

用户想：按模块刷题/做题、指定每轮题数、续刷保存的进度、复习错题、复习收藏题、保存自建题、避免重复题、查看刷题报表、重刷到期错题、模拟面试时，使用本 skill。

## 两种核心模式

| 模式 | 触发词 | 行为 |
|------|--------|------|
| **刷题模式** | `刷题` / `继续刷题` / `切换到刷题模式` | 题目 + 参考答案一起展示 |
| **做题模式** | `做题` / `继续做题` / `做题模式` | 只给题目，等用户作答，再评分和建议 |

- `继续` = 复用上次模块、模式、批量大小。
- 用户点名模块即切换；切换不重置其他模块状态。

## 状态同步（必须使用脚本，禁止手工 Edit state.md）

所有状态操作必须通过 `sync_state.py` 完成（用 Python 3.13 绝对路径执行，工作目录为 skill 目录）：

```
sync_state.py switch --module <M> --mode brush --batch 5   # 切换模块/模式/批量
sync_state.py issue --module <M> --questions "51. a,52. b" --mode brush  # 出题后同步
sync_state.py answer --module <M> --question 51 --result correct         # 记录答对
sync_state.py answer --module <M> --question 51 --result wrong --note "原因"  # 记录答错进错题本
sync_state.py answer --module <M> --question 51 --result reveal          # 直接看答案也计为薄弱点
sync_state.py reset --module <M>                          # 清空模块进度（state+history 一起清）
sync_state.py report                                      # 全模块统计报表（进度条+错题数）
sync_state.py wrong-list --module <M>                     # 查看模块错题集
sync_state.py review --module <M>                         # 查看今日到期该复习的错题
```

出题、作答、切换、重置的**每一步**都必须立即调用脚本同步，禁止手工 Edit 造成的重复段落/编号错位。

## 答案风格规范（重要，用户明确要求）

1. **口语化**：像面试现场口头回答，说人话，不堆术语。
2. **正常面试回答长度**：不能只有一句话，也不要长篇大论——结构是「一句核心定义 → 展开 3-4 个要点（可带短代码）→ 一句话收尾/面试怎么答」。
3. **逻辑清晰**：先总后分、有编号、有对比表格（适合概念对比题）。
4. **易记忆**：给口诀或一句话总结（如「小右大左」「查补数、存自己」）。
5. 手写代码题：**只给一种最简单、最容易记忆的写法**，不罗列多种解法；附「记忆要点」。
6. 题目展示：完整题目 + 标签 + 难度 + 频率 + 示例（最多 1 个，边界必要时才加第 2 个）。

## 批量刷题规则

- 用户可指定每轮题数（如「每次给出5题和答案」），记入 `current_batch_size`。
- 批量出题时每题独立编号展示，结尾统一给进度提示。
- 修改批量大小用 `switch --batch N`。

## 做题模式评分规范

用户提交答案后，按以下维度点评（简洁、先肯定再指错）：

1. **正确性**（核心）
2. **边界处理**（空输入、单元素、越界）
3. **代码风格**（命名规范——用户曾用拼音命名 maop/fobi，应建议 bubble_sort/fibonacci）
4. **复杂度**（时间/空间，能提则提）

评分规则：
- 答案 < 8/10 → `answer --result wrong` 记入错题本
- 直接要答案 / 说不会 → `answer --result reveal` 记入错题本
- 重做全对 → 仍保留错题记录，次数+1 的逻辑只在再次答错时触发；重做正确时在 note 中追加"重做后全对"

点评后先给正确写法和记忆要点，再继续下一题。

## 常用交互指令

| 用户说 | 行为 |
|--------|------|
| `继续` / `继续刷` | 按当前模块/模式/批量继续下一批 |
| `看答案` | 展示当前题参考答案；做题模式下同时记为薄弱点（reveal） |
| `换一题` | 跳过当前题换下一题（被跳过的题仍记入 asked，不重置进度） |
| `保存进度` | 确认 state 已同步 + 在项目 memory 写当日进度日志 |
| `清空XX进度，从第一题开始` | `reset --module`，然后按当前模式从第 1 题重新开始 |
| `切换到刷题模式 XX` | switch 到目标模块（brush 模式） |
| `查看刷题报告` / `刷题报告` | 运行 `report` 并展示 |
| `重刷错题` / `复习错题` | 运行 `review`，到期的错题按做题模式重出 |
| `收藏第N题` / `收藏这题` | 加入模块收藏夹 |
| `保存这道题到XX` | 加入模块自建题库 |

## 去重规则（统一，仅此一份）

- 同一模块内，`asked_questions`、`history_questions`、`answer_given_questions` 构成统一的"已见集合"，刷题/做题模式共用。
- 默认只出未见过的题；题库耗尽时明确告知用户并询问是否允许重复。
- 错题/收藏/自建题复习模式可在各自池内重复。
- 模式切换不重置去重。

## 高频优先规则

- 题库带 frequency 字段（高频/中高频/加分题）时，**优先出高频题**，再中高频，再加分题。
- 按题库顺序推进（completed_through）时若发现前面的题是低频而后有高频，仍以顺序为主，避免状态管理复杂化；新建模块时直接按频率排好题目顺序。
- 手写代码模块细分路由：基础算法题归 `Python基础手写代码题`；工程封装题（logger/config/request/base_page/smart_wait）归其所属工程模块。

## 错题本与艾宾浩斯复习

错题格式（state.md 中，由脚本维护）：
```
- 题目全名 | 错误原因 | 日期 | 错N次 | 复习:YYYY-MM-DD,YYYY-MM-DD,...
```

- 复习周期：**1 / 3 / 7 / 15 天**（脚本自动计算下一复习日）。
- 每日首次进入刷题会话时，主动运行 `review` 提醒今日到期错题（有则提醒，无则不打扰）。
- 错题重刷采用**做题模式**（先答再看），答对不删记录、答错次数+1 并顺延复习日。

## 模拟面试模式（加分功能）

用户说 `模拟面试` 时：
1. 从当前模块（或用户指定模块）**随机**抽题（无视去重，模拟真实随机性）。
2. 每题限时思考（用户说"过"跳过，说"好了"开始回答）。
3. 用户回答后按面试官视角追问 1-2 个延伸问题（如答 two_sum 追问"dict 底层为什么查找快"）。
4. 结束后输出本场评分：正确率、表达清晰度、薄弱知识点。

## 输出模板

每题结构：
1. 题号 + 题目标识
2. 题目正文（含 1 个示例）
3. 标签 / 难度 / 频率
4. 参考答案（刷题模式或做题模式点评后）
5. 记忆要点（代码题）或 面试怎么答（理论题）

## 持久化模型

每个模块维护：module_name、completed_through、next_question、asked_questions、mistakes（结构化）、answer_given_questions、history_questions、favorite_questions、custom_questions、current_mode、current_batch_size、last_round_questions、last_round_results。

全部由 `sync_state.py` 读写，`state.md` 是唯一数据源（wrong_questions.md 仅作历史归档，不再写入）。

## 题库文件

| 模块 | 文件 |
|------|------|
| Python基础手写代码题 | module_python_basic_code.md |
| Python编程基础理论面试题 | MODULE_PYTHON_THEORY.md |
| Python高阶编程 | MODULE_ADVANCED_PYTHON.md |
| 自动化测试题 | MODULE_AUTOMATION_TEST.md |
| Pytest框架 | MODULE_PYTEST_FRAMEWORK.md |
| 测试开发面试题 | MODULE_TESTDEV_INTERVIEW.md |
| 测试工程化与CI/CD | MODULE_CICD_ENGINEERING.md |
| 性能测试面试题 | MODULE_PERFORMANCE_TEST.md |
| 中间件面试题 | MODULE_MIDDLEWARE_INTERVIEW.md |
| 数据库面试题 | MODULE_DATABASE_INTERVIEW.md |
| Linux面试题 | MODULE_LINUX_INTERVIEW.md |

题库格式统一：`### 编号. 题名` + tags / difficulty / frequency / prompt / answer。
扩充题库时：从真实面试来源搜集（面试鸭、CSDN 测试面试真题、51Testing 等），去重后追加，保持编号连续。
