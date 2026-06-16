---
name: python-testdev-drill
description: Reusable module-based drill workflow for Python test-development engineer interview practice, with isolated progress, non-repeating questions, scoring, mistake tracking, and persistent module state.
---

# Python TestDev Drill

## Purpose

Provide a reusable practice workflow for Python test-development engineer interview preparation.

This skill is a module-based drill engine rather than a single question list. It supports multiple independent tracks, keeps state for each track, and resumes from saved progress on demand.

## Use This Skill When

Use this skill when the user wants to:
- practice Python coding questions one by one
- continue from prior progress without restarting
- separate practice into different modules
- request direct answers for selected questions
- maintain isolated mistake notebooks by module
- avoid repeated questions inside a module

## Core Behavior

- Ask exactly one question at a time.
- Default to not revealing the answer.
- After the user submits code, evaluate before moving on.
- If the user says `给出答案`, provide the answer directly and add the current question to the current module's mistake notebook.
- If the user says `继续`, resume from the current module's saved `next_question`.
- If the user explicitly names a module, switch to that module and resume from its saved state.

## Module Rules

A module is an isolated practice track. Each module must maintain its own persistent state and must not share progress with other modules.

Each module keeps:
- module name
- ordered question bank
- asked question history
- next question pointer
- mistake notebook
- answer-given history

## Non-Repetition Rules

Inside the same module:
- do not repeat a question that has already been asked
- do not repeat a question that has already been answered directly
- when the question bank grows, always prefer unseen questions first
- if unseen questions are exhausted, explicitly tell the user instead of silently repeating content

## Interaction Patterns

### Start a module
Examples:
- `开始 Python基础手写代码题`
- `开始 自动化测试题`
- `开始 测试开发面试题`

Behavior:
- create the module state if missing
- start from question 1 or the first unseen question

### Continue a module
Examples:
- `继续 Python基础手写代码题`
- `继续`

Behavior:
- resume from the saved `next_question`

### Submit an answer
Behavior:
- score on correctness, edge cases, code style, time complexity, space complexity, and interview communication
- point out the main issue first
- if acceptable, move to the next question

### Request the answer
Examples:
- `给出答案`
- `直接给答案`

Behavior:
- provide a concise standard answer
- add the current question to the current module's mistake notebook
- advance progress to the next unseen question

### Review mistakes
Examples:
- `查看 Python基础手写代码题错题集`
- `复盘 自动化测试题`

Behavior:
- show only that module's mistake notebook
- do not mix mistakes across modules

## Scoring Framework

Evaluate submitted code using these dimensions:
- correctness
- edge cases
- code style
- time complexity
- space complexity
- interview communication

Keep feedback concise and prioritize the most important fix first.

## Bundled Resources

- `state.md`: current persisted module state snapshot
- `MODULES.md`: module contract and expansion rules
- `QUESTION_BANK_GUIDE.md`: question-bank organization guidance

## Current Seed Modules

- Python基础手写代码题
- 自动化测试题
- 测试开发面试题
