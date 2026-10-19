# Python基础手写代码题（上海中小厂测开 25K 定向版）

> 定位：中小厂测开/自动化岗白板手撕题。面试官爱考「字符串处理、列表字典操作、正则、日志文件分析、数据造数、Pytest 手写」，
> 不爱考 LeetCode Hard。答案现场口语化讲，代码求最简最好记。

## 第一类：字符串操作（中小厂第一高频）

### 1. reverse_string
- tags: 字符串, 高频
- difficulty: easy
- frequency: 高频
- prompt: 反转字符串。
- answer: 切片 s[::-1]，最简写法。

### 2. is_palindrome
- tags: 字符串, 高频
- difficulty: easy
- frequency: 高频
- prompt: 判断回文字符串（忽略大小写和非字母数字）。
- answer: 先 isalnum 过滤+lower，再和切片反转比较。

### 3. count_characters
- tags: 字符串, 高频
- difficulty: easy
- frequency: 高频
- prompt: 统计字符串中每个字符出现次数。
- answer: dict.get(ch, 0) + 1 逐个累加。

### 4. my_strip
- tags: 字符串, 真题
- difficulty: easy
- frequency: 高频
- prompt: 不用 strip，手写去掉字符串首尾空格。
- answer: 双指针从头尾找第一个非空格位置，再切片。

### 5. swap_case_string
- tags: 字符串, 真题
- difficulty: easy
- frequency: 高频
- prompt: 不用 swapcase，大小写互换。
- answer: 遍历 isupper/islower 判断转换。

### 6. compress_string
- tags: 字符串, 真题
- difficulty: medium
- frequency: 高频
- prompt: 字符串压缩：aaabcc -> a3b1c2。
- answer: 遍历比较相邻字符计数；循环外补最后一段。

### 7. longest_common_prefix
- tags: 字符串, 真题
- difficulty: medium
- frequency: 高频
- prompt: 求一组字符串的最长公共前缀。
- answer: 以第一个串为基准，逐个收缩。

### 8. my_index_of
- tags: 字符串, 真题
- difficulty: medium
- frequency: 高频
- prompt: 不用 find，返回子串首次出现的下标，没有返回 -1。
- answer: 遍历起点逐段比较；空子串返回 0。

### 9. longest_substring_without_repeat
- tags: 字符串, 滑动窗口
- difficulty: medium
- frequency: 中高频
- prompt: 最长无重复字符子串的长度。
- answer: 滑动窗口+字典记录字符最近位置。

### 10. word_frequency_in_file
- tags: 文件, 统计, 真题
- difficulty: easy
- frequency: 高频
- prompt: 统计文本文件中每个单词出现频率。
- answer: 逐行 split，字典累加；熟练的话提 Counter。

## 第二类：列表与字典（必考基础）

### 11. dedup_list
- tags: 列表, 高频
- difficulty: easy
- frequency: 高频
- prompt: 列表去重并保留原始顺序。
- answer: list(dict.fromkeys(nums))；坑：直接 set 会乱序。

### 12. find_duplicates
- tags: 列表, 哈希
- difficulty: easy
- frequency: 高频
- prompt: 找出列表中所有重复出现的元素。
- answer: 集合记录已见，再遇即重复；或 Counter 取次数>1。

### 13. sort_dict_by_value
- tags: 字典, 排序
- difficulty: easy
- frequency: 高频
- prompt: 按字典的 value 排序（降序）。
- answer: sorted(d.items(), key=lambda x: x[1], reverse=True)。

### 14. merge_sorted_lists
- tags: 列表, 双指针
- difficulty: easy
- frequency: 高频
- prompt: 合并两个有序列表为新的有序列表（不许拼接后 sort）。
- answer: 双指针比大小，最后 extend 接尾巴。

### 15. two_sum
- tags: 哈希, 高频
- difficulty: easy
- frequency: 高频
- prompt: 两数之和：返回和为 target 的两个数下标。
- answer: 字典存「值->下标」，查补数存自己；O(n)。

### 16. my_max
- tags: 基础, 真题
- difficulty: easy
- frequency: 中高频
- prompt: 不用内置 max，求列表最大值。
- answer: 遍历逐个比较更新。

