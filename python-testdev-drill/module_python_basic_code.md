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

## 第七类：真实面试真题（测试开发方向）

> 来源：面试鸭 Python 手写代码真题库、CSDN 软件测试面试真题、TME 校招测试岗笔试真题等。

### 31. swap_without_temp
- tags: 基础语法, 经典真题
- difficulty: easy
- frequency: 高频
- prompt: 不使用中间变量，交换两个变量的值。
- answer: Python 支持多重赋值，一行 a, b = b, a 即可完成交换；也可用加减法 a = a + b; b = a - b; a = a - b，但多重赋值是 Pythonic 写法。

### 32. my_max
- tags: 基础语法, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 不使用内置 max，实现一个 max 函数，支持传入列表返回最大值。
- answer: 遍历列表，用当前最大值初始化为第一个元素，逐个比较更新，考察循环与比较逻辑。

### 33. day_of_year
- tags: 日期, 经典真题
- difficulty: easy
- frequency: 中高频
- prompt: 输入年月日，判断这一天是这一年的第几天。
- answer: 累加前几个月的天数再加当前日，注意闰年（能被4整除且不被100整除，或被400整除）2月多一天。

### 34. print_primes
- tags: 数学, 循环, 经典真题
- difficulty: easy
- frequency: 高频
- prompt: 输出给定范围内的所有质数。
- answer: 对每个数判断是否只能被1和自身整除，试除到平方根即可，外层循环内层判断。

### 35. armstrong_number
- tags: 数学, 经典真题
- difficulty: easy
- frequency: 加分题
- prompt: 检查一个数是否为 Armstrong 数（各位数字的 n 次方之和等于自身，如 153 = 1³+5³+3³）。
- answer: 转字符串取每一位，求各位的 len(str) 次方之和，与原数比较。

### 36. word_frequency_in_file
- tags: 文件处理, 统计, 真题
- difficulty: easy
- frequency: 高频
- prompt: 统计一个文本文件中每个单词出现的频率。
- answer: 逐行读取文件，split 拆分单词，用字典或 Counter 累加计数，考察文件读写与统计能力。

### 37. longest_word_in_file
- tags: 文件处理, 字符串, 真题
- difficulty: easy
- frequency: 中高频
- prompt: 查找文本文件中最长的单词并返回。
- answer: 读取全文拆分成单词列表，用 max(words, key=len) 或遍历比较取最长。

### 38. walk_folder
- tags: 文件处理, os模块, 真题
- difficulty: easy
- frequency: 高频
- prompt: 遍历一个文件夹及其所有子文件夹，打印所有文件路径。
- answer: 用 os.walk 递归遍历（根目录、子目录、文件三元组），或手写递归用 os.listdir 实现。

### 39. log_level_stats
- tags: 日志分析, 统计, 真题
- difficulty: medium
- frequency: 高频
- prompt: 日志文件每行格式为「时间戳 日志级别 消息」，统计每种日志级别（INFO/WARN/ERROR 等）出现的次数，按次数降序返回。
- answer: 逐行读取，split 取第二个字段为级别，用字典或 Counter 统计，最后按次数排序；注意脏行要跳过。

### 40. slow_api_top5
- tags: 日志分析, 排序, 真题
- difficulty: medium
- frequency: 高频
- prompt: 日志每行格式为「[时间] [接口名] [耗时ms]」，统计耗时超过 1000ms 的接口 Top5，输出接口名和次数。
- answer: 逐行解析并做格式校验和异常捕获（脏数据不崩溃），Counter 统计超时接口次数，用 most_common(5) 取 Top5。

### 41. test_result_analysis
- tags: JSON处理, 测试报告, 真题
- difficulty: medium
- frequency: 高频
- prompt: 给定测试用例执行结果的 JSON 文件（含 module、status、duration 字段），用 Python 分析并输出成功率、失败最多的模块、总耗时。
- answer: json.load 读入列表，统计 passed 数量算成功率，defaultdict 按模块累计失败次数取最大，累加 duration 得总耗时，考察 JSON 解析与聚合统计。

