# 测试开发面试题

### 1. 如何设计自动化测试平台
- tags: platform-design, service-design
- difficulty: medium
- prompt: 如果让你设计一个自动化测试平台，你会拆哪些核心模块？
- answer: 通常会拆用例管理、任务编排/调度、执行引擎、环境管理、报告系统、权限体系、通知告警、数据看板等模块。

### 2. 测试任务调度系统要考虑什么
- tags: scheduler, concurrency
- difficulty: medium
- prompt: 设计测试任务调度系统时，要重点考虑哪些问题？
- answer: 要考虑任务队列、并发控制、资源隔离、失败重试、优先级、超时取消、执行日志和可观测性。

### 3. 测试报告系统怎么设计
- tags: report-system, observability
- difficulty: medium
- prompt: 测试报告系统除了展示结果，还应该具备哪些能力？
- answer: 还应具备趋势统计、失败归因、日志/截图挂载、步骤明细、过滤检索、分享权限和历史对比等能力。

### 4. 平台权限设计怎么做
- tags: permission, service-design
- difficulty: medium
- prompt: 测试平台的权限设计一般如何做？
- answer: 常见做法是 RBAC，区分角色、资源、操作粒度，并结合项目/环境/数据范围控制，避免全局超权。

### 5. 为什么测试开发也要关注可观测性
- tags: observability, platform-design
- difficulty: medium
- prompt: 测试开发平台里为什么要关注日志、指标、链路等可观测性？
- answer: 因为平台问题往往不是“执行失败”这么简单，可观测性帮助快速定位是用例问题、环境问题、调度问题还是外部依赖问题。
