# Python基础手写代码题

## 第一类：基础算法与数据结构

### 1. reverse_string
- tags: 字符串, 基础算法
- difficulty: easy
- frequency: 高频
- prompt: 手写一个函数，返回字符串逆序结果。
- answer: 可以用切片 `s[::-1]`，也可以用双指针从两端交换，考察字符串基础操作能力。

### 2. count_characters
- tags: 字符串, 统计
- difficulty: easy
- frequency: 高频
- prompt: 统计字符串中每个字符出现的次数。
- answer: 用字典逐个累加计数即可，考察遍历与字典使用。

### 3. dedup_list
- tags: 列表, 去重
- difficulty: easy
- frequency: 高频
- prompt: 对列表进行去重，保留原始顺序。
- answer: 可用集合辅助记录已见元素，同时遍历原列表构造新列表。

### 4. merge_sorted_lists
- tags: 列表, 双指针
- difficulty: easy
- frequency: 高频
- prompt: 合并两个有序列表，返回一个新的有序列表。
- answer: 使用双指针依次比较两个列表元素，较小者进入结果列表。

### 5. sort_dict_by_value
- tags: 字典, 排序
- difficulty: medium
- frequency: 高频
- prompt: 手写一个函数，按字典的 value 对其排序。
- answer: 使用 `sorted(dict.items(), key=lambda x: x[1])`，再按需要转回字典。

### 6. binary_search
- tags: 二分查找, 基础算法
- difficulty: medium
- frequency: 高频
- prompt: 在有序列表中查找目标值，返回下标，不存在返回 -1。
- answer: 左右指针不断折半，比较中间值和目标值，直到找到或区间为空。

### 7. bubble_sort
- tags: 排序, 基础算法
- difficulty: medium
- frequency: 中高频
- prompt: 手写冒泡排序。
- answer: 双层循环，两两比较并交换，适合说明排序基础思想。

### 8. quick_sort
- tags: 排序, 递归
- difficulty: medium
- frequency: 中高频
- prompt: 手写快速排序。
- answer: 选取基准值，分成左右两部分递归排序后合并。

### 9. fibonacci
- tags: 递归, 动态规划基础
- difficulty: easy
- frequency: 高频
- prompt: 生成斐波那契数列第 n 项。
- answer: 可用递归、循环或动态规划，面试中更推荐迭代写法。

### 10. two_sum
- tags: 哈希, 基础算法
- difficulty: easy
- frequency: 高频
- prompt: 在列表中找到和为目标值的两个数下标。
- answer: 用哈希表记录已访问元素，当前值的补数如果已出现就直接返回。

### 11. valid_parentheses
- tags: 栈, 字符串
- difficulty: easy
- frequency: 高频
- prompt: 判断括号字符串是否有效。
- answer: 用栈保存左括号，遇到右括号时检查是否匹配，最后栈为空则有效。

### 12. longest_substring_without_repeat
- tags: 字符串, 滑动窗口
- difficulty: medium
- frequency: 中高频
- prompt: 求不含重复字符的最长子串长度。
- answer: 用滑动窗口维护当前无重复区间，遇到重复字符时收缩左边界。

## 第二类：Python 高级特性应用

### 13. retry_decorator
- tags: 装饰器, 重试, 高级特性
- difficulty: medium
- frequency: 高频
- prompt: 手写一个失败重试装饰器，支持指定重试次数和间隔。
- answer: 用装饰器包装原函数，在异常时捕获并重试，成功后直接返回结果，失败超过次数则抛出异常。

### 14. singleton
- tags: 单例模式, 设计模式
- difficulty: medium
- frequency: 中高频
- prompt: 手写一个单例模式，适合配置类或数据库连接池。
- answer: 可用类变量缓存实例，也可用装饰器或元类实现，核心是保证整个进程中只创建一个对象实例。

### 15. context_manager
- tags: 上下文管理器, with语句
- difficulty: medium
- frequency: 高频
- prompt: 手写一个自定义上下文管理器。
- answer: 实现 `__enter__` 和 `__exit__` 方法即可，`with` 语句会自动调用进入和退出逻辑，适合资源管理。