### 42. reverse_polish_eval
- tags: 栈, 表达式求值, 经典真题
- difficulty: hard
- frequency: 加分题
- prompt: 实现逆波兰表达式（后缀表达式）求值，如 [2,1,3,+]*2 -> (2+1)*3=9，不能使用内置 eval。
- answer: 用栈：遇到数字入栈，遇到运算符弹出两个数计算后把结果入栈，最后栈中唯一元素即结果；注意减法和除法的操作数顺序。

## 第八类：高频手写真题（续）

> 来源：面试鸭 Python 手写代码真题库、51Testing 测试面试必问、CSDN 软件测试面试八股真题等。

### 43. my_strip
- tags: 字符串, 经典真题
- difficulty: easy
- frequency: 高频
- prompt: 手写一个函数，去掉字符串开头和末尾的空格（不使用 strip）。
- answer: 用两个指针分别从头尾找到第一个非空格字符，再切片返回；考察边界处理。

### 44. my_index_of
- tags: 字符串, 查找, 经典真题
- difficulty: medium
- frequency: 高频
- prompt: 实现 strStr 函数，返回子串在主串中第一次出现的下标，找不到返回 -1（不用 find/index）。
- answer: 遍历主串每个起点，逐段截取与子串比较，相等即返回起点下标；注意空子串返回 0。

### 45. swap_case_string
- tags: 字符串, 经典真题
- difficulty: easy
- frequency: 高频
- prompt: 手写函数把字符串中大写转小写、小写转大写（不用 swapcase）。
- answer: 遍历每个字符，用 isupper/islower 判断后转换拼接；考察字符串方法与遍历。

### 46. regex_split_string
- tags: 正则, 经典真题
- difficulty: medium
- frequency: 高频
- prompt: 字符串 s = "info:xiaoZhang 33 shandong"，用正则切分输出 [info, xiaoZhang, 33, shandong]。
- answer: 用 re.split 按「冒号、空格」等多种分隔符切分，如 re.split(r":|\s+", s)，考察正则分割。

### 47. regex_valid_phone
- tags: 正则, 测试场景, 真题
- difficulty: easy
- frequency: 高频
- prompt: 用正则验证手机号是否合法（11位，1开头，第二位3-9）。
- answer: re.match(r"^1[3-9]\d{9}$", phone)，bool 转换结果；这是接口测试中参数校验的高频场景。

### 48. regex_extract_email
- tags: 正则, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 写正则从一段文本中提取所有邮箱地址。
- answer: re.findall(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)+", text)，考察 findall 与邮箱模式。

### 49. mask_phone
- tags: 正则, 数据脱敏, 真题
- difficulty: easy
- frequency: 高频
- prompt: 把手机号中间4位替换为星号，如 13800138000 -> 138****8000。
- answer: re.sub(r"(\d{3})\d{4}(\d{4})", r"****", phone)，用分组捕获保留前后段；日志脱敏常用。

### 50. generate_phone
- tags: 测试数据, 造数, 真题
- difficulty: easy
- frequency: 高频
- prompt: 用 Python 生成一个随机的合法测试手机号（自动化注册场景）。
- answer: 前缀从合法号段中随机选（如138/139/159），后8位随机数字拼接；考察 random 与业务规则结合。

### 51. compress_string
- tags: 字符串, 经典真题
- difficulty: medium
- frequency: 高频
- prompt: 字符串压缩：连续字符用「字符+次数」表示，如 aaabcc -> a3b1c2。
- answer: 遍历比较相邻字符，相同计数累加，不同则拼接「前一字符+计数」并重置；注意最后一段要在循环外补上。

### 52. remove_consecutive_duplicates
- tags: 列表, 真题
- difficulty: medium
- frequency: 加分题
- prompt: 移除列表中连续重复的元素（只保留一个），如 [1,2,2,3,3,3,2,2] -> [1,2,3,2]。
- answer: 遍历比较当前元素与前一个结果元素（或原列表前一个元素），不同才保留；与全量去重不同，只处理连续段。