### 17. swap_without_temp
- tags: 基础, 真题
- difficulty: easy
- frequency: 高频
- prompt: 不用中间变量交换两个变量的值。
- answer: a, b = b, a（元组解包）；底层先建临时元组。

### 18. append_vs_extend_trap
- tags: 列表, 易错点
- difficulty: easy
- frequency: 中高频
- prompt: 手写演示 append 和 extend 的区别（含传字符串的坑）。
- answer: append 整体进，extend 拆散进；extend("abc") 会拆成三个字符。

### 19. remove_consecutive_duplicates
- tags: 列表, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 移除列表连续重复元素只留一个：[1,2,2,3,3,3,2,2] -> [1,2,3,2]。
- answer: 和前一个元素比较，不同才保留。

### 20. flatten_nested_list
- tags: 列表, 递归
- difficulty: medium
- frequency: 中高频
- prompt: 把任意深度嵌套的列表拍平成一维。
- answer: 递归：是 list 就递归展开，否则收集。

## 第三类：正则表达式（测开特色，中小厂爱考）

### 21. regex_valid_phone
- tags: 正则, 参数校验, 真题
- difficulty: easy
- frequency: 高频
- prompt: 正则验证 11 位手机号（1 开头，第二位 3-9）。
- answer: re.match(r"^1[3-9]\d{9}$", phone)。

### 22. mask_phone
- tags: 正则, 数据脱敏, 真题
- difficulty: easy
- frequency: 高频
- prompt: 手机号中间 4 位打星：13800138000 -> 138****8000。
- answer: re.sub 分组捕获，r"(\d{3})\d{4}(\d{4})" -> r"\1****\2"。

### 23. regex_extract_email
- tags: 正则, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 正则提取文本中所有邮箱。
- answer: re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)。

### 24. regex_split_string
- tags: 正则, 真题
- difficulty: medium
- frequency: 高频
- prompt: "info:xiaoZhang 33 shandong" 用正则切成 4 段。
- answer: re.split(r":|\s+", s)，多分隔符用 | 合并。

### 25. regex_extract_json_field
- tags: 正则, 日志, 真题
- difficulty: medium
- frequency: 高频
- prompt: 从日志行 "resp={\"code\":0,\"msg\":\"ok\"}" 中提取 code 的值。
- answer: re.search(r'"code":(\d+)', line).group(1)；日志解析常用。

## 第四类：文件与日志分析（测开最有辨识度的题）

### 26. count_file_lines
- tags: 文件, 内存优化
- difficulty: easy
- frequency: 中高频
- prompt: 统计超大日志文件行数，不许整个读进内存。
- answer: for line in f 逐行迭代计数，内存恒定。

### 27. walk_folder
- tags: os, 文件遍历
- difficulty: easy
- frequency: 高频
- prompt: 遍历文件夹及所有子文件夹打印文件路径。
- answer: os.walk 三元组循环。

### 28. log_level_stats
- tags: 日志分析, 真题
- difficulty: medium
- frequency: 高频
- prompt: 日志每行「时间 级别 消息」，统计各级别出现次数按降序。
- answer: 逐行 split 取级别，Counter 统计，most_common 排序；脏行 try 跳过。

### 29. slow_api_top5
- tags: 日志分析, 排序, 真题
- difficulty: medium
- frequency: 高频
- prompt: 日志每行「[时间][接口][耗时ms]」，统计耗时>1000ms 的接口 Top5。
- answer: 解析+Counter+most_common(5)；考格式容错。

### 30. grep_keyword_in_log
- tags: 日志, 真题
- difficulty: easy
- frequency: 高频
- prompt: 在日志文件里找出所有包含 "ERROR" 的行及行号。
- answer: enumerate 逐行判断关键字；考察基础文件读取。

### 31. dir_stat_by_ext
- tags: 文件, 统计
- difficulty: medium
- frequency: 中高频
- prompt: 统计目录下各扩展名文件数量 {.py: 10, .log: 3}。
- answer: os.walk + splitext + 字典累加。

## 第五类：CSV/JSON 与数据驱动（接口自动化地基）

### 32. csv_to_dicts
- tags: CSV, 数据驱动
- difficulty: easy
- frequency: 高频
- prompt: 读 CSV 每行转字典（首行表头），返回字典列表。
- answer: csv.DictReader 一行；参数化数据驱动的地基。