### 16. timer_decorator
- tags: 装饰器, 性能统计
- difficulty: easy
- frequency: 中高频
- prompt: 手写一个函数执行时间统计装饰器。
- answer: 在调用前后记录时间戳，计算耗时后打印或上报日志。

### 17. memoize
- tags: 装饰器, 缓存
- difficulty: medium
- frequency: 加分题
- prompt: 手写一个函数缓存装饰器。
- answer: 用字典缓存参数到结果的映射，重复调用时直接返回缓存值。

## 第三类：自动化测试核心组件封装

### 18. requests_wrapper
- tags: Requests, 接口测试, Token管理
- difficulty: hard
- frequency: 高频
- prompt: 手写一个 Requests 二次封装类，支持自动附带 Token。
- answer: 在封装类中持有 session、base_url 和 token，请求前统一拼接请求头、自动带 Token，并提供 get/post 等基础方法。

### 19. request_base_client
- tags: Requests, 公共封装
- difficulty: hard
- frequency: 高频
- prompt: 手写一个公共请求基类，统一处理 base_url、headers、日志和异常。
- answer: 把请求前公共逻辑、请求后结果解析、异常处理和日志打印都封到一个基类中，让业务接口只关心参数和断言。

### 20. data_driver
- tags: Excel, YAML, 数据驱动
- difficulty: medium
- frequency: 高频
- prompt: 手写一个 Excel / YAML 数据驱动解析工具。
- answer: 读取 Excel 或 YAML 的测试数据，统一转换成标准结构，再供测试框架参数化调用。

### 21. logger_wrapper
- tags: 日志, 工具封装
- difficulty: medium
- frequency: 中高频
- prompt: 手写一个日志封装类，支持控制台和文件输出。
- answer: 封装 logger、handler、formatter，保证全项目日志格式统一并避免重复初始化。

### 22. config_loader
- tags: 配置管理, YAML
- difficulty: medium
- frequency: 中高频
- prompt: 手写一个配置读取工具，支持按环境加载 YAML 配置。
- answer: 读取配置文件后按环境键选择对应配置，并封装成统一访问接口。

### 23. assert_helper
- tags: 断言, 工具封装
- difficulty: medium
- frequency: 高频
- prompt: 手写一个统一断言工具类。
- answer: 封装状态码断言、字段断言、包含断言和数据库结果断言，提升接口测试代码复用率。

## 第四类：数据库与数据校验

### 24. mysql_assert
- tags: MySQL, 数据库断言
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个 MySQL 查询与断言工具类。
- answer: 封装连接、查询、结果转换和断言方法，支持按 SQL 取数后与预期结果比较。

### 25. redis_client_wrapper
- tags: Redis, 缓存, 工具封装
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个 Redis 连接封装类。
- answer: 把连接、读写、过期时间、异常处理封装成统一接口，方便测试脚本直接调用。

### 26. db_result_compare
- tags: SQL, 数据校验
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个接口结果与数据库结果比对工具。
- answer: 封装字段映射、结果读取和逐字段比较逻辑，用于接口自动化后的数据库校验。

## 第五类：UI 自动化封装

### 27. smart_wait
- tags: Selenium, Playwright, 显式等待, UI自动化
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个显式等待/智能等待封装。
- answer: 封装轮询等待逻辑，在超时时间内不断检查元素是否出现、可见或可点击，直到成功或超时。

### 28. base_page
- tags: UI自动化, 页面对象模型
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个 BasePage 基类封装。
- answer: 把元素查找、点击、输入、等待、截图等通用操作统一封装，页面类继承后复用。

### 29. click_with_retry
- tags: UI自动化, 重试
- difficulty: medium
- frequency: 加分题
- prompt: 手写一个带重试能力的点击封装。
- answer: 在点击失败时捕获异常、重新定位元素并按设定次数重试，同时记录日志。

## 第六类：工程化与辅助脚本

### 30. log_scan_script
- tags: Linux, 日志排查, 辅助脚本
- difficulty: medium
- frequency: 加分题
- prompt: 手写一个日志扫描脚本，统计错误关键字出现次数。
- answer: 读取日志文件逐行扫描，用字典统计关键字匹配次数，并输出汇总结果。