### 53. longest_common_prefix
- tags: 字符串, 经典真题
- difficulty: medium
- frequency: 高频
- prompt: 求一组字符串的最长公共前缀，如 [flower, flow, flight] -> fl。
- answer: 以第一个串为初始前缀，逐个与其余字符串比较并收缩前缀，直到匹配或为空。

### 54. find_duplicates
- tags: 列表, 哈希, 经典真题
- difficulty: easy
- frequency: 高频
- prompt: 找出列表中所有重复出现的数字并返回。
- answer: 用集合记录已见元素，再次遇到即加入结果集；或 Counter 统计后取次数大于1的键。

### 55. reverse_linked_list
- tags: 链表, 数据结构, 测试面试必问
- difficulty: medium
- frequency: 高频
- prompt: 单链表反转（1->2->3 变为 3->2->1）。
- answer: 三指针法：prev/curr/next，遍历中先保存 next，再把 curr.next 指向 prev，最后 prev 就是新头节点；测试开发面试数据结构第一题。

### 56. linked_list_has_cycle
- tags: 链表, 双指针, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 判断单链表中是否存在环。
- answer: 快慢指针（Floyd 判圈）：快指针每次走两步，慢指针走一步，若相遇则有环，快指针到达尾部则无环。

### 57. queue_from_stacks
- tags: 栈, 队列, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 用两个栈实现一个队列（支持入队和出队）。
- answer: 入队压入第一个栈；出队时若第二个栈为空，把第一个栈全部倒入第二个栈再弹出，实现先进先出。

### 58. my_stack_class
- tags: 数据结构, 类, 测试面试必问
- difficulty: easy
- frequency: 中高频
- prompt: 手写一个栈类，支持 push、pop、peek、is_empty、size。
- answer: 内部用 list 实现，push 用 append，pop/peek 操作末尾元素，考察类的设计与列表操作。

### 59. deep_copy_manual
- tags: 深拷贝, 递归, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 不使用 copy.deepcopy，手写实现对嵌套列表/字典的深拷贝。
- answer: 递归遍历：是 list/dict 就逐元素递归复制重建，否则直接返回（不可变对象本身安全），考察可变性与递归。

### 60. n_days_later_date
- tags: 日期, datetime, 真题
- difficulty: medium
- frequency: 加分题
- prompt: 输入形如 20190530 的日期和整数 N，输出 N 天后的日期字符串。
- answer: 用 strptime 解析成 date 对象，加 timedelta(days=N)，再 strftime 格式化输出；考察 datetime 模块使用。

### 61. multiply_closure
- tags: 闭包, 经典真题
- difficulty: medium
- frequency: 加分题
- prompt: 写一个函数接收整数 n，返回一个新函数，新函数把参数与 n 相乘并返回。
- answer: 外层函数记住 n（闭包捕获），内层函数返回 param * n；考察闭包概念的实际运用。

### 62. lru_cache_manual
- tags: 缓存, 设计, 加分题
- difficulty: hard
- frequency: 中高频
- prompt: 手写一个 LRU 缓存，支持 get 和 put，容量超限时淘汰最久未使用的键。
- answer: 用 OrderedDict：get/put 时 move_to_end 标记最新，put 超容量时 popitem(last=False) 淘汰最旧；或手写双向链表+哈希表。

## 第九类：排序与查找进阶（真题补充）

> 来源：51Testing 测试面试手写合集、面试鸭真题库、LeetCode 测试岗高频题。

### 63. selection_sort
- tags: 排序, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 手写选择排序。
- answer: 每轮从未排序区间选出最小值，放到已排序区间末尾；外层控制边界，内层找最小下标后交换。

### 64. insertion_sort
- tags: 排序, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 手写插入排序。
- answer: 从第二个元素开始，把当前元素往前比较并后移比它大的元素，插入到正确位置；像整理扑克牌。

### 65. merge_sort
- tags: 排序, 递归, 经典真题
- difficulty: hard
- frequency: 中高频
- prompt: 手写归并排序。
- answer: 递归二分到只剩一个元素，再合并两个有序子列表（双指针归并），稳定 O(nlogn)。