### 33. json_extract_fields
- tags: JSON, 接口测试
- difficulty: easy
- frequency: 高频
- prompt: 从接口返回的订单列表 JSON 提取所有订单号。
- answer: 列表推导式 [item["order_id"] for item in data]。

### 34. json_flatten
- tags: JSON, 递归
- difficulty: medium
- frequency: 中高频
- prompt: 嵌套 JSON 扁平化：{a:{b:1}} -> {"a.b":1}。
- answer: 递归带父路径下钻；全字段断言的基础。

### 35. compare_json_equal
- tags: JSON, 断言
- difficulty: medium
- frequency: 中高频
- prompt: 判断两个 JSON 是否相等（忽略键顺序，可选忽略列表顺序）。
- answer: dict 直接 == 天然忽略键序；列表顺序敏感时先排序。

### 36. render_template_vars
- tags: 接口关联, 框架核心
- difficulty: medium
- frequency: 高频
- prompt: 把请求数据里的 ${token} 占位符替换成上下文中的值（支持嵌套 dict/list 递归）。
- answer: re.sub 回调查字典；类型分流递归。接口关联核心。

### 37. yaml_case_loader
- tags: YAML, 数据驱动
- difficulty: easy
- frequency: 中高频
- prompt: 读取 YAML 测试用例文件返回列表（文件不存在给清晰报错）。
- answer: yaml.safe_load + utf-8 + FileNotFoundError 防御；坑：必须 safe_load。

## 第六类：Python 特性（装饰器/生成器/闭包）

### 38. retry_decorator
- tags: 装饰器, 高频
- difficulty: medium
- frequency: 高频
- prompt: 手写失败重试装饰器，支持重试次数和间隔。
- answer: 装饰器包 try，异常重试，超次 raise；记得 @wraps 和 return 结果。

### 39. timer_decorator
- tags: 装饰器
- difficulty: easy
- frequency: 高频
- prompt: 函数执行耗时统计装饰器。
- answer: 前后 time.time() 差值；坑：忘 @wraps、忘 return result。

### 40. memoize
- tags: 装饰器, 缓存
- difficulty: medium
- frequency: 中高频
- prompt: 函数结果缓存装饰器，相同参数直接返缓存。
- answer: 闭包字典，key=(args, tuple(sorted(kwargs.items())))；提 lru_cache 加分。

### 41. context_manager
- tags: 上下文管理器
- difficulty: medium
- frequency: 高频
- prompt: 手写自定义上下文管理器（with 语句）。
- answer: 实现 __enter__/__exit__；或 @contextmanager+yield。

### 42. read_big_file_generator
- tags: 生成器, 内存优化
- difficulty: easy
- frequency: 高频
- prompt: 用生成器逐行读取大文件（内存友好）。
- answer: yield 每行；解释惰性求值省内存。

### 43. fibonacci_iter
- tags: 迭代
- difficulty: easy
- frequency: 高频
- prompt: 斐波那契第 n 项（禁裸递归）。
- answer: a, b = b, a+b 迭代；裸递归 O(2^n) 是坑。

### 44. multiply_closure
- tags: 闭包
- difficulty: medium
- frequency: 中高频
- prompt: 函数接收 n，返回把参数乘 n 的新函数。
- answer: 外层记 n，内层返回 param*n；闭包经典。

## 第七类：排序与查找基础（只考最经典的）

### 45. bubble_sort
- tags: 排序
- difficulty: medium
- frequency: 中高频
- prompt: 手写冒泡排序。
- answer: 双层循环两两交换，每轮把最大冒到末尾。

### 46. quick_sort
- tags: 排序, 递归
- difficulty: medium
- frequency: 中高频
- prompt: 手写快速排序。
- answer: 选基准分左右递归合并；列表推导式版最易记。

### 47. binary_search
- tags: 二分查找
- difficulty: medium
- frequency: 高频
- prompt: 有序列表查找目标值下标，没有返回 -1。
- answer: left<=right，mid=(l+r)//2，mid±1 更新；坑：死循环和边界。

### 48. valid_parentheses
- tags: 栈, 高频
- difficulty: easy
- frequency: 高频
- prompt: 判断括号串是否合法闭合。
- answer: 左括号进栈，右括号查表弹栈，最后栈空；坑：空栈 pop 和残留左括号。

