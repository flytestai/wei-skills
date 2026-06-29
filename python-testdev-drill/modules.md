# Module Contract

## Purpose

This file defines how modules are created, expanded, and maintained inside `python-testdev-drill`.

## Required Module Fields

Each module must keep:
- `module_name`
- `completed_through`
- `next_question`
- `asked_questions`
- `mistakes`
- `answer_given_questions`
- `history_questions`
- `favorite_questions`
- `custom_questions`
- `current_mode`
- `current_batch_size`
- `last_round_questions`
- `last_round_results`

## Isolation Rules

- Progress is isolated by module.
- Mistakes are isolated by module.
- Asked-question history is isolated by module.
- Favorites are isolated by module.
- Custom banks are isolated by module.
- Switching modules must never overwrite another module's state.

## Expansion Rules

When a new module is added:
1. Assign a stable module name.
2. Create or attach an ordered question bank for that module.
3. Initialize empty progress, history, wrong, favorite, and custom-bank data.
4. Persist the module in `state.md`.

## Resume Rules

When the user names a module:
- load that module's state
- continue from `next_question` or the last drill mode
- preserve all other modules untouched

## Extraction Priority Rules

Default extraction priority inside a module:
1. 高频题（unseen first）
2. 中高频题（unseen first）
3. 加分题（unseen first）
4. unseen custom questions when applicable
5. optionally repeated questions only after user consent

For special modes:
- wrong mode → wrong-question bank first; if frequency info exists, still prefer 高频 within wrong questions
- favorites mode → favorites bank first; if frequency info exists, still prefer 高频 within favorites
- custom mode → custom-question bank first; if frequency info exists, still prefer 高频 within custom questions

## Active Modules

- `Python基础手写代码题`
- `Python编程基础理论面试题`
- `Python高阶编程`
- `自动化测试题`
- `Pytest框架`
- `测试开发面试题`
- `测试工程化与CI/CD`
- `性能测试面试题`
- `中间件面试题`
- `数据库面试题`

## Future Module Rule

Any newly created module must inherit the same routing rule:
- build high-frequency questions first
- then medium-high-frequency questions
- then bonus / differentiator questions

## History Rules

- every brushed question must be written into module history
- repeated extraction should be avoided when history already contains the question
- if all questions are exhausted, say so explicitly
