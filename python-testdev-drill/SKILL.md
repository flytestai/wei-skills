---
name: python-testdev-drill
description: Reusable module-based drill workflow for Python test-development engineer interview practice, now upgraded with configurable batch drilling, per-module history, wrong-book, favorites, custom question bank, non-repeating extraction, and multiple drill modes.
---

# Python TestDev Drill

## Purpose

Provide a reusable long-term interview drill system for Python test-development engineer preparation.

This skill is no longer just a one-question practice flow. It is a **persistent question-drill system** with:
- module-based practice
- configurable question count per round
- optional direct answers per question
- non-repeating question extraction
- per-module history
- wrong-question review
- favorites review
- custom question bank

## Use This Skill When

Use this skill when the user wants to:
- practice interview questions by module
- choose how many questions to receive at once
- continue from saved progress
- review wrong questions
- review favorite questions
- save custom questions into a module bank
- avoid repeating questions already brushed
- use **刷题模式**（题目 + 参考答案）
- use **做题模式**（只给题目，用户作答后再评分和建议）

## Core Behavior

- Support both **single-question** and **multi-question** drill.
- The skill supports two first-class interaction modes:
  - **刷题模式** = give the question and show the reference answer by default
  - **做题模式** = give the question only, wait for the user's answer, then score and advise
- If the user says `继续`, resume the last module, last drill mode, and last batch size.
- If the user says `刷题` or `继续刷题`, explicitly enter **刷题模式**.
- If the user says `做题` or `继续做题`, explicitly enter **做题模式**.
- If the user says `做题模式`, explicitly enter **做题模式**.
- If the user explicitly names a module, switch to that module.
- For both **刷题模式** and **做题模式**, extraction must use the same de-duplication rules.
- As long as the current pool still has unseen questions, do not repeat already asked questions.
- Questions asked in any mode must be written into history.
- Question issuance itself must trigger automatic progress synchronization for the current module.
- In both `刷题模式` and `做题模式`, once a question is issued, the skill should immediately update the current active module, current mode, last round question, and seen-question records.
- Questions directly answered in `做题模式` must also count as already seen for future de-duplication.
- For **all modules**, prefer **高频** questions first, then **中高频**, then **加分题**.
- This high-frequency-first rule applies to both **刷题模式** and **做题模式**.
- Any future newly created module must inherit the same high-frequency-first routing rule.
- For hand-coding practice, keep two distinct routes:
  - `Python基础手写代码题` should focus on 基础高频题 such as 列表、字符串、字典、集合、栈、双指针、哈希、排序.
  - `logger/config/request/assert/base page/smart wait` style engineering implementation questions should be routed to a separate 测试开发工程手写题 line or related engineering modules, instead of being mixed into the basic hand-code mainline.

## Supported Drill Modes

### 1. 随机刷题
Examples:
- `随机刷 3 道题`
- `随机刷 5 道 Python 面试题`

Behavior:
- select unseen questions first
- can mix system bank + custom bank if appropriate
- show reference answers by default