### 49. my_sqrt
- tags: 二分, 数学
- difficulty: easy
- frequency: 中高频
- prompt: 不用库函数求整数 x 的平方根（向下取整）。
- answer: 二分答案，mid*mid <= x 的最大 mid。

### 50. climb_stairs_dp
- tags: 动态规划
- difficulty: easy
- frequency: 中高频
- prompt: 爬楼梯：每次 1 或 2 阶，n 阶有几种爬法。
- answer: f(n)=f(n-1)+f(n-2) 滚动变量；本质斐波那契。

## 第八类：测试数据造数（测开专属高频）

### 51. generate_phone
- tags: 造数, 真题
- difficulty: easy
- frequency: 高频
- prompt: 生成一个随机合法测试手机号。
- answer: 号段池随机选前缀+random 后 8 位。

### 52. gen_random_users
- tags: 造数
- difficulty: medium
- frequency: 中高频
- prompt: 批量生成 N 条随机用户数据（姓名/邮箱/手机号）。
- answer: 姓+名字池随机组合，邮箱加时间戳后缀保唯一。

### 53. id_card_valid
- tags: 校验算法, 加分
- difficulty: medium
- frequency: 加分题
- prompt: 校验 18 位身份证合法性（日期+末位校验码）。
- answer: 前 17 位加权因子 (2^i % 11) 求和 mod 11 查校验表；日期用 datetime 验证。

### 54. timestamp_converter
- tags: datetime, 真题
- difficulty: easy
- frequency: 高频
- prompt: 时间戳与 "2024-01-01 12:00:00" 格式互转。
- answer: fromtimestamp+strftime / strptime+timestamp；测开日常必备。

### 55. n_days_later_date
- tags: datetime
- difficulty: medium
- frequency: 加分题
- prompt: 输入 20190530 和 N，输出 N 天后的日期字符串。
- answer: strptime 解析 + timedelta(N) + strftime 输出。

## 第九类：Pytest 手写（测开岗必考环节）

### 56. pytest_basic_test
- tags: pytest, 必考
- difficulty: easy
- frequency: 高频
- prompt: 手写最简单的 pytest 用例测 add(a,b)（注意命名规范）。
- answer: test_ 文件+test_ 函数+assert；讲清默认收集规则。

### 57. pytest_parametrize
- tags: pytest, 必考
- difficulty: easy
- frequency: 高频
- prompt: pytest 参数化让一个函数跑多组输入 (1,2,3)、(0,0,0)、(-1,1,0)。
- answer: @pytest.mark.parametrize("a,b,expected", [...])；配合 ids 显示用例名。

### 58. pytest_fixture_yield
- tags: pytest, fixture, 必考
- difficulty: medium
- frequency: 高频
- prompt: 手写带 setup/teardown 的 fixture（如数据库连接建与关）。
- answer: yield 前是 setup 后是 teardown；提 scope 参数加分。

### 59. pytest_raises
- tags: pytest, 异常
- difficulty: easy
- frequency: 中高频
- prompt: 测试函数非法输入时抛指定异常（如除零）。
- answer: with pytest.raises(ZeroDivisionError): 负向用例标准写法。

### 60. mock_patch_api
- tags: mock, 必考
- difficulty: medium
- frequency: 高频
- prompt: 用 mock.patch 模拟外部 HTTP 调用让测试不打真实网络。
- answer: patch("模块名.requests.get")，坑：patch 使用处不是定义处。

### 61. monkeypatch_simple
- tags: pytest, mock
- difficulty: medium
- frequency: 中高频
- prompt: 用 pytest 的 monkeypatch 替换函数依赖。
- answer: monkeypatch.setattr(模块, "函数名", 假函数)，自动还原。

## 第十类：并发与网络（25K 档位加分项）

### 62. concurrent_requests
- tags: 多线程, 接口并发
- difficulty: medium
- frequency: 中高频
- prompt: 线程池并发请求多个 URL，收集状态码和耗时。
- answer: ThreadPoolExecutor.map + requests；记录 start/end。