### 66. heap_sort
- tags: 排序, 堆, 测试面试必问
- difficulty: hard
- frequency: 加分题
- prompt: 手写堆排序。
- answer: 先自底向上建最大堆，然后每次把堆顶（最大值）与末尾交换并重新堆化；考察 heapify 的下沉调整。

### 67. find_first_last_position
- tags: 二分查找, 变体, 高频
- difficulty: medium
- frequency: 高频
- prompt: 在有序数组中查找目标值的第一个和最后一个位置，不存在返回 [-1,-1]。
- answer: 两次二分：找到目标后不停止，继续向左收缩找第一个、向右收缩找最后一个；考察二分边界处理。

### 68. my_sqrt
- tags: 二分查找, 数学, 真题
- difficulty: easy
- frequency: 中高频
- prompt: 不使用库函数，实现求整数 x 的平方根（向下取整）。
- answer: 二分答案：在 0~x 范围内找满足 mid*mid <= x 的最大 mid；注意用整除避免浮点误差。

## 第十类：数据结构进阶（真题补充）

### 69. find_middle_node
- tags: 链表, 快慢指针, 真题
- difficulty: easy
- frequency: 高频
- prompt: 找出单链表的中间节点（偶数个时返回第二个中间节点）。
- answer: 快慢指针：快指针每次走两步、慢指针走一步，快指针到尾部时慢指针正好在中间；一次遍历 O(n)。

### 70. remove_nth_from_end
- tags: 链表, 双指针, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 删除链表倒数第 N 个节点并返回头节点。
- answer: 快指针先走 N 步，然后快慢指针同步走，快指针到尾时慢指针在倒数第 N+1 个，改指针跳过目标；用哑结点简化头部删除。

### 71. yanghui_triangle
- tags: 数组, 经典真题
- difficulty: easy
- frequency: 中高频
- prompt: 打印杨辉三角前 n 行。
- answer: 每行首尾为1，中间元素 = 上一行左右两元素之和；用上一行列表推导生成当前行。

### 72. spiral_matrix
- tags: 矩阵, 边界控制, 面试鸭真题
- difficulty: hard
- frequency: 加分题
- prompt: 给定 m×n 矩阵，按螺旋顺序（顺时针）返回所有元素。
- answer: 维护上下左右四个边界，按「左到右、上到下、右到左、下到上」循环收缩边界，注意单行单列的越界判断。

### 73. min_stack
- tags: 栈, 设计, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 设计一个支持 push、pop、top 以及 O(1) 获取最小值的栈。
- answer: 用辅助栈同步保存「每个状态下的最小值」，pop 时两个栈一起弹；考察空间换时间的设计思维。

### 74. binary_tree_max_depth
- tags: 二叉树, 递归, 高频
- difficulty: easy
- frequency: 高频
- prompt: 求二叉树的最大深度。
- answer: 递归：空树深度0，否则 max(左子树深度, 右子树深度)+1；一行递归是标配答案。

### 75. binary_tree_level_order
- tags: 二叉树, BFS, 高频
- difficulty: medium
- frequency: 中高频
- prompt: 二叉树层序遍历（按层输出节点值）。
- answer: 用队列 BFS，每轮记录当前层节点数，逐个出队并把子节点入队，收集每层结果。

### 76. binary_tree_inorder
- tags: 二叉树, 遍历, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 二叉树中序遍历（递归和迭代两种写法）。
- answer: 递归：左-根-右；迭代：用栈不断把左子树入栈，弹出访问后再转向右子树。

### 77. josephus_problem
- tags: 模拟, 经典真题
- difficulty: medium
- frequency: 加分题
- prompt: 约瑟夫环：n 个人围成一圈，从1开始报数，数到 m 的人出列，求最后剩下的人。
- answer: 递推公式 f(1)=0, f(i)=(f(i-1)+m)%i，或用列表模拟循环删除；考察数学归纳与模运算。

### 78. hanoi_tower
- tags: 递归, 经典真题
- difficulty: medium
- frequency: 加分题
- prompt: 汉诺塔：打印把 n 个盘子从 A 移到 C 的所有步骤。
- answer: 递归：先把 n-1 个从 A 借 C 移到 B，再把第 n 个 A 移 C，最后把 n-1 个从 B 借 A 移到 C。

