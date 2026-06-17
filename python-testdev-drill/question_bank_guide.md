# System Question Bank Guide

本文件定义 `python-testdev-drill` 的系统题库组织方式。

## 模块

### 1. Python基础手写代码题
适合刷手写代码、基础算法、常见数据结构处理。

推荐标签：
- string
- list
- dict
- set
- two-pointers
- sorting
- stack
- queue
- hash
- dp-basic

### 2. Python编程基础理论面试题
适合理解 Python 语言机制与常见面试问答。

推荐标签：
- data-types
- copy
- decorator
- generator
- iterator
- closure
- gc
- gil
- coroutine
- exception
- oop

### 3. 自动化测试题
适合自动化测试实践与方法论。

推荐标签：
- case-design
- api-test
- ui-test
- mock
- pytest
- ci-cd
- flaky
- environment
- metrics

### 4. 测试开发面试题
适合测试开发平台设计、架构和工程能力。

推荐标签：
- platform-design
- scheduler
- report-system
- permission
- observability
- async
- concurrency
- db-modeling
- service-design

## 题目结构建议

每道系统题建议包含：
- id
- title
- prompt
- answer
- tags
- difficulty

## 抽题原则

- 默认优先抽当前模块未刷过题
- 再考虑未刷过的自建题
- 错题/收藏/自建模式使用对应专属题池
- 题目耗尽时必须显式提示用户
