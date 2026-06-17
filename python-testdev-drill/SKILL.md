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
- receive each question with its answer
- continue from saved progress
- review wrong questions
- review favorite questions
- save custom questions into a module bank
- avoid repeating questions already brushed

## Core Behavior

- Support both **single-question** and **multi-question** drill.
- Default drill output may include the answer when the user is in 刷题 mode.
- If the user says `继续`, resume the last module and last drill mode.
- If the user explicitly names a module, switch to that module.
- Newly generated questions should avoid the module's brushed history first.
- Questions brushed in any mode must be written into history.

## Supported Drill Modes

### 1. 随机刷题
Examples:
- `随机刷 3 道题`
- `随机刷 5 道 Python 面试题`

Behavior:
- select unseen questions first
- can mix system bank + custom bank if appropriate

### 2. 选择模块刷题
Examples:
- `刷 3 道 Python基础手写代码题`
- `刷 5 道 自动化测试题`

Behavior:
- extract from the named module
- default to unseen questions first
- each question includes a reference answer unless the user asks to hide answers

### 3. 错题集刷题
Examples:
- `刷错题集`
- `刷 5 道 自动化测试题错题`

Behavior:
- prioritize historically mistaken questions
- if wrong bank is empty, say so clearly

### 4. 收藏题库刷题
Examples:
- `刷收藏题`
- `刷 3 道 测试开发面试题收藏题`

Behavior:
- extract from favorite questions only

### 5. 自建题库刷题
Examples:
- `刷自建题库`
- `从 Python基础手写代码题自建题库刷 4 道`

Behavior:
- extract from user-saved custom questions only

## Answer Visibility Rules

### Default rules
- In `刷题` mode, each question may include a concise reference answer by default.
- If the user asks `先只给题，不要答案`, hide answers for the current round.
- If the user later asks `看答案`, reveal the stored answer.

### Legacy answer request
If the user says:
- `给出答案`
- `直接给答案`

Behavior:
- provide the answer to the current question
- add that question to the module's wrong-question notebook if appropriate

## Question Bank Layers

Each module may draw from these layers:

1. **System bank** — built-in question bank
2. **Custom bank** — user-saved questions
3. **Favorites bank** — user-starred questions
4. **Wrong bank** — historically mistaken questions
5. **History log** — all brushed questions

## Non-Repetition Rules

Inside the same module:
- avoid repeating brushed history first
- avoid repeating directly answered questions first
- prefer unseen system questions, then unseen custom questions
- if the bank is exhausted, explicitly tell the user and ask whether repetition is allowed

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

### Mode routing
- wrong mode → only use `wrong_questions.md`
- favorites mode → only use `favorites.md`
- custom mode → only use `custom_questions.md`
- module mode / random mode → use system bank first, then unseen custom questions

### De-duplication
- By default, do not repeat questions already in `history.md` for the same module.
- If the available pool is exhausted, explicitly ask whether repetition is allowed.
- Wrong/favorites modes may repeat because the goal is review.

### Output template
For each question, use this structure when possible:
1. 题号 / identifier
2. 标题
3. 题目正文
4. 标签
5. 难度
6. 参考答案（if answers are visible in the current round）

### Write-back rules
- Any brushed question must be appended to `history.md`.
- Add to `wrong_questions.md` when:
  - the user answers incorrectly
  - the user directly asks for the answer
  - the user explicitly says they do not know it / need review
- Add to `favorites.md` only on explicit favorite action.
- Add to `custom_questions.md` only when the user explicitly asks to save a custom question.

### Answer visibility
- In brushing mode, concise reference answers may be shown by default.
- If the user asks to hide answers, suppress answers for the current round.
- The user may later request the answer for a specific question.

## Scoring Framework

When the user submits an answer or code, evaluate concisely on:
- correctness
- edge cases
- code style
- time complexity
- space complexity
- interview communication

Record wrong or weak items into the module's wrong-question notebook when appropriate.

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