### 63. simple_http_client
- tags: requests, 封装
- difficulty: medium
- frequency: 高频
- prompt: 封装一个 ApiClient：base_url 拼接 + Session 复用 + Token 自动注入。
- answer: session.headers.update 挂 Token，request 统一分发；讲连接池复用。

### 64. response_time_stat
- tags: 统计, 性能
- difficulty: medium
- frequency: 中高频
- prompt: 给一批接口响应时间，算平均、中位数、P95。
- answer: 排序取位置：中位数中间值，P95 取 95% 位置；性能报告基础。

### 65. first_unique_char
- tags: 字符串, 哈希, 真题
- difficulty: easy
- frequency: 高频
- prompt: 找字符串中第一个只出现一次的字符，没有返回空。
- answer: Counter 统计后遍历找第一个次数为 1 的；或字典两遍扫描。

### 66. valid_ipv4
- tags: 字符串, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 判断字符串是否是合法点分十进制 IPv4（如 192.168.1.1）。
- answer: split('.') 拆四段，每段 isdigit、0-255、非 0 开头（除单独 0）；测开笔试真题。

### 67. reverse_words
- tags: 字符串, 真题
- difficulty: easy
- frequency: 高频
- prompt: "the sky is blue" -> "blue is sky the"（单词内部不反转）。
- answer: split + 切片反转 + join：' '.join(s.split()[::-1])。

### 68. second_max
- tags: 列表, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 找列表中第二大的数（不许排序）。
- answer: 一次遍历维护 first/second 两个变量；坑：重复最大值和初始化。

### 69. char_freq_sort
- tags: 哈希, 排序, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 统计列表中每个元素出现次数并按次数降序输出。
- answer: Counter + most_common；或字典统计+sorted(key=lambda)。

### 70. find_topk
- tags: 堆, TopK, 真题
- difficulty: medium
- frequency: 高频
- prompt: 100 万个数里找最大的 100 个（海量数据 TopK）。
- answer: heapq.nlargest(100, nums)；讲小顶堆思路：维护 100 个元素，比堆顶大就替换。

### 71. dict_merge
- tags: 字典, 真题
- difficulty: easy
- frequency: 中高频
- prompt: 合并两个字典，键冲突以第二个为准。
- answer: {**d1, **d2} 或 d1.update(d2)；讲 ** 解包语法。

### 72. safe_get_nested
- tags: 字典, 防御性编程, 真题
- difficulty: medium
- frequency: 高频
- prompt: 安全取嵌套字典 data['user']['profile']['age']，任一层缺失返回默认值不报错。
- answer: 循环逐层 isinstance+in 判断；坑：直接链式取值 KeyError。

### 73. mutable_default_arg_trap
- tags: 陷阱题, 高频
- difficulty: medium
- frequency: 高频
- prompt: def f(x=[]): x.append(1); return x 连续调两次输出什么？为什么？怎么修？
- answer: [1] 和 [1,1]——默认参数只在函数定义时求值一次，可变对象被共享；修法：x=None 再 x = x or []。经典必考。

### 74. mutable_assignment_output
- tags: 陷阱题, 高频
- difficulty: easy
- frequency: 高频
- prompt: a=[1,2]; b=a; b.append(3); print(a) 输出什么？为什么？
- answer: [1,2,3]——b=a 赋的是引用（同一内存），append 原地修改双方都可见；引深浅拷贝讨论。

### 75. is_vs_eq_output
- tags: 陷阱题, 高频
- difficulty: easy
- frequency: 高频
- prompt: a=[1,2]; b=[1,2]; print(a==b, a is b) 输出什么？
- answer: True False——==比值调 __eq__，is比内存地址；补小整数缓存 -5~256 常驻。

### 76. args_kwargs_print
- tags: 函数参数, 真题
- difficulty: easy
- frequency: 高频
- prompt: 写函数接收任意位置参数和关键字参数并打印类型和内容。
- answer: def f(*args, **kwargs)：args 是 tuple，kwargs 是 dict。

### 77. my_dict_class
- tags: 面向对象, 类设计
- difficulty: medium
- frequency: 中高频
- prompt: 手写一个类实现统计字符频率（构造时传入字符串，提供 top(n) 方法）。
- answer: __init__ 里 Counter 统计存实例属性，top 方法返回 most_common(n)；考类封装。

