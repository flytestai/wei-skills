# 自动化测试题

### 1. 如何设计接口测试用例
- tags: case-design, api-test
- difficulty: easy
- prompt: 设计接口测试用例时，一般要覆盖哪些维度？
- answer: 应覆盖正常流程、参数校验、边界值、异常场景、鉴权、幂等性、并发、数据一致性和性能基本观察等维度。

### 2. UI 自动化为什么容易 flaky
- tags: ui-test, flaky
- difficulty: easy
- prompt: UI 自动化测试为什么容易出现 flaky case？
- answer: 常见原因包括元素定位不稳定、页面异步加载、环境波动、测试数据污染、等待机制不合理、外部依赖不稳定等。

### 3. pytest fixture 有什么价值
- tags: pytest
- difficulty: easy
- prompt: pytest 的 fixture 解决了什么问题？
- answer: fixture 用于复用测试前置和资源初始化逻辑，支持作用域管理、依赖注入和 teardown，能显著降低重复代码。

### 4. mock 一般适合哪些场景
- tags: mock
- difficulty: medium
- prompt: 在自动化测试里，什么情况下适合使用 mock？
- answer: 当外部依赖不稳定、成本高、不可控或难以构造边界场景时适合 mock，例如第三方支付、短信、库存服务、超时异常等。

### 5. 如何衡量自动化测试价值
- tags: metrics, ci-cd
- difficulty: medium
- prompt: 你会用哪些指标衡量自动化测试体系的价值？
- answer: 可看覆盖率、缺陷拦截率、回归耗时、稳定性（flaky 比例）、失败定位成本、CI 成功率、关键链路保护效果等。