## 第十一类：动态规划与高频算法

### 79. climb_stairs_dp
- tags: 动态规划, 高频
- difficulty: easy
- frequency: 高频
- prompt: 爬楼梯：每次爬1或2阶，求爬到 n 阶的方法数。
- answer: 本质是斐波那契：f(n)=f(n-1)+f(n-2)，滚动两个变量迭代，O(n) 时间 O(1) 空间。

### 80. house_robber
- tags: 动态规划, 高频
- difficulty: medium
- frequency: 中高频
- prompt: 打家劫舍：数组是各房屋现金，不能偷相邻两家，求最大金额。
- answer: dp[i]=max(dp[i-1], dp[i-2]+nums[i])，滚动变量迭代即可；每家只有「偷或不偷」两种决策。

### 81. coin_change
- tags: 动态规划, 高频
- difficulty: medium
- frequency: 中高频
- prompt: 零钱兑换：给定面额数组，求凑成目标金额的最少硬币数，凑不出返回 -1。
- answer: dp[金额]=最少硬币数，初始化为无穷大，对每个金额遍历所有面额取 min(dp[i-coin]+1)。

### 82. longest_palindrome_substring
- tags: 字符串, 高频
- difficulty: medium
- frequency: 高频
- prompt: 求字符串中的最长回文子串。
- answer: 中心扩展法：遍历每个位置，向两边扩展（分奇偶长度两种中心），记录最长回文；面试最常写的是这个解法。

### 83. three_sum
- tags: 双指针, 高频
- difficulty: medium
- frequency: 高频
- prompt: 找出数组中所有和为 0 的三元组（不重复）。
- answer: 先排序，固定一个数，再用左右双指针找另外两个数；注意跳过重复元素去重。

### 84. longest_increasing_subsequence
- tags: 动态规划, 经典真题
- difficulty: medium
- frequency: 中高频
- prompt: 求最长严格递增子序列的长度。
- answer: dp[i] 表示以 i 结尾的最长递增子序列长度，遍历之前所有 j，nums[j]<nums[i] 时转移；O(n²) 写法是面试标配。

## 第十二类：pytest 单测手写（测试开发必考）

> 来源：credmark、climbtheladder 等英文测试面试题库，pytest 手写是测试开发岗必考环节。

### 85. pytest_basic_test
- tags: pytest, 单元测试, 必考
- difficulty: easy
- frequency: 高频
- prompt: 手写一个最简单的 pytest 用例，测试 add(a,b) 函数（注意文件与函数命名规范）。
- answer: 测试文件以 test_ 开头、测试函数以 test_ 开头，内部用 assert 断言；运行 pytest 命令自动发现并执行。

### 86. pytest_parametrize
- tags: pytest, 参数化, 必考
- difficulty: easy
- frequency: 高频
- prompt: 用 pytest 参数化，让一个测试函数跑多组输入（如 (1,2,3)、(0,0,0)、(-1,1,0)）。
- answer: @pytest.mark.parametrize("a, b, expected", [...])，装饰器参数名与函数签名一致，pytest 自动逐组执行。

### 87. pytest_fixture_yield
- tags: pytest, fixture, 必考
- difficulty: medium
- frequency: 高频
- prompt: 手写一个带 setup/teardown 的 fixture（如数据库连接的建立与关闭）。
- answer: @pytest.fixture 内 yield 前是 setup、后是 teardown，测试函数以参数名引用 fixture；考察资源管理。

### 88. pytest_raises
- tags: pytest, 异常测试, 高频
- difficulty: easy
- frequency: 中高频
- prompt: 编写测试验证函数在非法输入时抛出指定异常（如除零）。
- answer: with pytest.raises(ZeroDivisionError): 包裹调用；不抛异常则测试失败，是负向用例的标准写法。