### 78. lru_cache_ordereddict
- tags: 缓存, OrderedDict, 真题
- difficulty: hard
- frequency: 中高频
- prompt: 用 OrderedDict 手写 LRU 缓存（get/put，超容量淘汰最久未使用）。
- answer: get/put 都 move_to_end，超容量 popitem(last=False)；为什么 OrderedDict：dict 没有 move_to_end API。

### 79. simple_deque_stack
- tags: 数据结构
- difficulty: easy
- frequency: 中高频
- prompt: 用 collections.deque 实现栈和队列。
- answer: 栈 append+pop；队列 append+popleft；讲 deque 两端 O(1) 比 list 头部插入 O(n) 快。

### 80. json_file_io
- tags: JSON, 文件
- difficulty: easy
- frequency: 高频
- prompt: 把字典列表写入 JSON 文件再读回（中文不乱码）。
- answer: json.dump(data, f, ensure_ascii=False, indent=2)；坑：不加 ensure_ascii 中文变 \uXXXX。

### 81. csv_writer
- tags: CSV, 数据驱动
- difficulty: easy
- frequency: 中高频
- prompt: 把测试结果列表写入 CSV（表头：用例名,状态,耗时）。
- answer: csv.writer + writerow；讲 DictWriter 按字段名写更稳。

### 82. excel_read_openpyxl
- tags: Excel, 数据驱动, 测开特色
- difficulty: medium
- frequency: 高频
- prompt: 用 openpyxl 读取 Excel 测试用例表（第一行表头，返回字典列表）。
- answer: load_workbook + iter_rows(values_only=True)，zip 表头和每行组字典；数据驱动经典。

### 83. send_webhook_notify
- tags: 接口, 工程实战
- difficulty: medium
- frequency: 中高频
- prompt: 封装函数向飞书/企微 Webhook 发送测试结果通知。
- answer: requests.post(webhook, json={"msg_type":"text","content":...})；提加签和超时兜底。

### 84. retry_on_status_code
- tags: requests, 重试, 工程实战
- difficulty: medium
- frequency: 高频
- prompt: 封装带自动重试的 GET 请求：非 200 或超时重试 3 次。
- answer: for 循环+try except requests.Timeout/ConnectionError，检查 status_code；提 urllib3 Retry + HTTPAdapter 加分。

### 85. assert_json_path
- tags: JSON, 断言, 测开特色
- difficulty: medium
- frequency: 高频
- prompt: 写断言函数：从接口 JSON 响应中按路径 "data.user.name" 取值并校验等于预期。
- answer: 路径 split('.') 逐层下钻取值，比对预期；接口自动化断言核心。

### 86. group_by_field
- tags: 数据处理
- difficulty: medium
- frequency: 中高频
- prompt: 把用例结果列表按模块分组统计通过/失败数，返回 {模块: {passed: x, failed: y}}。
- answer: defaultdict 逐条归组累加；测试报告聚合统计原型。

### 87. diff_two_lists
- tags: 集合, 数据校验
- difficulty: easy
- frequency: 中高频
- prompt: 比对期望用户列表和实际列表，找出缺失的和多余的。
- answer: 集合差集 expected-actual（缺失）、actual-expected（多余）；数据核对经典。

### 88. sql_in_clause_builder
- tags: SQL, 造数
- difficulty: easy
- frequency: 中高频
- prompt: 给一批用户 ID，拼出安全的 SQL IN 查询（防注入）。
- answer: 参数化查询占位符 ','.join(['%s']*len(ids)) + tuple(ids)；讲为什么不能 f-string 拼。

### 89. sha256_of_file
- tags: 哈希, 文件
- difficulty: easy
- frequency: 中高频
- prompt: 计算文件的 SHA256 值（大文件不许一次读入内存）。
- answer: hashlib.sha256 分块 read(8192) 逐块 update；验证下载包完整性场景。

### 90. simple_rate_limiter
- tags: 并发, 工程实战, 加分
- difficulty: hard
- frequency: 加分题
- prompt: 实现简单限流器：每秒最多放行 N 个请求（令牌桶或滑动窗口）。
- answer: 滑动窗口：deque 记时间戳，进请求时 pop 掉 1 秒前的旧戳再判断长度；压测限流常用。