### 2. 选择模块刷题
Examples:
- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`

Behavior:
- extract from the named module
- default to unseen questions first
- each question includes a reference answer unless the user asks to hide answers

### 3. 随机做题
Examples:
- `随机做 3 道题`
- `随机做 5 道 Python 面试题`

Behavior:
- select unseen questions first
- can mix system bank + custom bank if appropriate
- do not show the answer by default
- wait for the user answer, then score and advise

### 4. 选择模块做题
Examples:
- `做 3 道 Python基础手写代码题`
- `做 5 道 自动化测试题`
- `继续 Python编程基础理论面试题做题`

Behavior:
- extract from the named module
- default to unseen questions first
- do not show the answer by default
- after the user answers, score on correctness, edge cases, style, complexity, and expression clarity

### 5. 错题集刷题 / 做题
Examples:
- `刷错题集`
- `做错题集`
- `做 5 道 自动化测试题错题`

Behavior:
- prioritize historically mistaken questions
- if wrong bank is empty, say so clearly
- 刷题模式显示答案，做题模式先不给答案

### 6. 收藏题库刷题 / 做题
Examples:
- `刷收藏题`
- `做 3 道 测试开发面试题收藏题`

Behavior:
- extract from favorite questions only
- 刷题模式显示答案，做题模式先不给答案

### 7. 自建题库刷题 / 做题
Examples:
- `刷自建题库`
- `从 Python基础手写代码题自建题库做 4 道`

Behavior:
- extract from user-saved custom questions only
- 刷题模式显示答案，做题模式先不给答案

## Answer Visibility Rules

### Default rules
- In `刷题` mode, each question should include a concise reference answer by default.
- In `做题` mode, the answer should be hidden by default.
- If the user asks `先只给题，不要答案`, hide answers for the current round.
- If the user later asks `看答案`, reveal the stored answer.
- In `做题` mode, after the user submits an answer, score first and give suggestions first; only reveal the reference answer when the user asks for it or when it is clearly necessary for correction.

### Legacy / direct answer request
If the user says:
- `给出答案`
- `直接给答案`

Behavior:
- provide the answer to the current question
- in `做题模式`, always treat that question as a weak point and add it to the module's wrong-question notebook
- do not append duplicates if the same question is already in the wrong-question notebook
- this rule applies especially to `做题模式`, because asking directly for the answer means the current question should be treated as a weak point

## Question Bank Layers

Each module may draw from these layers:

1. **System bank** — built-in question bank
2. **Custom bank** — user-saved questions
3. **Favorites bank** — user-starred questions
4. **Wrong bank** — historically mistaken questions
5. **History log** — all brushed questions

## Non-Repetition Rules

Inside the same module:
- `刷题模式` and `做题模式` must share one unified de-duplication pool
- any question that has appeared before in `asked_questions`, `history_questions`, or `answer_given_questions` counts as already seen
- default extraction must always prefer unseen questions first
- do not repeat questions only because the interaction mode changed from `刷题` to `做题`, or from `做题` to `刷题`
- prefer unseen system questions first, then unseen custom questions
- wrong / favorites / custom review modes may repeat only inside their own review pool
- if the normal module pool is exhausted, explicitly tell the user that new questions are exhausted and ask whether repetition is allowed

## Persistence Model

Each module maintains:
- module_name
- completed_through
- next_question
- asked_questions
- mistakes
- answer_given_questions
- history_questions
- favorite_questions
- custom_questions
- current_mode
- current_batch_size
- last_round_questions
- last_round_results

## New User Actions

### Save a custom question
Examples:
- `保存这道题到 Python基础手写代码题`
- `加入到 自动化测试题 自建题库`

Behavior:
- save the original question text into that module's custom bank
- preserve module isolation

### Favorite a question
Examples:
- `收藏第2题`
- `把这题加入收藏`

Behavior:
- save into the module's favorites bank

### Query stored data
Examples:
- `查看刷题历史`
- `查看自动化测试题错题集`
- `查看测试开发面试题收藏题库`
- `查看Python基础手写代码题自建题库`

## Runtime Rules

### Default extraction
- If the user does not specify a mode, use the current module and prefer unseen questions first.
- If the user only says `继续`, reuse the last module, last mode, and last batch size.
- If the user says `刷题` or `继续刷题`, explicitly continue in `刷题模式`.
- If the user says `做题`, `继续做题`, or `做题模式`, explicitly continue in `做题模式`.

### Mode routing
- wrong mode → only use `wrong_questions.md`
- favorites mode → only use `favorites.md`
- custom mode → only use `custom_questions.md`
- module mode / random mode → use system bank first, then unseen custom questions
- `刷题模式` and `做题模式` share the same extraction, de-duplication, wrong-book, favorites, and custom-bank routing logic
- the only default difference between `刷题模式` and `做题模式` is answer visibility and whether the user answers first before scoring

### De-duplication
- By default, do not repeat questions already seen in the same module, whether they were seen in `刷题模式` or `做题模式`.
- Treat `asked_questions`, `history_questions`, and `answer_given_questions` as a unified seen-question set.
- Switching modes must not reset or weaken de-duplication.
- If the available normal pool is exhausted, explicitly ask whether repetition is allowed instead of silently reusing old questions.
- Wrong/favorites modes may repeat because the goal is targeted review, but normal module extraction must stay de-duplicated.

### Output template
For each question, use this structure when possible:
1. 题号 / identifier
2. 标题
3. 题目正文
4. 标签
5. 难度
6. 参考答案（if answers are visible in the current round）

### Question brevity
- By default, keep question prompts concise.
- Prefer only one necessary example.
- Add a second example only when the edge case truly needs clarification.
- Prefer: 题目 + 关键要求 + 1 个示例, instead of long explanatory setup.

### Write-back rules
- Any brushed question must be appended to `history.md`.
- In both `刷题模式` and `做题模式`, as soon as a question is issued, automatically sync the current module progress.
- Automatic sync should update at least: `last_active_module`, `last_active_mode`, `last_batch_size`, `last_round_questions`, and the module's seen-question records.
- Add to `wrong_questions.md` when:
  - the user answers incorrectly
  - the user directly asks for the answer
  - the user explicitly says they do not know it / need review
- Add to `favorites.md` only on explicit favorite action.
- Add to `custom_questions.md` only when the user explicitly asks to save a custom question.

### Answer visibility
- In brushing mode, concise reference answers should be shown by default.
- In doing mode, answers should be hidden by default.
- If the user asks to hide answers, suppress answers for the current round.
- The user may later request the answer for a specific question.
- In `做题模式`, after the user submits an answer, evaluate first, then give suggestions, and then reveal the reference answer only when requested or clearly helpful.

## Scoring Framework

When the user submits an answer or code, evaluate concisely on:
- correctness
- edge cases
- code style
- time complexity
- space complexity
- interview communication
- implementation clarity for coding questions

Scoring rule for `做题模式`:
- if the answer score is below `8/10`, add the question to the module's wrong-question notebook
- if the user directly requests the answer, also add the question to the module's wrong-question notebook
- do not append duplicates if the same question is already in the wrong-question notebook

Record wrong or weak items into the module's wrong-question notebook when appropriate.
In `做题模式`, scoring and suggestions should come before the reference answer unless the user explicitly requests the answer first.

## Bundled Resources

- `state.md`: current persisted multi-module state
- `MODULES.md`: module contract and expansion rules
- `QUESTION_BANK_GUIDE.md`: question-bank organization guidance
- `history.md`: brushed-question history
- `wrong_questions.md`: wrong-question notebook
- `favorites.md`: favorites bank
- `custom_questions.md`: user custom bank
- `question_bank.md`: bank structure/index notes

## Current Seed Modules

- Python基础手写代码题
- 自动化测试题
- 测试开发面试题
- Python编程基础理论面试题
- 测试工程化与CI/CD