### 89. mock_patch_api
- tags: mock, 单元测试, 必考
- difficulty: medium
- frequency: 高频
- prompt: 用 unittest.mock.patch 模拟外部 HTTP 接口调用，让测试不打真实网络。
- answer: patch("模块名.requests.get", return_value=假响应)，注意 patch 的目标是「被使用处」而非定义处；隔离外部依赖让测试快且稳定。

### 90. monkeypatch_simple
- tags: pytest, mock, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 用 pytest 自带的 monkeypatch fixture 替换函数依赖，验证测试逻辑。
- answer: monkeypatch.setattr(模块, "函数名", 替换函数)，测试结束自动还原；比手动 patch 更 Pythonic 的 pytest 风格。

## 第十三类：测试开发工程场景（真实真题）

> 来源：接口自动化实战博客、CSDN 测试开发八股、测试平台工程真题。

### 91. csv_to_dicts
- tags: CSV, 数据驱动, 真题
- difficulty: easy
- frequency: 高频
- prompt: 读取 CSV 文件，把每行转成字典（首行为表头），返回字典列表。
- answer: 用 csv.DictReader 一行实现；或手动读首行做表头、zip 表头与每行生成字典——参数化数据驱动的地基。

### 92. json_extract_fields
- tags: JSON, 接口测试, 真题
- difficulty: easy
- frequency: 高频
- prompt: 从接口返回的 JSON（如订单列表）中提取所有指定字段的值（如所有订单号）。
- answer: json.loads 解析后列表推导式提取 [item[key] for item in data]，嵌套结构逐层取值；接口断言前置步骤。

### 93. json_flatten
- tags: JSON, 递归, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 把嵌套 JSON 扁平化，如 {a:{b:1}} 变成 {"a.b":1}（点分路径做键）。
- answer: 递归遍历：值是 dict 就带上父路径继续下钻，否则写入结果；接口全字段断言和 diff 工具的基础。

### 94. compare_json_equal
- tags: JSON, 断言, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 判断两个 JSON 数据是否相等（忽略键顺序、忽略列表顺序可选）。
- answer: 直接 ==（dict 无序天然忽略键顺序）；若忽略列表顺序，先对列表按固定规则排序（如转字符串排序）再比较；接口响应 diff 的核心。

### 95. response_time_stat
- tags: 统计, 性能, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 给定一批接口响应时间数据，计算平均值、中位数和 P95。
- answer: 排序后按公式取值：中位数取中间值（偶数取平均），P95 取第 95% 位置的值；性能报告的基础统计。

### 96. concurrent_requests
- tags: 多线程, 接口测试, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 用线程池并发请求多个 URL，收集每个请求的状态码和耗时。
- answer: concurrent.futures.ThreadPoolExecutor + executor.map/submit，requests 发请求，记录 start/end 时间；接口并发测试场景的最小实现。

### 97. gen_random_users
- tags: 测试数据, 造数, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 批量生成 N 条随机用户测试数据（姓名、邮箱、手机号），可指定数量。
- answer: 姓名从姓氏+名字池随机组合，邮箱加随机后缀，手机号按号段规则生成；不依赖 Faker 的手写造数。

### 98. id_card_valid
- tags: 校验算法, 真题
- difficulty: medium
- frequency: 加分题
- prompt: 校验 18 位身份证号是否合法（含出生日期与末位校验码）。
- answer: 前两位省份校验、6-14 位日期合法性（datetime 解析），第 18 位按加权因子 (2^(17-i))%11 与校验表比对。

### 99. count_file_lines
- tags: 文件处理, 内存优化, 真题
- difficulty: easy
- frequency: 中高频
- prompt: 统计一个超大日志文件的行数，要求不把整个文件读进内存。
- answer: for line in f 逐行迭代计数（缓冲读取，内存占用恒定）；或用缓冲块读取统计换行符数量，更快。

### 100. dir_stat_by_ext
- tags: 文件处理, 统计, 真题
- difficulty: medium
- frequency: 中高频
- prompt: 统计一个目录（含子目录）下各种扩展名文件的数量，如 {.py: 10, .log: 3}。
- answer: os.walk 递归遍历，os.path.splitext 取扩展名，字典累加统计；配合 Counter.most_common 排序输出。
