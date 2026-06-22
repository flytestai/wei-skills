# Pytest框架

## 第一类：Pytest 基础高频题

### 1. fixture_basic
- tags: Pytest, fixture, 基础
- difficulty: easy
- frequency: 高频
- prompt: Pytest 里的 fixture 是什么？它主要解决什么问题？
- answer: fixture 本质上是 Pytest 提供的一种测试前置资源管理机制。它可以把初始化、清理、依赖注入这些公共逻辑抽出来复用，避免每个测试函数都重复写 setup 代码。面试里可以强调三点：第一，提升复用性；第二，让测试依赖更清晰；第三，天然支持作用域和组合，适合管理浏览器、数据库连接、登录态、测试数据等资源。

### 2. fixture_vs_setup
- tags: Pytest, fixture, setup
- difficulty: easy
- frequency: 高频
- prompt: Pytest 的 fixture 和 setup/teardown 有什么区别？
- answer: 口语化来说，setup/teardown 更像是传统生命周期钩子，能做前后处理，但复用性和依赖表达能力比较弱；fixture 更灵活，既能做初始化和清理，又能通过参数注入给测试函数，还支持作用域、依赖链和自动使用。真实项目里一般优先用 fixture，因为它更适合工程化组织测试资源。

### 3. conftest_role
- tags: Pytest, conftest, 组织结构
- difficulty: easy
- frequency: 高频
- prompt: `conftest.py` 的作用是什么？为什么很多项目都会用它？
- answer: `conftest.py` 可以理解成 Pytest 的本地共享配置入口。常见用途是放公共 fixture、hook、marker 注册、前置处理逻辑等。它的好处是不用显式 import，Pytest 会按目录层级自动发现，所以很适合做测试目录下的公共能力沉淀。

### 4. fixture_scope
- tags: Pytest, fixture, scope
- difficulty: medium
- frequency: 高频
- prompt: Pytest 的 fixture scope 有哪些？分别适合什么场景？
- answer: 常见 scope 有 `function`、`class`、`module`、`package`、`session`。`function` 是每条用例都执行一次，最隔离；`class` 适合同一个测试类共用资源；`module` 适合同一个文件共用；`session` 适合全局只创建一次的重资源，比如浏览器驱动、数据库连接池、测试环境初始化。面试时最好补一句：scope 越大，执行越快，但资源隔离越弱，要在性能和独立性之间做平衡。

### 5. fixture_autouse
- tags: Pytest, fixture, autouse
- difficulty: medium
- frequency: 高频
- prompt: `autouse=True` 的 fixture 有什么作用？使用时要注意什么？
- answer: `autouse=True` 表示不用在测试函数参数里显式声明，这个 fixture 也会自动生效。适合做全局日志、环境初始化、统一清理这类“所有测试都要用”的动作。但要注意别滥用，因为 autouse 太多会让依赖关系变隐式，别人看测试函数时不知道背后做了哪些前置逻辑，排查问题会更难。

### 6. parametrize_basic
- tags: Pytest, 参数化, 高频
- difficulty: easy
- frequency: 高频
- prompt: `@pytest.mark.parametrize` 的作用是什么？常见使用场景有哪些？
- answer: 它的核心作用是一套测试逻辑跑多组输入数据。最常见场景有接口参数校验、边界值测试、等价类覆盖、异常输入覆盖。面试里可以强调：参数化能减少重复代码，让测试结构更紧凑，也更适合配合数据驱动做批量验证。

### 7. skip_xfail
- tags: Pytest, skip, xfail
- difficulty: medium
- frequency: 高频
- prompt: `skip`、`skipif`、`xfail` 分别是什么？它们的区别是什么？
- answer: `skip` 是直接跳过；`skipif` 是满足条件时跳过，比如平台不兼容；`xfail` 是“预期失败”，意思是这个问题当前已知会失败，但先保留测试。三者的核心区别是语义不同：skip 是不执行，xfail 是执行但失败可接受。项目里用 xfail 往往能体现你对已知缺陷和测试管理的理解。

