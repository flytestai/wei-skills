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
- tags: Pytest, fixture, 最佳实践
- difficulty: medium
- frequency: 中高频
- prompt: fixture 使用上有哪些最佳实践？
- answer: 核心几条：命名用「动作/状态」而非「数据名」，比如 `clean_db` 比 `db` 清晰；能复用的一律放 conftest.py，避免跨文件 import；scope 往大放（能用 session 不用 function），但要确认测试之间没有副作用污染；清理逻辑放 yield 之后而不是每个用例自己删。收尾可以提一句：fixture 是 Pytest 的灵魂，用好了用例干净、用烂了比 setup/tearDown 还难维护，关键就在「谁依赖谁、什么时候清理」想清楚。

### 16. conftest_role_advanced
- tags: Pytest, conftest, 工程化
- difficulty: hard
- frequency: 加分题
- prompt: 多个目录都有 conftest.py 时，fixture 怎么生效？
- answer: conftest.py 的作用域是「它所在的目录及其子目录」，不需要 import 就能被范围内的用例使用。多个 conftest 是叠加关系：子目录的 conftest 补充（而不是覆盖）父目录的，用例能同时用到整条目录链上的所有 fixture。这个特性常用来分层：根 conftest 放全局配置（环境地址、driver），api/ 目录放接口测试专用 fixture，ui/ 目录放登录态、浏览器 fixture，互不干扰。再深一层：根 conftest 里可以定义 hook（如 pytest_addoption 加命令行参数）让全局生效。答出「就近叠加 + 分层设计」就到位了。

### 17. fixture_override_resolution
- tags: Pytest, fixture, 进阶
- difficulty: hard
- frequency: 加分题
- prompt: 父目录和子目录定义了同名 fixture，用例用的是哪个？
- answer: 规则是「就近覆盖」：离用例越近的定义优先，子目录 conftest 的同名 fixture 会覆盖父目录的，用例文件里定义的又覆盖 conftest 的。另一个维度是参数化覆盖：用例上 `@pytest.mark.usefixtures` 显式指定、或 fixture 通过 `request.getfixturevalue` 动态取，都能改变解析结果。这个机制的典型用法是「默认实现 + 特殊目录覆盖」：根 conftest 定义 `base_url` 指向测试环境，某个调试目录覆盖成 localhost。回答时强调一句：同名覆盖是隐式的，团队协作里建议用不同名字或参数化来表达差异，可读性更好。

### 18. pytest_generate_tests
- tags: Pytest, hook, 参数化
- difficulty: hard
- frequency: 加分题
- prompt: 除了 @pytest.mark.parametrize，还有什么动态参数化的方式？
- answer: 有，`pytest_generate_tests` 这个收集期 hook。它在用例收集阶段被调用，能在代码里读文件、查数据库、按环境变量动态算出参数，然后 `metafunc.parametrize("case", data)` 注入。和 parametrize 装饰器的区别：装饰器的参数是写死在代码里的静态列表，hook 是运行收集时才生成的动态数据。典型场景：用例数据全部外置到 Excel/YAML，测试函数只有一行，参数由 hook 读文件灌进去——数据驱动框架的标准做法。再补一句：hook 在收集期跑，所以别在里面做太重的操作，会影响整个收集速度。

### 19. pytest_allure_integration
- tags: Pytest, allure, 报告
- difficulty: medium
- frequency: 中高频
- prompt: Pytest 怎么集成 Allure 报告？常用能力有哪些？
- answer: 集成两步：装 `allure-pytest` 插件，跑测试时加 `--alluredir=result` 参数生成原始结果目录，再用 allure 命令行工具 `allure serve result` 渲染成网页报告。常用能力记四个：`@allure.feature/@allure.story` 给用例分层打标，报告按业务模块树状展示；`allure.attach` 附加文件（截图、接口响应），失败排查全靠它；`with allure.step("步骤")` 记录执行步骤；severity 标记优先级。面试加分点：说清楚 CI 里怎么串——pytest 产结果目录，Jenkins/GitLab CI 装 Allure 插件出趋势图，每次构建对比通过率变化。

### 20. pytest_xdist_precautions
- tags: Pytest, xdist, 并发
- difficulty: hard
- frequency: 中高频
- prompt: 用 pytest-xdist 并发跑用例，有哪些坑要注意？
- answer: 坑集中在三点。第一，用例必须无序无状态：xdist 把用例打散到多个 worker，谁先谁后不确定，用例间共享可变全局变量、依赖执行顺序的写法必然翻车。第二，fixture 作用域被打破：session 级 fixture 在每个 worker 进程里都会执行一次，比如 session 级建数据库连接，8 个 worker 就是 8 条连接，初始化逻辑要想清楚放哪。第三，报告和资源竞争：同一个文件被多个 worker 同时写要加锁或用临时目录，登录态要每个 worker 各自获取。收尾给方案：`-n auto` 按核数跑、配 `--dist=loadscope` 让同模块/同类的用例落同一 worker，能规避一部分顺序问题。