### 8. mark_usage
- tags: Pytest, mark, 标签
- difficulty: medium
- frequency: 高频
- prompt: Pytest 的 mark 有什么用？你在项目里一般怎么用？
- answer: mark 就是给测试打标签，便于分类、筛选和控制执行。比如可以按 `smoke`、`regression`、`api`、`ui`、`slow` 分组，再配合 `-m` 做选择性运行。项目里常见用法就是把冒烟、回归、核心链路、慢用例分开，支撑 CI 分层执行。

## 第二类：Pytest 工程化常考题

### 9. pytest_ini
- tags: Pytest, pytest.ini, 配置
- difficulty: medium
- frequency: 中高频
- prompt: `pytest.ini` 一般用来做什么配置？
- answer: `pytest.ini` 是 Pytest 的项目级配置文件，常见放 marker 注册、默认命令参数、测试目录、文件命名规则、日志配置、过滤 warning 等。它的价值在于把运行规范固化到项目里，避免每个人本地执行方式不一致。

### 10. collection_rules
- tags: Pytest, 测试收集, 规则
- difficulty: medium
- frequency: 中高频
- prompt: Pytest 默认是怎么发现和收集测试用例的？
- answer: 默认会按命名规则收集，比如文件一般是 `test_*.py` 或 `*_test.py`，类一般以 `Test` 开头，函数一般以 `test_` 开头。面试时可以补一句：这些规则也可以通过配置调整，所以项目里最好统一约定命名规范，避免漏收或误收。

### 11. fixture_dependency
- tags: Pytest, fixture, 依赖注入
- difficulty: medium
- frequency: 中高频
- prompt: fixture 之间可以互相依赖吗？这种设计有什么好处？
- answer: 可以。一个 fixture 可以把另一个 fixture 作为参数，这本质上就是依赖注入。好处是资源可以分层拆分，比如先建数据库连接，再基于连接创建测试用户，再基于用户生成登录态。这样逻辑更清晰，也更容易复用和维护。

### 12. yield_fixture_cleanup
- tags: Pytest, fixture, 清理
- difficulty: medium
- frequency: 中高频
- prompt: 为什么很多人会在 fixture 里用 `yield`？
- answer: 因为 `yield` 前面可以写初始化逻辑，后面可以写清理逻辑，这样一个 fixture 就同时承担了 setup 和 teardown。相比手动分散写清理逻辑，`yield` 更集中、更不容易漏，特别适合文件、连接、浏览器、临时数据这类有生命周期的资源。

### 13. plugin_ecosystem
- tags: Pytest, 插件, 工程化
- difficulty: medium
- frequency: 中高频
- prompt: 你常用过哪些 Pytest 插件？它们分别解决什么问题？
- answer: 比较常见的有 `pytest-xdist` 做并发执行，`pytest-rerunfailures` 做失败重跑，`allure-pytest` 做报告，`pytest-order` 控制执行顺序，`pytest-assume` 做软断言。回答时别只报名字，最好顺手说清楚它们解决的是执行效率、稳定性、可观测性还是组织控制问题。

### 14. hook_basic
- tags: Pytest, hook, 插件机制
- difficulty: hard
- frequency: 中高频
- prompt: Pytest 的 hook 机制你怎么理解？
- answer: hook 可以理解成 Pytest 在执行生命周期里预留的扩展点。比如用例收集前后、执行前后、报告生成阶段，都可以通过 hook 插入自定义逻辑。它适合做结果增强、失败截图、日志补充、动态改报告、执行控制等。面试里不一定要背很多 hook 名字，但要说清楚：hook 本质是扩展执行流程的机制。

### 15. fixture_best_practice
- tags: Pytest, 最佳实践, 工程化
- difficulty: hard
- frequency: 加分题
- prompt: 在大型项目里设计 fixture 体系时，你觉得最容易踩的坑是什么？
- answer: 最常见的坑有三个：第一，fixture 过度耦合，依赖链太深；第二，scope 设太大导致用例相互污染；第三，autouse 滥用导致执行逻辑不透明。比较好的做法是：按资源层次拆分、明确命名、控制作用域、把公共能力沉淀到 `conftest.py`，同时减少隐式副作用。
