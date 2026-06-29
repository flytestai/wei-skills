# 自建题库

按模块保存用户主动提交/补充的题目原文。

## 写入规则
- 只有用户明确要求保存时才写入
- 尽量保留原题原文
- 自建题按模块隔离保存

## Python基础手写代码题

### 自建题 1：反转一个字符串
- tags: 字符串, 切片, 基础
- difficulty: easy
- prompt: 手写一个函数，接收一个字符串并返回它的反转结果。例如输入 `"hello"`，返回 `"olleh"`。
- answer: 可以直接使用切片 `s[::-1]` 实现，这是最简洁、最 Pythonic 的写法。

### 自建题 2：判断一个字符串是否是回文
- tags: 字符串, 回文, 基础
- difficulty: easy
- prompt: 手写一个函数，判断一个字符串是否是回文串。需要忽略大小写和非字母数字字符。例如 `"A man a plan a canal Panama"` 应返回 `True`。
- answer: 先把字符串标准化，只保留字母数字并统一转成小写，再判断处理后的字符串是否等于它的反转结果。

### 自建题 3：计算斐波那契数列第 n 项
- tags: 递归, 循环, 基础算法
- difficulty: easy
- prompt: 手写一个函数，返回斐波那契数列第 `n` 项，并分别说明循环写法和递归写法的区别。
- answer: 面试中通常更推荐循环写法，因为时间复杂度是 `O(n)`；递归写法更适合展示思路，但效率较低，时间复杂度接近 `O(2^n)`。

### 自建题 4：找出列表中的重复元素
- tags: 列表, 集合, 去重
- difficulty: easy
- prompt: 手写一个函数，找出列表中所有重复出现过的元素，并且结果中不要重复。
- answer: 可以用一个 `seen` 集合记录已见元素，再用另一个集合记录重复元素，最后转成列表返回。

### 自建题 5：统计列表中每个元素的出现次数
- tags: 列表, 字典, 统计
- difficulty: easy
- prompt: 手写一个函数，统计列表中每个元素出现的次数，并返回一个字典。
- answer: 可以使用 `collections.Counter`，也可以手写字典累加逻辑：`d[item] = d.get(item, 0) + 1`。

### 自建题 6：实现一个统计函数执行时间的装饰器
- tags: 装饰器, 时间统计, Python特性
- difficulty: medium
- prompt: 手写一个装饰器，用来统计任意函数的执行耗时，并保留原函数名称等元信息。
- answer: 经典做法是用 `functools.wraps` 保留元信息，在装饰器内部使用 `time.perf_counter()` 记录调用前后的时间差。

### 自建题 7：安全读取文件内容
- tags: 文件操作, 异常处理, 基础
- difficulty: easy
- prompt: 手写一个函数，接收文件路径；如果文件存在就读取内容并返回，如果不存在或读取失败则返回清晰的错误信息。
- answer: 先判断路径是否存在，再使用 `with open(...)` 读取文件，同时用 `try/except` 做异常处理，体现代码健壮性。

### 自建题 8：对字典列表按指定键排序
- tags: 排序, 字典, 列表
- difficulty: easy
- prompt: 手写一个函数，对“字典组成的列表”按指定键进行排序。例如按 `age` 对用户列表排序。
- answer: 使用 `sorted(lst, key=lambda x: x[key])` 即可，关键点是通过 `key` 指定排序依据。

### 自建题 9：合并两个字典
- tags: 字典, 基础
- difficulty: easy
- prompt: 手写一个函数，合并两个字典。如果有相同键，以后一个字典中的值为准。
- answer: Python 3.5+ 可直接使用 `{**dict1, **dict2}`；也可以使用 `update()`，但要注意是否会修改原字典。

### 自建题 10：列表推导式过滤并转换数据
- tags: 列表推导式, 过滤, 类型转换
- difficulty: easy
- prompt: 手写一个函数，把列表中的奇数筛选出来，并把它们转换成字符串列表。例如输入 `[1,2,3,4,5]`，返回 `["1","3","5"]`。
- answer: 这是列表推导式的经典用法：前半部分做转换，后半部分 `if` 条件做过滤。

### 自建题 11：实现一个文件上下文管理器
- tags: 上下文管理器, with语句, Python特性
- difficulty: medium
- prompt: 手写一个上下文管理器类，用于文件打开和关闭，支持 `with` 语句使用。
- answer: 需要实现 `__enter__` 和 `__exit__` 方法，核心是保证即使发生异常也能正常释放文件资源。

### 自建题 12：递归列出目录下的所有文件
- tags: 文件系统, os.walk, 递归
- difficulty: medium
- prompt: 手写一个函数，遍历某个目录及其所有子目录，返回其中所有文件的完整路径。
- answer: 推荐使用 `os.walk(directory)`，它比手写递归更简单也更安全。

### 自建题 13：计算一个数的阶乘
- tags: 循环, 数学, 基础算法
- difficulty: easy
- prompt: 手写一个函数，计算非负整数 `n` 的阶乘；如果传入负数，需要合理处理。
- answer: 通常使用循环实现最直接高效；注意 `0! = 1`，负数应抛出异常或做明确错误处理。

### 自建题 14：过滤出列表中的所有偶数
- tags: 列表, filter, 列表推导式
- difficulty: easy
- prompt: 手写一个函数，从列表中筛选出所有偶数并返回新列表。
- answer: 可以使用 `filter()`，也可以使用列表推导式 `[x for x in lst if x % 2 == 0]`，后者通常更直观。

### 自建题 15：将两个列表合并成一个字典
- tags: 字典, zip, 基础
- difficulty: easy
- prompt: 手写一个函数，将一个键列表和一个值列表组合成字典。例如 `['name','age']` 和 `['Alice',25]` 变成 `{'name':'Alice','age':25}`。
- answer: 最简洁的做法是使用 `dict(zip(keys, values))`。

### 自建题 16：实现一个简单队列类
- tags: 队列, 类, 数据结构
- difficulty: medium
- prompt: 手写一个简单队列类，支持入队、出队、判空和获取长度，遵循 FIFO（先进先出）规则。
- answer: 可以先用列表模拟队列，重点是理解 FIFO 行为；面试中也可以补充 `collections.deque` 会更高效。

### 自建题 17：不使用 strip 去除字符串首尾空格
- tags: 字符串, 双指针, 基础
- difficulty: medium
- prompt: 不使用 `str.strip()`，手写一个函数去除字符串首尾的空格。
- answer: 常见写法是用两个指针分别从左和右向中间收缩，找到第一个和最后一个非空格字符，再切片返回。

### 自建题 18：计算字符串中元音字母的个数
- tags: 字符串, 计数, 基础
- difficulty: easy
- prompt: 手写一个函数，统计字符串中元音字母（a、e、i、o、u，区分大小写时要同时考虑大小写）的个数。
- answer: 遍历字符串并判断字符是否在元音集合中，满足则计数加一。

### 自建题 19：统计文本中每个单词出现的次数
- tags: 字符串, 正则, Counter
- difficulty: medium
- prompt: 手写一个函数，接收一段文本，按单词维度统计每个单词出现的次数；需要忽略大小写，并尽量忽略标点影响。
- answer: 常见做法是先统一转小写，再用正则提取单词，最后用 `Counter` 或字典完成计数。

### 自建题 20：使用生成器实现斐波那契数列
- tags: 生成器, yield, 迭代
- difficulty: medium
- prompt: 手写一个生成器函数，按顺序不断产出斐波那契数列的值。
- answer: 使用 `yield` 可以按需生成数据，不需要一次性把所有结果存入内存，适合这种无限序列场景。

## 自动化测试题

## 测试开发面试题

## Python编程基础理论面试题

### 自建题 1：Python 中列表和元组有什么区别
- tags: Python基础, list, tuple, 高频
- difficulty: easy
- prompt: 请说明 Python 中列表和元组的主要区别，并从可变性、方法、性能和使用场景几个角度回答。
- answer: 列表是可变类型，用 `[]` 定义，创建后可以增删改元素，方法更多，比如 `append`、`pop`、`sort`；元组是不可变类型，用 `()` 定义，创建后不能修改，方法较少，性能通常略好，占用内存更少。元组如果内部元素也可哈希，可以作为字典的键，而列表不能作为字典键。

### 自建题 2：如何创建空字典和空集合
- tags: Python基础, dict, set
- difficulty: easy
- prompt: Python 中如何创建一个空字典和一个空集合？为什么不能用 `{}` 创建空集合？
- answer: 空字典可以用 `{}` 或 `dict()` 创建；空集合必须用 `set()` 创建。因为 `{}` 在 Python 中默认表示空字典，不表示空集合。

### 自建题 3：Python 中常见基本数据类型有哪些
- tags: Python基础, 数据类型
- difficulty: easy
- prompt: 请列举 Python 中常见的基本数据类型，并简单说明它们的用途。
- answer: 常见类型包括数字类型 `int`、`float`、`complex`，布尔类型 `bool`，字符串 `str`，列表 `list`，元组 `tuple`，字典 `dict`，集合 `set`。数字用于计算，字符串用于文本，列表和元组用于有序数据，字典用于键值映射，集合用于去重和集合运算。

### 自建题 4：如何检查变量类型
- tags: Python基础, type, isinstance
- difficulty: easy
- prompt: Python 中如何检查一个变量的类型？`type()` 和 `isinstance()` 有什么区别？
- answer: 可以使用 `type(x)` 查看变量的具体类型，也可以用 `isinstance(x, int)` 判断变量是否属于某个类型。实际开发中更常用 `isinstance()`，因为它支持继承关系判断，表达语义也更清楚。

### 自建题 5：解释 Python 中的缩进规则
- tags: Python基础, 缩进, 语法
- difficulty: easy
- prompt: Python 为什么使用缩进？缩进规则有哪些注意事项？
- answer: Python 使用缩进表示代码块，而不是大括号。同一代码块中的语句必须保持相同缩进，通常推荐使用 4 个空格作为一级缩进。缩进不一致会导致 `IndentationError`，因此缩进是 Python 语法的一部分。

### 自建题 6：如何注释 Python 代码
- tags: Python基础, 注释
- difficulty: easy
- prompt: Python 中如何写单行注释和多行注释？多行字符串和注释有什么关系？
- answer: 单行注释使用 `#`。多行内容通常可以用三引号字符串表示，虽然它本质上是字符串，但在不赋值、不使用时常被当作多行注释使用。实际项目中，函数或类的说明更推荐写成 docstring。

### 自建题 7：如何从用户获取输入
- tags: Python基础, input
- difficulty: easy
- prompt: Python 中如何从用户获取输入？`input()` 返回的数据类型是什么？
- answer: 使用 `input()` 从用户获取输入，例如 `name = input("请输入名字：")`。需要注意 `input()` 返回的一定是字符串，如果要用于数字计算，需要再用 `int()` 或 `float()` 转换。

### 自建题 8：如何将字符串转换为数字
- tags: Python基础, 类型转换, int, float
- difficulty: easy
- prompt: Python 中如何把字符串转换成整数或浮点数？转换时需要注意什么？
- answer: 字符串转整数使用 `int()`，转浮点数使用 `float()`。需要注意字符串内容必须符合目标数字格式，否则会抛出 `ValueError`，实际开发中最好做异常处理或输入校验。

### 自建题 9：如何将数字转换为字符串
- tags: Python基础, 类型转换, str
- difficulty: easy
- prompt: Python 中如何把数字转换成字符串？常见使用场景是什么？
- answer: 使用 `str()` 可以把数字转换成字符串，例如 `str(123)` 得到 `"123"`。常见场景包括字符串拼接、日志输出、格式化展示等。

### 自建题 10：Python 中如何格式化字符串
- tags: Python基础, 字符串格式化, f-string
- difficulty: easy
- prompt: Python 中常见的字符串格式化方式有哪些？你更推荐哪一种？
- answer: 常见方式有 `%` 格式化、`str.format()` 和 f-string。Python 3.6+ 更推荐 f-string，因为写法简洁、可读性好，也支持直接嵌入表达式。

### 自建题 11：如何创建和调用函数
- tags: Python基础, 函数
- difficulty: easy
- prompt: Python 中如何定义一个函数并调用它？函数参数和返回值怎么写？
- answer: 使用 `def` 定义函数，例如 `def greet(name): return f"Hello, {name}!"`，调用时传入参数即可。函数可以通过参数接收输入，通过 `return` 返回结果。

### 自建题 12：函数中的 return 语句有什么作用
- tags: Python基础, 函数, return
- difficulty: easy
- prompt: Python 函数中的 `return` 有什么作用？如果函数没有写 `return`，默认返回什么？
- answer: `return` 用于结束函数执行，并把结果返回给调用者。如果函数没有 `return`，或者只写了空 `return`，默认返回 `None`。

### 自建题 13：如何定义有默认参数的函数
- tags: Python基础, 函数参数, 默认参数
- difficulty: easy
- prompt: Python 中如何定义带默认参数的函数？默认参数有什么作用？
- answer: 可以在函数定义时给参数赋默认值，例如 `def greet(name, message="Hello")`。调用时如果不传该参数，就使用默认值；如果传了，就使用传入值。默认参数可以减少重复传参，让函数调用更灵活。

### 自建题 14：什么是 Python 的条件语句
- tags: Python基础, if, 条件判断
- difficulty: easy
- prompt: Python 中如何使用条件语句进行分支判断？`if`、`elif`、`else` 分别有什么作用？
- answer: Python 使用 `if`、`elif`、`else` 进行条件判断。`if` 判断第一个条件；`elif` 表示其他条件分支；`else` 表示前面条件都不满足时执行的默认分支。

### 自建题 15：Python 中循环有哪几种
- tags: Python基础, for, while, 循环
- difficulty: easy
- prompt: Python 中常见循环有哪些？`for` 循环和 `while` 循环分别适合什么场景？
- answer: Python 常见循环有 `for` 和 `while`。`for` 适合遍历序列或可迭代对象，比如列表、字符串、字典；`while` 适合在某个条件为真时重复执行，直到条件不满足为止。

### 自建题 16：如何中断或跳过循环
- tags: Python基础, break, continue, 循环控制
- difficulty: easy
- prompt: Python 中 `break` 和 `continue` 有什么区别？分别适合什么场景？
- answer: `break` 用于完全退出当前循环；`continue` 用于跳过本次循环后面的代码，直接进入下一次循环。比如找到目标后退出循环可以用 `break`，遇到不需要处理的数据时可以用 `continue`。

### 自建题 17：如何遍历字典
- tags: Python基础, dict, 遍历
- difficulty: easy
- prompt: Python 中如何遍历字典的键、值以及键值对？
- answer: 遍历键可以直接 `for key in dict_obj`；遍历值可以用 `dict_obj.values()`；遍历键值对可以用 `dict_obj.items()`，例如 `for key, value in person.items()`。

### 自建题 18：如何向列表添加元素
- tags: Python基础, list, append, insert
- difficulty: easy
- prompt: Python 中如何向列表末尾添加元素？如何在指定位置插入元素？
- answer: 向列表末尾添加元素使用 `append()`；在指定位置插入元素使用 `insert(index, value)`。例如 `fruits.append("orange")` 和 `fruits.insert(1, "grape")`。

### 自建题 19：如何从列表删除元素
- tags: Python基础, list, remove, pop, del
- difficulty: easy
- prompt: Python 中从列表删除元素有哪些常见方式？它们有什么区别？
- answer: `remove(value)` 按值删除第一个匹配项；`pop(index)` 按索引删除并返回该元素，不传索引默认删除最后一个；`del list[index]` 按索引删除但不返回值。选择哪种方式取决于你是按值删还是按位置删，以及是否需要返回被删除元素。

### 自建题 20：如何获取列表长度
- tags: Python基础, list, len
- difficulty: easy
- prompt: Python 中如何获取列表的长度？`len()` 还能用于哪些对象？
- answer: 使用 `len(list_obj)` 获取列表长度。`len()` 还可以用于字符串、元组、字典、集合等容器类型，用来返回元素个数或字符数。

### 自建题 21：如何对列表进行排序
- tags: Python基础, list, sort, sorted
- difficulty: easy
- prompt: Python 中如何对列表进行升序、降序排序？`list.sort()` 和 `sorted()` 有什么区别？
- answer: `list.sort()` 会在原列表上排序，默认升序，设置 `reverse=True` 可降序；`sorted()` 会返回一个新的排序列表，不改变原列表。面试中要说明是否会修改原数据，这是两者的核心区别。

### 自建题 22：如何复制列表
- tags: Python基础, list, copy, 浅拷贝, 深拷贝
- difficulty: easy
- prompt: Python 中复制列表有哪些常见方式？浅拷贝和深拷贝有什么区别？
- answer: 普通列表浅拷贝可以用 `copy()`、`list(original)` 或切片 `original[:]`。如果是嵌套列表，浅拷贝只复制外层对象，内部对象仍共享；需要完全复制嵌套对象时应使用 `copy.deepcopy()`。

### 自建题 23：如何检查元素是否在列表中
- tags: Python基础, list, in
- difficulty: easy
- prompt: Python 中如何判断某个元素是否存在于列表中？
- answer: 使用 `in` 关键字，例如 `"apple" in fruits` 返回布尔值。也可以用 `not in` 判断元素不存在。这个写法简洁清晰，是最常用方式。

### 自建题 24：字符串常用方法有哪些
- tags: Python基础, str, 字符串方法
- difficulty: easy
- prompt: 请列举 Python 字符串常用方法，并说明它们分别适合什么场景。
- answer: 常用方法包括 `strip()` 去除首尾空白，`lower()` 转小写，`upper()` 转大写，`replace()` 替换内容，`split()` 分割字符串，`capitalize()` 首字母大写。实际回答时可以结合文本清洗、格式转换、字段拆分等场景说明。

### 自建题 25：如何连接两个列表
- tags: Python基础, list, 拼接
- difficulty: easy
- prompt: Python 中如何把两个列表连接在一起？不同方式有什么区别？
- answer: 可以使用 `+` 返回新列表，也可以用 `extend()` 把第二个列表追加到第一个列表中，还可以用切片赋值。`+` 不修改原列表，`extend()` 会修改原列表，这是主要区别。

### 自建题 26：什么是字典，如何创建和使用
- tags: Python基础, dict, 键值对
- difficulty: easy
- prompt: 什么是 Python 字典？如何创建字典、访问值以及添加或修改键值对？
- answer: 字典是键值对集合，用 `{key: value}` 创建。可以通过 `dict[key]` 访问值，也可以用 `dict.get(key)` 安全获取；添加或修改键值对直接使用 `dict[key] = value`。字典适合按键快速查找数据。

### 自建题 27：如何删除字典中的键值对
- tags: Python基础, dict, 删除
- difficulty: easy
- prompt: Python 中删除字典键值对有哪些方式？`del`、`pop()` 和 `clear()` 有什么区别？
- answer: `del dict[key]` 按键删除，不返回值；`pop(key, default)` 删除并返回对应值，键不存在时可返回默认值；`clear()` 会清空整个字典。实际使用时，如果需要拿到被删的值，更适合用 `pop()`。

### 自建题 28：如何获取字典所有键和值
- tags: Python基础, dict, keys, values, items
- difficulty: easy
- prompt: Python 中如何获取字典的所有键、所有值和所有键值对？
- answer: 使用 `keys()` 获取所有键，`values()` 获取所有值，`items()` 获取所有键值对。它们返回的是视图对象，如需列表可以用 `list()` 转换。

### 自建题 29：什么是集合，有什么特点
- tags: Python基础, set, 去重, 集合运算
- difficulty: easy
- prompt: 什么是 Python 集合？集合有哪些特点和常见操作？
- answer: 集合是无序且元素唯一的数据结构，常用于去重和集合运算。可以用 `{}` 创建非空集合，用 `set()` 创建空集合；常见操作包括 `add()` 添加元素，`remove()` 删除元素，以及并集 `|`、交集 `&`、差集 `-`。

### 自建题 30：如何读取文件内容
- tags: Python基础, 文件操作, read
- difficulty: easy
- prompt: Python 中如何读取文件内容？读取整个文件和逐行读取分别怎么写？
- answer: 推荐使用 `with open(file, 'r', encoding='utf-8') as f` 打开文件，读取整个文件可用 `f.read()`，逐行读取可以直接 `for line in f`。使用 `with` 可以自动关闭文件，避免资源泄漏。

### 自建题 31：如何写入文件
- tags: Python基础, 文件操作, write
- difficulty: easy
- prompt: Python 中如何写入文件？覆盖写入和追加写入有什么区别？
- answer: 使用 `open(file, 'w')` 是覆盖写入，原内容会被替换；使用 `open(file, 'a')` 是追加写入，新内容会加到文件末尾。写文件也推荐使用 `with open(...)`，保证文件自动关闭。

### 自建题 32：什么是异常处理
- tags: Python基础, 异常处理, try-except
- difficulty: easy
- prompt: Python 中如何进行异常处理？`try`、`except`、`else`、`finally` 分别有什么作用？
- answer: `try` 中放可能出错的代码；`except` 捕获并处理异常；`else` 在没有异常时执行；`finally` 无论是否发生异常都会执行，常用于释放资源。异常处理能提升程序健壮性。

### 自建题 33：如何主动抛出异常
- tags: Python基础, raise, 异常
- difficulty: easy
- prompt: Python 中如何主动抛出异常？适合在什么场景使用？
- answer: 使用 `raise` 主动抛出异常，例如参数非法时 `raise ValueError("年龄不能为负数")`。主动抛异常适合输入校验、业务规则不满足、状态异常等场景，让调用方明确知道错误原因。

### 自建题 34：如何定义和使用模块
- tags: Python基础, 模块, import
- difficulty: easy
- prompt: Python 中什么是模块？如何创建模块并在其他文件中导入使用？
- answer: 一个 `.py` 文件就可以看作一个模块。可以在模块中定义函数、变量、类，然后通过 `import module_name` 导入，或使用 `from module_name import func` 导入指定内容。模块能帮助代码复用和组织。

### 自建题 35：什么是 Python 包
- tags: Python基础, 包, __init__.py
- difficulty: easy
- prompt: Python 中什么是包？包和模块有什么关系？
- answer: 包是包含多个模块的文件夹，通常包含 `__init__.py` 文件。模块是单个 `.py` 文件，包用于组织多个相关模块。可以通过 `from package import module` 或 `from package.subpackage import module` 使用包中的内容。

### 自建题 36：如何获取当前日期时间
- tags: Python基础, datetime, 日期时间
- difficulty: easy
- prompt: Python 中如何获取当前日期、当前时间以及格式化后的日期时间字符串？
- answer: 可以使用 `datetime.now()` 获取当前日期时间，`date.today()` 获取当前日期，使用 `strftime()` 按指定格式输出字符串，例如 `%Y-%m-%d %H:%M:%S`。

### 自建题 37：如何计算两个日期的差值
- tags: Python基础, datetime, timedelta
- difficulty: easy
- prompt: Python 中如何计算两个日期之间相差多少天？如何对日期做加减？
- answer: 两个 `datetime` 对象相减会得到 `timedelta`，可以通过 `.days` 获取天数差；日期加减可以使用 `timedelta(days=7)`。这常用于计算有效期、间隔天数、过期时间等场景。

### 自建题 38：如何使用随机数
- tags: Python基础, random
- difficulty: easy
- prompt: Python 中如何生成随机整数、随机浮点数、随机选择元素和打乱列表？
- answer: 使用 `random.randint(a, b)` 生成区间内随机整数，`random.random()` 生成 0 到 1 的随机浮点数，`random.choice(seq)` 随机选择元素，`random.shuffle(list)` 原地打乱列表。

### 自建题 39：如何安装第三方包
- tags: Python基础, pip, 第三方库
- difficulty: easy
- prompt: Python 中如何使用 pip 安装、升级、卸载第三方包，以及从 requirements 文件安装依赖？
- answer: 安装包用 `pip install package_name`，安装指定版本用 `pip install package==version`，从依赖文件安装用 `pip install -r requirements.txt`，升级用 `pip install --upgrade package`，卸载用 `pip uninstall package`。

### 自建题 40：Python 常用内置函数有哪些
- tags: Python基础, 内置函数
- difficulty: easy
- prompt: 请列举一些 Python 常用内置函数，并按用途简单分类。
- answer: 类型转换类有 `int()`、`float()`、`str()`、`list()`、`tuple()`；数学类有 `abs()`、`round()`、`min()`、`max()`、`sum()`；迭代相关有 `len()`、`range()`、`enumerate()`、`zip()`；其他常用的有 `print()`、`input()`、`open()`、`isinstance()`、`type()`、`id()`、`help()`。

### 自建题 41：如何定义类
- tags: Python基础, 面向对象, class
- difficulty: easy
- prompt: Python 中如何定义一个类？类属性、实例属性、实例方法和类方法分别是什么？
- answer: 使用 `class` 定义类，类属性属于类本身，实例属性通常在 `__init__` 中通过 `self` 定义，实例方法第一个参数是 `self`，类方法使用 `@classmethod` 修饰并接收 `cls`。创建对象时通过 `ClassName(...)` 实例化。

### 自建题 42：什么是继承
- tags: Python基础, 面向对象, 继承
- difficulty: easy
- prompt: Python 面向对象中什么是继承？继承有什么作用？
- answer: 继承指子类复用父类的属性和方法，并可以扩展或重写父类行为。它能减少重复代码，表达类之间的“是一种”关系。例如 `Dog` 和 `Cat` 可以继承 `Animal`。

### 自建题 43：如何重写父类方法
- tags: Python基础, 面向对象, 方法重写, super
- difficulty: easy
- prompt: Python 中什么是方法重写？子类重写父类方法后，如何调用父类原方法？
- answer: 子类中定义与父类同名的方法，就会覆盖父类方法，这叫方法重写。如果仍想调用父类逻辑，可以在子类方法中使用 `super().method()`。

### 自建题 44：什么是多态
- tags: Python基础, 面向对象, 多态
- difficulty: easy
- prompt: Python 面向对象中什么是多态？请用通俗方式说明。
- answer: 多态指不同对象对同一个方法调用表现出不同的行为。例如多个类都有 `draw()` 方法，调用方只需要调用 `shape.draw()`，不关心具体是圆形还是方形。Python 的多态更强调鸭子类型：只要对象有需要的方法，就可以使用。

### 自建题 45：如何使用 super 函数
- tags: Python基础, super, 继承
- difficulty: easy
- prompt: Python 中 `super()` 有什么作用？常见使用场景是什么？
- answer: `super()` 用于调用父类方法，最常见场景是在子类 `__init__` 中调用父类初始化逻辑，例如 `super().__init__(name)`。这样既能复用父类逻辑，又能在子类中扩展自己的属性。

### 自建题 46：什么是 property 装饰器
- tags: Python基础, property, 面向对象
- difficulty: medium
- prompt: Python 中 `@property` 有什么作用？什么时候适合使用？
- answer: `@property` 可以把方法包装成属性访问形式，让调用方像访问字段一样调用方法。也可以配合 setter 控制赋值逻辑。它适合用于计算属性、只读属性或需要在赋值时做校验的场景。

### 自建题 47：如何遍历数字序列
- tags: Python基础, range, for循环
- difficulty: easy
- prompt: Python 中如何使用 `range()` 遍历数字序列？`range(stop)`、`range(start, stop)`、`range(start, stop, step)` 有什么区别？
- answer: `range(5)` 生成 0 到 4；`range(5, 10)` 生成 5 到 9；`range(0, 11, 2)` 按步长 2 生成数字。`range()` 常和 `for` 循环一起使用。

### 自建题 48：如何反转列表
- tags: Python基础, list, reverse, reversed, 切片
- difficulty: easy
- prompt: Python 中反转列表有哪些方式？它们是否会修改原列表？
- answer: `list.reverse()` 会原地反转列表；切片 `list[::-1]` 会返回一个新列表；`reversed(list)` 返回反向迭代器，需要用 `list()` 转换成列表。面试时要说明是否修改原列表。

### 自建题 49：如何检查文件是否存在
- tags: Python基础, 文件操作, os.path
- difficulty: easy
- prompt: Python 中如何判断一个路径是否存在？如何区分它是文件还是目录？
- answer: 可以使用 `os.path.exists(path)` 判断路径是否存在，使用 `os.path.isfile(path)` 判断是否是文件，使用 `os.path.isdir(path)` 判断是否是目录。实际代码中常用于文件读取前的安全检查。

## Python高阶编程

### 自建题 1：列表和元组的区别，如何从高阶视角回答
- tags: Python高阶, list, tuple, 可变性
- difficulty: easy
- prompt: 从可变性、性能、内存占用和使用场景几个角度，说明 Python 中列表和元组的区别。
- answer: 列表是可变对象，适合频繁增删改；元组是不可变对象，创建后不能修改。元组通常性能略好、占用内存更少，也更适合表示“不会变化的一组数据”。如果元组内部元素都可哈希，它还能作为字典键，而列表不可以。

### 自建题 2：字典和集合底层是如何实现的
- tags: Python高阶, dict, set, 哈希表
- difficulty: medium
- prompt: 请解释 Python 字典和集合的底层实现原理，以及为什么它们查找通常很快。
- answer: 字典和集合底层都基于哈希表实现。字典存储键值对，集合本质上只存键不存值。Python 会对键求哈希值来定位槽位，因此查找、插入、删除平均时间复杂度通常是 `O(1)`。前提是键必须是可哈希对象，例如字符串、数字、不可变元组等。

### 自建题 3：什么是生成器，与列表有什么区别
- tags: Python高阶, 生成器, yield, 惰性求值
- difficulty: medium
- prompt: 请解释什么是生成器，并从内存、执行方式和使用场景几个角度对比生成器和列表。
- answer: 生成器是一种特殊迭代器，通常通过 `yield` 或生成器表达式创建。它是惰性求值的，只有在遍历到某一步时才产生对应数据，因此非常节省内存。列表会一次性把所有元素生成出来，适合需要多次访问、随机访问的数据；生成器更适合大数据量、流式处理或只遍历一次的场景。

### 自建题 4：解释 *args 和 **kwargs 的作用
- tags: Python高阶, 函数参数, args, kwargs
- difficulty: easy
- prompt: Python 中 `*args` 和 `**kwargs` 分别是什么？它们一般用在什么场景？
- answer: `*args` 用于接收任意数量的位置参数，在函数内部表现为元组；`**kwargs` 用于接收任意数量的关键字参数，在函数内部表现为字典。它们常用于通用封装、装饰器、可扩展函数接口等场景，使函数调用更灵活。

### 自建题 5：深拷贝和浅拷贝有什么区别
- tags: Python高阶, copy, 深拷贝, 浅拷贝
- difficulty: medium
- prompt: 请说明 Python 中深拷贝和浅拷贝的区别，并解释为什么嵌套对象场景下这个区别很重要。
- answer: 浅拷贝只复制最外层对象，内部子对象仍然和原对象共享引用；深拷贝会递归复制所有层级对象，得到完全独立的新对象。对于嵌套列表、嵌套字典等结构，如果只做浅拷贝，修改内部子对象时可能会意外影响原数据，因此要根据场景选择 `copy.copy()` 或 `copy.deepcopy()`。

### 自建题 6：什么是装饰器，写一个简单示例
- tags: Python高阶, 装饰器, wrapper
- difficulty: medium
- prompt: 请解释 Python 装饰器的概念，并说明它通常用来解决什么问题。
- answer: 装饰器本质上是“接收函数并返回新函数”的高阶函数，用来在不修改原函数代码的前提下增强函数行为。常见场景包括日志记录、耗时统计、权限校验、重试、缓存等。实现时通常会在内部定义 `wrapper(*args, **kwargs)`，再返回这个包装后的函数。

### 自建题 7：解释 Python 的 GIL 及其影响
- tags: Python高阶, GIL, 多线程, 多进程
- difficulty: medium
- prompt: 什么是 Python 的 GIL？它会对多线程程序带来什么影响？
- answer: GIL 是 CPython 中的全局解释器锁，用于保证同一时刻只有一个线程执行 Python 字节码。它会限制 CPU 密集型任务无法通过多线程实现真正并行，但对 I/O 密集型任务影响相对较小，因为线程在等待 I/O 时会释放 GIL。CPU 密集型并行更适合使用多进程。

### 自建题 8：什么是上下文管理器，with 语句如何工作
- tags: Python高阶, 上下文管理器, with
- difficulty: medium
- prompt: 请解释什么是上下文管理器，并说明 `with` 语句背后的工作机制。
- answer: 上下文管理器用于管理资源的获取和释放，通常通过实现 `__enter__()` 和 `__exit__()` 方法实现。`with` 语句进入代码块时会调用 `__enter__()`，退出时会调用 `__exit__()`，无论中间是否发生异常都能确保资源被正确释放，常见于文件、锁、数据库连接等场景。

### 自建题 9：Python 的内存管理机制是怎样的
- tags: Python高阶, 内存管理, 引用计数, GC
- difficulty: medium
- prompt: Python 的内存管理主要依赖哪些机制？请从引用计数、垃圾回收和内存池几个角度说明。
- answer: Python 的内存管理主要包括三部分：第一是引用计数，对象被引用时加一、引用解除时减一，计数归零时立即回收；第二是垃圾回收机制，用来解决循环引用问题，通常采用分代回收策略；第三是内存池机制，用于提高小对象内存分配效率，减少频繁申请和释放带来的开销。

### 自建题 10：什么是描述符（Descriptor）
- tags: Python高阶, 描述符, 属性管理
- difficulty: hard
- prompt: 请解释 Python 描述符的概念，以及它在属性访问控制中能发挥什么作用。
- answer: 描述符是实现了 `__get__`、`__set__`、`__delete__` 中一个或多个方法的对象。把描述符实例绑定为类属性后，就能拦截该属性的读取、赋值和删除操作。它常用于属性校验、ORM 字段映射、懒加载等高级属性管理场景。

### 自建题 11：什么是元类，它有什么用途
- tags: Python高阶, 元类, type
- difficulty: hard
- prompt: 什么是元类？Python 中为什么说“类也是对象”？元类通常适合用在什么场景？
- answer: 元类就是“创建类的类”，默认元类是 `type`。因为类本身也是对象，所以它们也可以被创建、修改和控制。通过自定义元类，可以在类创建阶段统一修改类属性、注册类、做接口约束等。但元类复杂度较高，通常只在框架开发、ORM、插件注册等高级场景使用。

### 自建题 12：解释 Python 的多继承和 MRO
- tags: Python高阶, 多继承, MRO, C3
- difficulty: hard
- prompt: Python 中多继承时方法是按什么顺序查找的？什么是 MRO？
- answer: MRO 是方法解析顺序，决定多继承场景下属性和方法按什么顺序查找。Python 使用 C3 线性化算法生成一条稳定的继承链。可以通过 `Class.__mro__` 或 `Class.mro()` 查看解析顺序。理解 MRO 的关键在于知道：当多个父类都有同名方法时，最终调用哪个方法取决于这条解析链。

### 自建题 13：什么是协程，与线程有何区别
- tags: Python高阶, 协程, 线程, 并发
- difficulty: medium
- prompt: 请解释什么是协程，并从调度方式、切换成本和使用场景几个角度对比协程与线程。
- answer: 协程是用户态的轻量级并发单位，通常由程序自己控制调度；线程由操作系统调度。协程切换开销更小，适合高并发 I/O 场景；线程更通用，但切换成本更高，且共享数据时通常要考虑锁。协程通常运行在单线程中，通过异步 I/O 提高吞吐。

### 自建题 14：解释 Python 的垃圾回收机制
- tags: Python高阶, 垃圾回收, 引用计数, 分代回收
- difficulty: medium
- prompt: Python 的垃圾回收机制有哪些组成部分？为什么只靠引用计数不够？
- answer: Python 的垃圾回收主要包含引用计数、标记清除和分代回收。引用计数能快速回收大多数对象，但无法解决循环引用；因此 Python 还会使用垃圾回收器定期扫描对象图，识别不可达对象并回收。分代回收基于“新对象更容易死亡”的经验，对不同代对象采用不同频率的回收策略。

### 自建题 15：什么是鸭子类型
- tags: Python高阶, 鸭子类型, 多态
- difficulty: easy
- prompt: 请用通俗语言解释什么是鸭子类型，并说明它体现了 Python 的什么设计思想。
- answer: 鸭子类型的核心思想是：不关心对象是不是某个固定类型，只关心它有没有需要的方法或行为。也就是说，“如果它走起来像鸭子、叫起来像鸭子，那它就是鸭子”。这体现了 Python 更重行为、更重协议，而不是强依赖静态类型继承关系。

### 自建题 16：单下划线和双下划线分别有什么含义
- tags: Python高阶, 命名规范, 下划线
- difficulty: easy
- prompt: Python 中变量名前的单下划线、双下划线，以及两边都有双下划线，分别代表什么含义？
- answer: `_var` 通常表示内部使用约定，`from module import *` 时不会默认导入；`__var` 会触发名称改写，变成 `_ClassName__var`，常用于避免子类命名冲突；`__var__` 通常是 Python 的特殊方法，如 `__init__`、`__str__`；而 `var_` 常用于避免和关键字重名。

### 自建题 17：解释闭包的概念
- tags: Python高阶, 闭包, 作用域
- difficulty: medium
- prompt: 什么是闭包？闭包为什么能“记住”外部函数中的变量？
- answer: 闭包是指内部函数引用了外部函数作用域中的变量，并且外部函数返回了这个内部函数。即使外部函数已经执行结束，这些被引用的变量仍然会被保存下来，因此内部函数后续调用时还能继续访问它们。闭包常用于函数工厂、延迟计算和装饰器实现。

### 自建题 18：什么是 Python 的 WSGI
- tags: Python高阶, WSGI, Web基础
- difficulty: medium
- prompt: 什么是 WSGI？它在 Python Web 开发中起什么作用？
- answer: WSGI 是 Python Web 服务器和 Python Web 应用之间的标准接口协议。它规定了服务器如何把请求信息传给应用，以及应用如何把响应返回给服务器。像 Gunicorn、uWSGI、Django、Flask 等都可以围绕 WSGI 协议协同工作。

### 自建题 19：解释 Python 的异步编程 asyncio
- tags: Python高阶, asyncio, async, await
- difficulty: medium
- prompt: 请解释 Python 中 `asyncio` 的核心思想，以及 `async/await` 的基本工作方式。
- answer: `asyncio` 是 Python 的异步 I/O 框架，核心思想是事件循环调度多个协程，让任务在等待 I/O 时主动让出执行权。`async def` 定义协程函数，`await` 用于等待异步操作完成。它非常适合网络请求、爬虫、消息处理等高并发 I/O 场景。

### 自建题 20：Python 中属性管理有哪些方式
- tags: Python高阶, 属性管理, property, 描述符
- difficulty: medium
- prompt: Python 中管理对象属性访问常见有哪些方式？不同方式分别适合什么场景？
- answer: 常见方式包括 `@property`，适合把方法包装成属性并添加校验；描述符，适合做更底层、更通用的属性访问控制；还可以结合 `getattr()`、`setattr()`、`__getattr__()`、`__setattr__()` 做更灵活的动态属性管理。选择哪种方式取决于场景复杂度和复用需求。

### 自建题 21：解释 Python 的模块和包
- tags: Python高阶, 模块, 包, import
- difficulty: easy
- prompt: 请解释 Python 中模块和包的概念，并说明 `sys.path` 在模块导入中的作用。
- answer: 模块通常指单个 `.py` 文件，包通常指包含 `__init__.py` 的目录，可以组织多个模块。Python 导入模块时会按 `sys.path` 中的路径顺序查找，因此运行目录、环境变量和安装路径都会影响导入结果。

### 自建题 22：什么是 Python 字节码
- tags: Python高阶, 字节码, pyc
- difficulty: medium
- prompt: 什么是 Python 字节码？它在代码执行过程中扮演什么角色？
- answer: Python 源代码在执行前通常会先编译成字节码，这是一种中间表示形式，通常可以缓存为 `.pyc` 文件。字节码最终由 Python 虚拟机执行。它不是机器码，而是解释器能理解的一组中间指令。

### 自建题 23：解释装饰器堆叠
- tags: Python高阶, 装饰器, 装饰器堆叠
- difficulty: medium
- prompt: 多个装饰器同时作用于一个函数时，执行顺序是怎样的？请说明“从下往上应用、从外往内调用”的含义。
- answer: 当一个函数写了多个装饰器时，装饰过程是从下往上应用的，例如 `@d1` 在 `@d2` 外层时，本质上是 `d1(d2(func))`。最终调用函数时，最外层装饰器先执行，再进入内层装饰器，最后才调用原函数。

### 自建题 24：什么是元组拆包
- tags: Python高阶, 元组拆包, 星号表达式
- difficulty: easy
- prompt: Python 中什么是序列拆包？普通拆包和带星号的拆包分别适合什么场景？
- answer: 序列拆包就是把可迭代对象中的元素按位置赋值给多个变量，例如 `a, b, c = (1, 2, 3)`。带星号拆包如 `first, *middle, last = [1,2,3,4,5]` 可以接收不定长中间部分。它也常用于交换变量，如 `a, b = b, a`。

### 自建题 25：解释 Python 的枚举类型
- tags: Python高阶, Enum, 枚举
- difficulty: medium
- prompt: Python 中为什么要使用枚举类型？相比直接写常量有什么好处？
- answer: 枚举类型用来表达一组有限且有明确语义的常量，例如状态、颜色、等级等。相比直接使用数字或字符串常量，枚举的可读性更高、约束更明确，也更适合配合类型提示和状态判断使用。常见实现方式是继承 `Enum`，必要时还可以配合 `auto()` 自动赋值。

### 自建题 26：什么是数据类 dataclass
- tags: Python高阶, dataclass, 类简化
- difficulty: medium
- prompt: Python 中 `@dataclass` 有什么作用？它适合用在什么场景？
- answer: `@dataclass` 可以自动为类生成 `__init__`、`__repr__`、`__eq__` 等常用方法，适合主要用于“存数据”的类。它能显著减少样板代码，提高可读性，适用于配置对象、DTO、简单实体对象等场景。

### 自建题 27：解释 Python 的类型提示
- tags: Python高阶, 类型提示, typing
- difficulty: medium
- prompt: Python 类型提示是什么？它的价值体现在哪些方面？
- answer: 类型提示是 Python 3.5+ 提供的可选静态类型标注能力，比如 `List[str]`、`Dict[str, int]`、`Optional[str]`。它不会直接改变运行时行为，但能提升代码可读性、IDE 自动补全体验和静态检查能力，适合大型项目和团队协作。

### 自建题 28：协程在 Python 中是如何实现的
- tags: Python高阶, 协程, async, yield from
- difficulty: medium
- prompt: 请简要说明 Python 协程的发展过程，以及基于生成器的旧式协程和 `async/await` 新式协程的关系。
- answer: Python 早期协程是基于生成器实现的，常用 `yield` 和 `yield from` 驱动；后来引入 `async def` 和 `await` 语法，使协程表达更清晰，也更适合配合事件循环框架使用。可以理解为：新式协程是在语言层面对协程模型进行了正式支持和语义强化。

### 自建题 29：解释 Python 的魔术方法
- tags: Python高阶, 魔术方法, dunder
- difficulty: medium
- prompt: 什么是 Python 魔术方法？它们通常用来解决什么问题？
- answer: 魔术方法是指以双下划线开头和结尾的特殊方法，例如 `__init__`、`__str__`、`__add__`。它们用于让自定义对象支持内置语法和协议，比如初始化、打印、加法运算、迭代、比较等，是 Python 面向对象协议的重要组成部分。

### 自建题 30：Python 中并发编程有哪些方式
- tags: Python高阶, 并发, 多线程, 多进程, 协程
- difficulty: medium
- prompt: Python 中常见并发编程方式有哪些？它们分别适合什么场景？
- answer: 常见方式包括多线程、多进程、协程和 `concurrent.futures` 提供的高级接口。多线程适合 I/O 密集型任务，多进程适合 CPU 密集型任务，协程适合高并发 I/O 场景，`concurrent.futures` 则提供了更统一、更易用的线程池和进程池接口。

### 自建题 31：解释 Python 的包管理工具
- tags: Python高阶, pip, poetry, virtualenv, conda
- difficulty: easy
- prompt: Python 生态中常见包管理和环境管理工具有哪些？它们分别解决什么问题？
- answer: `pip` 主要负责安装和卸载 Python 包；`virtualenv` 或 `venv` 用于创建隔离环境；`poetry` 更偏向现代依赖管理和打包；`conda` 除了管理 Python 包，也能管理跨语言依赖和环境。它们分别对应“装包”“环境隔离”“依赖声明与发布”“更完整环境管理”几个问题。

### 自建题 32：什么是 __slots__
- tags: Python高阶, __slots__, 内存优化
- difficulty: medium
- prompt: Python 中 `__slots__` 有什么作用？它的优点和限制分别是什么？
- answer: `__slots__` 用于显式限制类实例允许拥有的属性集合，从而避免为每个实例创建 `__dict__`，在大量对象场景下可以节省内存。它的限制是不能随意新增未声明属性，也会影响某些动态特性使用，因此更适合对象数量大、结构固定的场景。

### 自建题 33：解释上下文管理器协议
- tags: Python高阶, 上下文管理器, __enter__, __exit__
- difficulty: medium
- prompt: Python 上下文管理器协议包含哪些方法？`__exit__` 返回 True 和 False 有什么区别？
- answer: 上下文管理器协议主要包括 `__enter__()` 和 `__exit__()`。`__enter__()` 在进入 `with` 块时调用，`__exit__()` 在退出时调用。如果 `__exit__()` 返回 `True`，表示异常被处理并抑制；返回 `False` 或 `None` 则表示异常继续向外抛出。

### 自建题 34：Python 的参数传递到底是什么机制
- tags: Python高阶, 参数传递, call by sharing
- difficulty: medium
- prompt: Python 函数参数传递到底是值传递、引用传递，还是别的机制？请结合可变对象和不可变对象解释。
- answer: Python 采用的是“共享传参（call by sharing）”机制。函数接收到的是对象引用的副本，但对象本身仍是同一个。对于不可变对象，看起来像值传递；对于可变对象，如果在函数内部原地修改，就会反映到外部，因此常被误以为是引用传递。

### 自建题 35：解释生成器表达式
- tags: Python高阶, 生成器表达式, 惰性求值
- difficulty: easy
- prompt: 生成器表达式和列表推导式有什么区别？分别适合什么场景？
- answer: 列表推导式会立即计算并生成完整列表；生成器表达式会返回生成器对象，按需惰性产出数据。列表适合需要多次访问结果或随机访问的场景，生成器更适合大数据量、单次遍历和节省内存的场景。

### 自建题 36：什么是 functools 模块
- tags: Python高阶, functools, lru_cache, partial
- difficulty: medium
- prompt: `functools` 模块中有哪些常用工具？它们分别适合解决什么问题？
- answer: `functools` 提供了很多高阶函数工具。常见的如 `lru_cache` 用于函数结果缓存，减少重复计算；`partial` 用于创建偏函数，提前固定部分参数；`wraps` 常用于装饰器中保留原函数元信息。它们都属于增强函数能力的实用工具。

### 自建题 37：解释迭代器协议
- tags: Python高阶, 迭代器协议, __iter__, __next__
- difficulty: medium
- prompt: 什么样的对象可以被 for 循环遍历？请解释 Python 的迭代器协议。
- answer: 一个对象想被 `for` 循环遍历，通常要实现可迭代协议或迭代器协议。迭代器对象需要实现 `__iter__()` 和 `__next__()`，其中 `__next__()` 在没有更多数据时抛出 `StopIteration`。`for` 循环本质上就是不断调用这些协议方法完成遍历。

### 自建题 38：类方法和静态方法有什么区别
- tags: Python高阶, classmethod, staticmethod, OOP
- difficulty: easy
- prompt: Python 中实例方法、类方法和静态方法有什么区别？分别适合什么场景？
- answer: 实例方法接收 `self`，用于访问实例状态；类方法接收 `cls`，适合访问类属性或实现备用构造器；静态方法不接收 `self` 或 `cls`，更像放在类命名空间下的普通工具函数。选择哪一种，关键看它是否依赖实例状态或类状态。

### 自建题 39：解释元编程概念
- tags: Python高阶, 元编程, 装饰器, 元类
- difficulty: hard
- prompt: 什么是元编程？Python 中有哪些常见的元编程手段？
- answer: 元编程指“编写能操作代码本身的代码”。Python 中常见元编程手段包括装饰器、元类、动态属性访问、运行时修改类和对象、代码生成等。它能带来很强的灵活性，但也会增加理解和维护难度，因此要谨慎使用。

### 自建题 40：什么是猴子补丁
- tags: Python高阶, monkey patch, 动态修改
- difficulty: medium
- prompt: 请解释什么是猴子补丁（monkey patch），以及它的优点和风险。
- answer: 猴子补丁是指在运行时动态修改类、对象或模块的属性和方法。它的优点是灵活、见效快，常用于测试、热修复或兼容旧接口；风险是会让代码行为变得隐式且难追踪，可能影响全局状态，增加维护难度。

### 自建题 41：Python 调试技巧有哪些
- tags: Python高阶, 调试, pdb, logging
- difficulty: easy
- prompt: Python 开发中常见的调试方式有哪些？它们分别适合什么场景？
- answer: 常见调试方式包括 `print` 调试、`logging` 日志、`pdb` 交互式调试器、`breakpoint()` 断点，以及 PyCharm、VSCode 等 IDE 图形化调试。简单问题可以先用打印和日志，复杂流程和状态跟踪更适合用断点或 pdb。

### 自建题 42：解释字符串驻留
- tags: Python高阶, 字符串驻留, is
- difficulty: medium
- prompt: 什么是 Python 的字符串驻留（interning）？为什么有些相同字符串用 `is` 比较会得到 True？
- answer: Python 会对部分字符串做驻留优化，也就是让多个相同的字符串对象共享同一块内存。这样在某些场景下，相同字符串用 `is` 比较可能返回 True。但这属于实现优化，不应该依赖它做业务判断，字符串内容比较应始终使用 `==`。

### 自建题 43：Python 性能优化技巧有哪些
- tags: Python高阶, 性能优化
- difficulty: medium
- prompt: 请总结一些常见的 Python 性能优化思路，并说明优化时应该注意什么。
- answer: 常见优化方式包括使用局部变量减少全局查找、避免不必要拷贝、用生成器节省内存、用 `join()` 拼接大量字符串、选择合适数据结构、善用内置函数和标准库。优化前应先定位瓶颈，避免过早优化；同时要平衡可读性和性能收益。

### 自建题 44：解释 Python 包发布流程
- tags: Python高阶, 包发布, PyPI, build, twine
- difficulty: medium
- prompt: 如果要把一个 Python 包发布到 PyPI，大致流程是什么？
- answer: 通常要先准备 `setup.py` 或更现代的 `pyproject.toml`，配置包名、版本、依赖和元数据；然后使用 `python -m build` 构建分发包；最后通过 `twine upload dist/*` 上传到 PyPI。发布前还要注意版本号规范、README 展示和依赖声明是否正确。

### 自建题 45：什么是 wheel 格式
- tags: Python高阶, wheel, 打包分发
- difficulty: easy
- prompt: Python 包中的 wheel 是什么格式？相比源码包有什么优势？
- answer: Wheel 是 Python 的二进制分发格式，扩展名通常是 `.whl`。相比源码包，wheel 安装更快，因为很多情况下不需要在安装时再次编译。对用户来说，它能提升安装效率，也减少环境依赖问题。

### 自建题 46：解释虚拟环境的重要性
- tags: Python高阶, 虚拟环境, 依赖隔离
- difficulty: easy
- prompt: 为什么 Python 项目通常建议使用虚拟环境？
- answer: 虚拟环境可以为每个项目提供独立的 Python 解释器和依赖集合，避免不同项目之间的包版本冲突。它还能帮助团队更稳定地复现开发和部署环境，是依赖管理和项目隔离的基础手段。

### 自建题 47：Python 中函数式编程特性有哪些
- tags: Python高阶, 函数式编程, 高阶函数, lambda
- difficulty: medium
- prompt: Python 支持哪些函数式编程特性？这些特性通常适合什么样的场景？
- answer: Python 中常见函数式编程特性包括一等函数、高阶函数、`map/filter/reduce`、匿名函数 `lambda`、闭包和装饰器。它们适合数据转换、管道式处理、函数封装和行为复用，但要注意不要为了“函数式”而牺牲代码可读性。

### 自建题 48：解释 Python 的并发陷阱
- tags: Python高阶, 并发, GIL, 线程安全, 死锁
- difficulty: medium
- prompt: Python 并发编程中常见的陷阱有哪些？
- answer: 常见陷阱包括：误以为多线程一定能提升 CPU 密集型任务性能，忽略 GIL 限制；共享数据访问缺乏同步导致线程安全问题；锁使用不当造成死锁；资源竞争导致结果不稳定；协程中混入阻塞调用影响事件循环。并发优化前需要先明确任务类型和风险点。

### 自建题 49：什么是模式匹配
- tags: Python高阶, 模式匹配, match-case
- difficulty: medium
- prompt: Python 3.10 引入的 `match-case` 模式匹配是什么？它适合解决什么问题？
- answer: `match-case` 是 Python 3.10+ 提供的结构模式匹配语法，能根据数据结构和模式进行分支处理。它不仅能匹配简单常量，还能匹配列表、字典、类结构和联合模式。适合处理复杂分支逻辑、结构化数据解析等场景。

### 自建题 50：解释异步上下文管理器
- tags: Python高阶, async with, 异步上下文管理器
- difficulty: hard
- prompt: 什么是异步上下文管理器？它和普通上下文管理器有什么区别？
- answer: 异步上下文管理器用于 `async with` 语句，需要实现 `__aenter__()` 和 `__aexit__()`。它和普通上下文管理器的区别在于进入和退出过程本身也可以是异步操作，适用于异步连接池、异步会话、异步资源释放等场景。

### 自建题 51：描述符协议包含哪些方法
- tags: Python高阶, 描述符协议, __get__, __set__, __delete__
- difficulty: hard
- prompt: Python 描述符协议具体包含哪些方法？每个方法分别在什么场景下被调用？
- answer: 描述符协议包括 `__get__(self, instance, owner)`，用于读取属性；`__set__(self, instance, value)`，用于设置属性；`__delete__(self, instance)`，用于删除属性。只要对象被作为类属性绑定，并实现了这些方法之一，就可以参与属性访问控制。

### 自建题 52：解释枚举的高级用法
- tags: Python高阶, Enum, auto, unique
- difficulty: medium
- prompt: Python 枚举除了基础定义外，还有哪些常见高级用法？
- answer: 常见高级用法包括 `auto()` 自动分配值，`@unique` 确保枚举值不重复，以及在枚举类中定义实例方法，用来表达状态判断、行为封装等逻辑。这样可以让枚举不仅表示常量，还能携带一定业务语义。

### 自建题 53：属性访问控制有哪些方式
- tags: Python高阶, 属性控制, property, 私有属性
- difficulty: medium
- prompt: Python 中控制属性访问权限常见有哪些方式？
- answer: 常见方式包括公有属性、以下划线开头的保护属性约定、双下划线触发名称改写的“私有属性”、以及使用 `@property` 控制属性读写逻辑。除此之外，还可以借助描述符、`__getattr__()`、`__setattr__()` 做更高级的访问控制。

### 自建题 54：解释协程状态
- tags: Python高阶, 协程状态, 生成器状态
- difficulty: hard
- prompt: 协程或生成器在运行过程中可能有哪些状态？这些状态分别表示什么？
- answer: 常见状态包括已创建未启动、正在运行、挂起等待恢复、已关闭结束。比如生成器常见状态名有 `GEN_CREATED`、`GEN_RUNNING`、`GEN_SUSPENDED`、`GEN_CLOSED`。理解这些状态有助于排查协程是否真正启动、是否被挂起、是否已经结束。

### 自建题 55：什么是 memoryview
- tags: Python高阶, memoryview, 二进制数据
- difficulty: medium
- prompt: Python 中 `memoryview` 有什么作用？它适合用在什么场景？
- answer: `memoryview` 允许在不复制底层数据的前提下访问和操作对象内部缓冲区，例如 `bytes`、`bytearray`。它适合处理大块二进制数据、性能敏感的数据切片场景，因为可以减少不必要的数据复制。

### 自建题 56：解释结构模式匹配
- tags: Python高阶, 结构模式匹配, match-case
- difficulty: medium
- prompt: Python 的结构模式匹配和普通 if-elif 有什么区别？
- answer: 普通 `if-elif` 更偏向基于条件表达式判断，而结构模式匹配不仅判断值，还能直接拆解数据结构，比如列表、字典、对象字段等。它更适合处理层级化、结构化的数据分支逻辑，让代码更清晰。

### 自建题 57：Python 中常见数据序列化格式有哪些
- tags: Python高阶, 序列化, json, pickle, yaml, protobuf
- difficulty: medium
- prompt: Python 中常见的数据序列化格式有哪些？它们各自适合什么场景？
- answer: 常见格式有 `pickle`、`json`、`yaml`、`msgpack`、`protobuf`。`json` 跨语言兼容性好，适合接口通信；`pickle` 适合 Python 内部对象持久化，但不适合跨语言且有安全风险；`yaml` 可读性高，常用于配置；`protobuf` 适合高性能、强 schema 的通信场景。

### 自建题 58：解释 Python 的并发编程模型
- tags: Python高阶, 并发模型, 多线程, 多进程, 协程, Actor
- difficulty: hard
- prompt: 如果从更抽象的层面看，Python 常见并发编程模型有哪些？它们的核心差异是什么？
- answer: 常见并发模型包括多线程（共享内存）、多进程（进程隔离、靠 IPC 通信）、异步编程（单线程事件循环调度协程），以及更抽象的 Actor 模型（通过消息传递通信）。它们的核心差异在于调度方式、内存共享方式和通信方式。

### 自建题 59：Python 的类型系统有哪些特性
- tags: Python高阶, 类型系统, 动态类型, 强类型, 鸭子类型
- difficulty: medium
- prompt: 请总结 Python 类型系统的几个核心特性。
- answer: Python 是动态类型语言，变量在运行时绑定对象类型；它又是强类型语言，不会像某些弱类型语言那样随意做隐式转换；同时它支持鸭子类型，更强调对象行为；此外还支持可选的类型提示，帮助静态检查和大型项目维护。

### 自建题 60：什么是包的相对导入
- tags: Python高阶, 相对导入, 包结构
- difficulty: medium
- prompt: Python 包内什么是相对导入？它和绝对导入分别适合什么场景？
- answer: 相对导入是指在包内部用 `from . import module`、`from ..subpackage import x` 这种方式按包层级导入模块。它适合包内部模块之间的组织；绝对导入更适合从项目根路径出发导入，通常可读性更强。相对导入依赖正确的包上下文运行。

### 自建题 61：什么是上下文变量 contextvars
- tags: Python高阶, contextvars, 异步上下文
- difficulty: hard
- prompt: `contextvars` 是做什么用的？它为什么在异步代码中很重要？
- answer: `contextvars` 提供上下文局部变量，能让不同协程各自维护独立上下文状态，而不会像全局变量那样互相污染。它在异步 Web 请求、链路追踪、请求 ID 传递等场景中非常有用，因为这些场景往往需要“逻辑全局、协程局部”的状态隔离。

### 自建题 62：解释元类编程的应用场景
- tags: Python高阶, 元类, ORM, 自动注册
- difficulty: hard
- prompt: 元类在真实项目中常见的应用场景有哪些？
- answer: 元类常见应用包括：自动注册子类、校验类属性定义、在类创建时自动生成方法、实现 ORM 字段收集、框架插件注册等。它的价值在于把“对类的统一约束或加工”前移到类定义阶段完成。

### 自建题 63：Python 中函数缓存有哪些方式
- tags: Python高阶, 缓存, lru_cache, Redis
- difficulty: medium
- prompt: Python 中函数结果缓存有哪些常见实现方式？分别适合什么场景？
- answer: 小型场景可直接用 `functools.lru_cache`；也可以用自定义字典做简单缓存；跨进程或分布式场景通常会接 Redis 等外部缓存系统。选择方式取决于缓存粒度、数据一致性要求、是否跨进程以及失效策略。

### 自建题 64：解释异步迭代器
- tags: Python高阶, 异步迭代器, __aiter__, __anext__
- difficulty: hard
- prompt: 什么是异步迭代器？它和普通迭代器的区别是什么？
- answer: 异步迭代器用于 `async for` 场景，需要实现 `__aiter__()` 和 `__anext__()`。和普通迭代器不同，异步迭代器的取下一个元素过程本身可以包含异步等待，因此适合流式异步数据、异步分页拉取等场景。

### 自建题 65：什么是 Protocol 协议
- tags: Python高阶, typing.Protocol, 协议, 鸭子类型
- difficulty: medium
- prompt: Python 类型系统中的 `Protocol` 是什么？它和继承接口有什么不同？
- answer: `typing.Protocol` 是对鸭子类型的一种静态类型表达方式，只要对象实现了协议要求的方法，就可以被视为符合该协议，而不需要显式继承某个基类。它让 Python 的结构化类型检查能力更强，也更符合 Python 的动态风格。

### 自建题 66：解释包资源管理
- tags: Python高阶, importlib.resources, 包资源
- difficulty: medium
- prompt: Python 包内部如果有模板、配置、图片等资源文件，应该如何安全访问？
- answer: 现代 Python 推荐使用 `importlib.resources` 访问包内资源，而不是手工拼接文件路径。这样在不同安装方式、不同运行环境下更稳健，也更适合打包发布后的资源读取。

### 自建题 67：描述符常见使用场景有哪些
- tags: Python高阶, 描述符, ORM, 惰性求值
- difficulty: hard
- prompt: 除了概念解释之外，描述符在实际开发中常见有哪些使用场景？
- answer: 描述符常见场景包括属性校验、惰性求值、观察者模式实现、ORM 字段映射、统一属性存取策略等。它适合需要对“类属性控制实例访问行为”进行通用封装的场景。

### 自建题 68：解释异步生成器
- tags: Python高阶, 异步生成器, async for
- difficulty: hard
- prompt: 什么是异步生成器？它和普通生成器、普通协程分别有什么区别？
- answer: 异步生成器是在 `async def` 中使用 `yield` 定义的生成器，通常通过 `async for` 消费。它兼具“按需产出数据”和“异步等待”的能力，适合异步流式读取、订阅消息流等场景。它和普通生成器的区别在于支持异步上下文，和普通协程的区别在于它可以多次产出值。

### 自建题 69：Python 中单例模式有哪些实现方式
- tags: Python高阶, 单例模式, 元类, __new__
- difficulty: medium
- prompt: Python 中实现单例模式有哪些常见方式？它们各有什么特点？
- answer: 常见方式包括利用模块天然单例、使用装饰器、使用元类、重写 `__new__()` 等。模块方式最简单；装饰器实现直观；元类更适合统一控制类创建；`__new__()` 方案更贴近对象创建过程。是否真的需要单例，要结合共享状态和可测试性权衡。
## 性能测试面试题

### 自建题 1：什么是性能测试，性能测试的目的是什么
- tags: 性能测试, 基础理论, 高频
- difficulty: easy
- prompt: 请解释什么是性能测试，并说明做性能测试通常想解决哪些问题。
- answer: 性能测试是通过模拟一定数量用户或业务流量，评估系统在特定负载下的响应时间、吞吐量、稳定性和资源使用情况的测试活动。它的核心目的通常有三个：验证系统是否满足性能目标、发现性能瓶颈、以及为容量规划和上线决策提供依据。

### 自建题 2：性能测试和功能测试有什么区别
- tags: 性能测试, 功能测试, 对比题
- difficulty: easy
- prompt: 请从测试目标、测试方法和关注指标三个角度，对比性能测试和功能测试的区别。
- answer: 功能测试关注“功能是否正确”，通常模拟单用户或小量用户行为；性能测试关注“系统在负载下是否还能稳定、快速地工作”，通常会模拟并发流量。功能测试更关注结果对不对，性能测试更关注响应时间、TPS、吞吐量、资源占用和错误率等指标。

### 自建题 3：性能测试的主要类型有哪些
- tags: 性能测试, 负载测试, 压力测试, 稳定性测试
- difficulty: easy
- prompt: 性能测试常见有哪些类型？它们分别适合解决什么问题？
- answer: 常见类型包括基准测试、负载测试、压力测试和稳定性测试。基准测试先验证脚本和场景正确；负载测试用来找到正常承载上限；压力测试用来验证超过预期负载后的极限和恢复能力；稳定性测试则关注长时间运行下是否出现内存泄漏、资源泄漏或性能衰减。

### 自建题 4：什么是 TPS 和 QPS，它们有什么区别
- tags: 性能测试, TPS, QPS, 高频
- difficulty: easy
- prompt: 请解释 TPS 和 QPS 的含义，并说明为什么它们不是完全相同的概念。
- answer: TPS 是每秒事务处理数，更偏业务事务维度；QPS 是每秒查询或请求数，更偏接口请求维度。一个业务事务往往可能包含多个接口调用，因此一个下单事务可能只算 1 个 TPS，但会产生多个 QPS。性能测试中关注哪个指标，要看你是从业务视角还是接口视角分析问题。

### 自建题 5：什么是响应时间，90% 响应时间是什么意思
- tags: 性能测试, 响应时间, 分位值
- difficulty: easy
- prompt: 什么是响应时间？90% 响应时间（P90）为什么比平均响应时间更有参考价值？
- answer: 响应时间是从客户端发出请求到收到完整响应的总耗时。90% 响应时间表示有 90% 的请求都在这个时间以内完成，只有 10% 更慢。相比平均值，分位值更能体现大多数用户的真实体验，也更容易暴露长尾慢请求问题。

### 自建题 6：什么是并发用户数，它和线程数是一个概念吗
- tags: 性能测试, 并发用户, 线程数
- difficulty: easy
- prompt: 请解释什么是并发用户数，并说明在压测工具里它和线程数是什么关系。
- answer: 并发用户数是指同一时间内同时向系统发起请求的用户数量。在很多压测工具里，通常一个线程就模拟一个并发用户，所以线程数常常近似等于并发用户数。但真实业务中，还要考虑思考时间、业务停顿和用户行为节奏，因此“在线用户数”并不等于“真实并发数”。

### 自建题 7：什么是性能瓶颈，常见瓶颈有哪些
- tags: 性能测试, 性能瓶颈, 排查
- difficulty: easy
- prompt: 什么是性能瓶颈？请列举几个常见的性能瓶颈来源。
- answer: 性能瓶颈是限制系统吞吐能力或拉高响应时间的关键短板。常见瓶颈包括数据库慢查询、索引缺失、连接池不足、线程阻塞、内存泄漏、CPU 打满、磁盘 I/O 瓶颈、网络带宽不足、外部依赖服务响应慢等。定位瓶颈通常要结合监控、日志和压测结果一起分析。

### 自建题 8：什么是思考时间，为什么要设置思考时间
- tags: 性能测试, 思考时间, 压测场景
- difficulty: easy
- prompt: 请解释什么是思考时间，以及在性能测试场景里为什么不能忽略它。
- answer: 思考时间是指用户两次操作之间的停顿时间，例如浏览页面、阅读信息、填写表单的时间。设置思考时间可以让压测更接近真实用户行为，也能避免压测工具持续无间断发请求，导致结果虚高、场景失真。没有思考时间的测试通常更像极限压测，而不是业务场景压测。

### 自建题 9：什么是吞吐量，它和 TPS 有什么关系
- tags: 性能测试, 吞吐量, TPS
- difficulty: easy
- prompt: 什么是吞吐量？它和 TPS 在性能测试里是什么关系？
- answer: 吞吐量通常指单位时间内系统能够处理的数据量或事务量。在很多性能测试语境下，吞吐量可以直接理解为 TPS，也就是每秒完成多少笔事务；但在网络场景中，吞吐量也可能表示每秒传输的字节数。因此具体含义要结合上下文来看。

### 自建题 10：什么是性能拐点，如何找到性能拐点
- tags: 性能测试, 性能拐点, 阶梯加压
- difficulty: medium
- prompt: 请解释什么是性能拐点，以及在压测中通常如何找到这个拐点。
- answer: 性能拐点是系统性能由平稳增长转为不再增长，甚至开始下降的临界点。通常通过阶梯式加压来发现：逐步增加并发，观察 TPS、响应时间和错误率变化。当 TPS 不再提升、响应时间明显变长、错误率上升时，通常说明已经接近或达到性能拐点。

### 自建题 11：什么是容量规划，如何做容量规划
- tags: 性能测试, 容量规划, 资源评估
- difficulty: medium
- prompt: 什么是容量规划？请说明如何根据压测结果推导系统需要多少资源。
- answer: 容量规划是根据业务峰值需求和压测结果，评估系统需要多少台机器、多少资源才能安全支撑目标负载。常见做法是：先明确业务峰值，再通过压测得到单机承载能力，最后结合冗余比例、可用性要求和风险预留，推导出最终资源规模。

### 自建题 12：什么是性能基线，为什么要建立性能基线
- tags: 性能测试, 性能基线, 回归对比
- difficulty: easy
- prompt: 什么是性能基线？为什么性能测试中建议长期维护基线数据？
- answer: 性能基线是在固定环境、固定配置、固定负载下测得的一组参考性能指标。建立性能基线可以帮助团队做版本对比、发现性能劣化、判断优化是否有效，也能为线上问题排查提供参考坐标。

### 自建题 13：什么是混合场景压测，和单接口压测有什么区别
- tags: 性能测试, 混合场景, 单接口压测
- difficulty: medium
- prompt: 请解释混合场景压测的含义，并说明它和单接口压测的区别。
- answer: 单接口压测只关注某一个接口的承载能力和极限；混合场景压测则会按照真实业务比例，把浏览、查询、下单、支付等多个接口组合起来一起施压。混合场景更接近真实生产流量，也更容易暴露资源竞争和系统整体瓶颈。

### 自建题 14：性能测试报告应该包含哪些内容
- tags: 性能测试, 测试报告, 输出规范
- difficulty: easy
- prompt: 一份完整的性能测试报告通常应该包含哪些核心内容？
- answer: 性能测试报告通常包含：测试目标和范围、测试环境说明、场景设计、指标要求、执行结果、监控数据、瓶颈分析、问题列表、优化建议和最终结论。高质量报告不仅给出数据，还要说明这些数据意味着什么，以及后续建议怎么做。

### 自建题 15：什么是长尾请求，它有什么影响
- tags: 性能测试, 长尾请求, 响应时间
- difficulty: medium
- prompt: 什么是长尾请求？为什么系统平均响应时间看起来正常，但用户依然可能觉得系统很慢？
- answer: 长尾请求是指响应时间特别慢但占比不一定很高的一小部分请求。即使平均响应时间正常，如果 P95、P99 或极少数请求非常慢，用户依然会明显感知卡顿和不稳定。长尾问题通常和慢 SQL、缓存失效、GC 停顿、锁竞争等有关。

### 自建题 16：什么是全链路压测，和普通压测有什么区别
- tags: 性能测试, 全链路压测, 生产压测
- difficulty: medium
- prompt: 请解释什么是全链路压测，以及它和普通测试环境压测的主要区别。
- answer: 全链路压测通常是在接近生产甚至生产环境中，对真实完整链路进行压测，常配合流量染色、影子库或隔离机制，避免污染真实业务数据。相比普通测试环境压测，它更真实，但技术复杂度和风险控制要求也更高。

### 自建题 17：性能测试中如何准备测试数据
- tags: 性能测试, 测试数据, 数据准备
- difficulty: easy
- prompt: 性能测试为什么要重视测试数据准备？常见的数据准备方式有哪些？
- answer: 性能测试如果数据不足或数据结构不真实，会直接影响测试结果可信度。常见方式有：从测试环境抽取真实数据、通过自动化脚本调用业务接口批量造数、直接在数据库中批量生成数据。选择哪种方式，要看数据真实性要求、业务规则复杂度和准备效率。

### 自建题 18：什么是预热，为什么需要预热
- tags: 性能测试, 预热, JVM, 缓存
- difficulty: easy
- prompt: 在正式压测前为什么通常要先预热系统？预热主要解决哪些问题？
- answer: 预热是指正式压测前，先用较小负载运行一段时间，让系统进入稳定状态。这样可以提前加载类和代码、预热数据库和缓存、触发 JIT 编译、建立连接池，避免正式测试阶段前几分钟的数据失真。

### 自建题 19：性能测试通常什么时候做
- tags: 性能测试, 测试时机, 迭代流程
- difficulty: easy
- prompt: 性能测试一般在项目哪个阶段进行？为什么通常不会放在功能测试之前大规模展开？
- answer: 性能测试通常在功能相对稳定之后进行，因为如果系统功能还不稳定，压测结果本身就缺乏意义。不过在项目早期也可以做架构层面的性能摸底测试。正式版本上线前、大促活动前、重大架构变更后，通常都需要做性能验证。

### 自建题 20：性能测试和压力测试是一回事吗
- tags: 性能测试, 压力测试, 区别题
- difficulty: easy
- prompt: 性能测试和压力测试是不是同一个概念？请说明它们之间的关系和区别。
- answer: 不是一回事。性能测试是大类，包含负载测试、压力测试、稳定性测试等；压力测试只是其中一种类型，重点是验证系统在超过正常负载时的极限表现和恢复能力。可以理解为：性能测试是总集合，压力测试是其中一种专项方法。

### 自建题 21：性能测试中主要监控哪些指标
- tags: 性能测试, 监控, 高频
- difficulty: easy
- prompt: 性能测试过程中通常要从哪些层面监控指标？请按应用层、系统层、数据库层和中间件层说明。
- answer: 性能测试通常要监控四个层面。应用层看 TPS、响应时间、并发数、错误率等；系统层看 CPU、内存、磁盘 I/O、网络带宽；数据库层看连接数、慢查询、锁等待、QPS、缓存命中率；中间件层看 Redis 命中率、MQ 堆积量、线程池使用率等。只有多层联动看，才能更准确定位瓶颈。

### 自建题 22：Grafana、Prometheus、Exporter 的监控原理是什么
- tags: 性能测试, Grafana, Prometheus, Exporter
- difficulty: medium
- prompt: 请解释 Grafana + Prometheus + Exporter 这一套监控体系的基本工作原理。
- answer: Exporter 负责从服务器、数据库或中间件采集指标并暴露出来；Prometheus 定时拉取这些指标并存入时序数据库；Grafana 再从 Prometheus 查询数据并做图形化展示。可以理解为：Exporter 负责采集，Prometheus 负责存储和查询，Grafana 负责展示和告警可视化。

### 自建题 23：Linux 中常用的性能监控命令有哪些
- tags: 性能测试, Linux, 监控命令
- difficulty: easy
- prompt: Linux 环境下做性能排查时，常用的系统监控命令有哪些？分别适合看什么问题？
- answer: 常用命令有 `top` 看进程和 CPU，`free -h` 看内存，`df -h` 看磁盘空间，`iostat` 看磁盘 I/O，`vmstat` 看系统整体状态，`ss` 或 `netstat` 看网络连接，`dstat` 做综合监控。如果需要持续观察，可以配合 `watch` 周期性刷新。

### 自建题 24：如何监控 Java 应用的 JVM 性能
- tags: 性能测试, JVM, jstat, jmap, jvisualvm
- difficulty: medium
- prompt: 压测 Java 应用时，通常如何监控 JVM 层面的性能问题？
- answer: 常见工具包括 `jvisualvm`、`jstat`、`jmap`、`jstack`。`jvisualvm` 适合可视化看堆内存、线程和 GC；`jstat -gcutil` 常用于看 GC 次数、年轻代和老年代使用率；`jmap -histo` 或堆 dump 用于分析对象分布和内存泄漏；`jstack` 用于分析线程状态和阻塞问题。

### 自建题 25：如何判断 CPU 使用率是否正常
- tags: 性能测试, CPU
- difficulty: easy
- prompt: 压测时如何判断 CPU 使用率是否正常？只看总 CPU 百分比够不够？
- answer: 只看总 CPU 百分比不够，还要结合业务类型和 CPU 细分指标看。一般持续 80% 以上就要重点关注，但 CPU 密集型和 I/O 密集型应用的判断标准不同。还要看 `user`、`system`、`iowait` 等占比，如果 `iowait` 高，说明问题可能不在 CPU 本身，而在磁盘 I/O。

### 自建题 26：如何监控数据库性能指标
- tags: 性能测试, 数据库监控, MySQL
- difficulty: medium
- prompt: 性能测试中数据库层面通常要重点监控哪些指标？
- answer: 重点指标包括连接数、慢查询、QPS/TPS、锁等待、缓存命中率、磁盘 I/O、主从延迟等。数据库往往是性能瓶颈高发区，所以不仅要看“慢不慢”，还要看是不是连接池不够、锁冲突严重或缓存命中率过低。

### 自建题 27：什么是慢查询，如何定位慢查询
- tags: 性能测试, 慢查询, SQL优化
- difficulty: easy
- prompt: 什么是慢查询？在 MySQL 中通常如何定位和分析慢查询问题？
- answer: 慢查询是执行时间超过阈值的 SQL，比如超过 `long_query_time` 配置值的语句。通常先开启慢查询日志，用 `mysqldumpslow` 或日志分析工具找出高频慢 SQL，再用 `EXPLAIN` 看执行计划，判断是否走索引、是否全表扫描、是否回表过多，再决定如何优化。

### 自建题 28：如何监控 Redis 的性能
- tags: 性能测试, Redis, 监控
- difficulty: medium
- prompt: 性能测试时监控 Redis，通常要关注哪些指标？
- answer: 主要关注命中率、内存使用、连接数、慢查询、阻塞命令、QPS 和 key 数量变化等。常用 `info stats`、`info memory`、`info clients`、`slowlog get` 等命令辅助分析。Redis 如果命中率低、内存打满或连接耗尽，都会直接影响整体性能。

### 自建题 29：压测时发现数据库 CPU 很高，如何排查
- tags: 性能测试, 数据库CPU, 排查题
- difficulty: medium
- prompt: 如果压测过程中发现数据库 CPU 飙高，你通常会按什么步骤排查？
- answer: 一般会先确认是不是数据库进程本身占用 CPU 高，再查看慢查询日志和热点 SQL，然后用 `EXPLAIN` 分析执行计划，看是否缺索引或全表扫描；接着检查锁等待、连接数、缓存命中率和磁盘 I/O，最后再结合业务流量判断是不是某类请求异常集中。排查时要先定位“是高频 SQL 还是单条特别慢的 SQL”。

### 自建题 30：如何监控线程状态，什么是线程阻塞
- tags: 性能测试, 线程状态, 阻塞
- difficulty: medium
- prompt: 压测中如何观察线程状态？什么情况下可以判断系统存在明显线程阻塞问题？
- answer: 常见方式是用 `jvisualvm`、`jstack` 或线程监控面板查看线程状态。线程如果大量处于 `Blocked`、`Waiting` 或长时间等待某个锁，通常说明有锁竞争、死锁风险或线程池设计不合理。性能问题里，TPS 上不去但 CPU 又不高时，常常要重点排查线程阻塞。

### 自建题 31：什么是 GC，如何监控 GC 情况
- tags: 性能测试, GC, JVM
- difficulty: medium
- prompt: 什么是 GC？性能测试时为什么要重点关注 Full GC 的频率和耗时？
- answer: GC 是垃圾回收机制，用于回收不再使用的对象内存。性能测试中要重点看 GC 次数、停顿时间、年轻代回收情况和 Full GC 频率，因为 Full GC 往往会带来明显停顿，导致响应时间抖动甚至吞吐下降。常见监控工具有 `jstat`、GC 日志、jvisualvm 等。

### 自建题 32：如何判断是否发生了内存泄漏
- tags: 性能测试, 内存泄漏, JVM
- difficulty: medium
- prompt: 压测中如何判断系统是否可能发生了内存泄漏？
- answer: 常见现象有：老年代占用持续上升且长时间不回落、Full GC 越来越频繁但回收效果越来越差、最终出现 OOM。进一步定位通常要抓堆 dump，用 MAT、jvisualvm 等工具分析大对象、引用链和对象未释放原因。

### 自建题 33：压测时如何实时查看应用日志
- tags: 性能测试, 日志监控, Linux
- difficulty: easy
- prompt: 压测过程中如果要实时观察应用日志，常用哪些方式？
- answer: 最常用的是 `tail -f` 实时跟踪日志文件，也可以配合 `grep` 过滤 `ERROR`、`Exception`、请求 ID 等关键字。如果日志很多，还可以按应用日志、Nginx 日志、数据库日志分别开窗口观察，帮助快速判断问题出在哪一层。

### 自建题 34：什么是线程池，如何监控线程池状态
- tags: 性能测试, 线程池, Tomcat
- difficulty: medium
- prompt: 什么是线程池？性能测试时如何判断线程池是否成为瓶颈？
- answer: 线程池是预先创建并复用线程来处理任务的机制，能减少频繁创建销毁线程的开销。监控时要重点看活跃线程数、最大线程数、任务队列长度、拒绝任务数和平均等待时间。如果线程长期接近满载、队列持续堆积或出现拒绝策略触发，通常说明线程池配置偏小或下游阻塞严重。

### 自建题 35：如何监控网络带宽使用情况
- tags: 性能测试, 网络带宽, iftop, ifstat
- difficulty: easy
- prompt: 压测中怀疑网络成为瓶颈时，通常如何监控网络带宽和连接情况？
- answer: 常用命令包括 `ifstat`、`iftop`、`nload`、`sar -n`、`ss` 等。它们可以帮助观察网卡实时吞吐、热点连接、连接数变化和流量峰值。如果发现带宽接近上限、连接暴涨或某些节点流量异常集中，就要进一步分析是不是网络瓶颈或请求分发不均。

### 自建题 36：压测时发现磁盘 IO 很高，如何排查
- tags: 性能测试, 磁盘IO, 排查题
- difficulty: medium
- prompt: 如果压测中发现磁盘 I/O 很高，你通常如何一步步定位问题？
- answer: 先用 `iostat -x` 看磁盘利用率和等待时间，再用 `iotop` 或系统监控定位是哪个进程在读写磁盘；之后结合应用日志、数据库读写、日志级别和缓存策略分析原因。高 I/O 常见原因包括日志刷盘过多、数据库随机读写频繁、缓存不足和大文件操作过多。

### 自建题 37：什么是负载均衡，如何监控负载均衡效果
- tags: 性能测试, 负载均衡, Nginx
- difficulty: medium
- prompt: 什么是负载均衡？压测中如何判断负载均衡是否真正生效、分发是否均匀？
- answer: 负载均衡是把请求分发到多台服务器，避免单点过载。监控时要看每台机器的请求量、TPS、CPU、内存和响应时间是否接近；如果某台明显比其他机器忙，可能是负载策略、会话粘滞或节点异常导致分发不均。

### 自建题 38：如何监控消息队列 MQ 的性能
- tags: 性能测试, MQ, Kafka, 消息堆积
- difficulty: medium
- prompt: 性能测试时如果链路中有消息队列，通常要重点监控哪些指标？
- answer: 主要看消息堆积量、生产速率、消费速率、消费延迟、消费者实例状态和失败重试情况。消息队列的问题往往不是“服务挂了”，而是“消费跟不上”，所以监控核心要看积压是否持续扩大、延迟是否不断上升。

### 自建题 39：压测过程中如何设置监控告警
- tags: 性能测试, 告警, Grafana, Prometheus
- difficulty: easy
- prompt: 在性能测试过程中，监控告警一般如何设计才比较有效？
- answer: 告警设计要先选关键指标，再设置合理阈值和级别，比如 CPU、响应时间、错误率、Full GC、数据库连接数、MQ 堆积量等。通常会区分 Warning 和 Critical 两级，并配置通知渠道和恢复通知。好的告警不是越多越好，而是能在问题刚出现时及时提醒，同时尽量减少无效噪音。

### 自建题 40：如何生成性能监控报告
- tags: 性能测试, 监控报告, Grafana
- difficulty: easy
- prompt: 一份性能监控报告通常应该包含哪些内容？除了图表，还要写哪些分析结论？
- answer: 性能监控报告通常要包含关键指标汇总、趋势图、峰值与平均值、异常时段截图、告警记录、问题分析、与历史基线对比以及最终结论。图表只是现象展示，更重要的是解释“为什么会这样”“风险在哪里”“后续如何优化”。

### 自建题 41：压测时 TPS 上不去可能是什么原因，如何排查
- tags: 性能测试, TPS, 瓶颈分析
- difficulty: medium
- prompt: 压测过程中如果 TPS 一直上不去，你通常会从哪些层面逐步排查？
- answer: TPS 上不去可能是压力机打满、网络带宽不足、应用服务器资源耗尽、数据库慢查询或连接池不足、线程阻塞、缓存失效等原因造成的。排查时一般从“压测端 → 网络 → 应用 → 数据库/缓存 → 代码线程”逐层分析，先排除压测工具和环境瓶颈，再定位真正的系统瓶颈点。

### 自建题 42：压测时 CPU 使用率很高怎么办
- tags: 性能测试, CPU, 线程分析
- difficulty: medium
- prompt: 压测时如果 CPU 使用率很高，你通常怎么判断这是正常现象还是异常问题？又如何进一步定位？
- answer: 先结合 TPS 和响应时间判断：如果 TPS 高、响应时间稳定，CPU 高可能是正常打满；如果 TPS 低、响应时间长，说明 CPU 高背后可能有异常。定位时常用 `top` 找高 CPU 进程，再用 `top -Hp` 定位线程，最后结合 `jstack` 看线程堆栈，找到是热点计算、死循环、锁竞争还是频繁日志等问题。

### 自建题 43：压测时响应时间很长怎么分析
- tags: 性能测试, 响应时间, 排查题
- difficulty: medium
- prompt: 如果接口响应时间明显变长，你一般会从哪些方面做系统化分析？
- answer: 一般会从硬件资源、网络延迟、线程状态、中间件、数据库和应用代码六个方向分析。先看 CPU、内存、磁盘和网络是否异常，再看线程是否阻塞、Redis 或 MQ 是否有堆积，接着排查慢 SQL 和连接池，最后结合 Profiling 工具定位代码耗时点。响应时间问题往往是链路型问题，不能只盯某一个点。

### 自建题 44：如何定位线程阻塞问题
- tags: 性能测试, 线程阻塞, jstack
- difficulty: medium
- prompt: 压测过程中如果怀疑线程阻塞，通常如何定位是哪把锁、哪段代码导致的？
- answer: 常见方法是先用 `jvisualvm` 或线程面板看是否有大量线程处于 `Blocked` 状态，然后导出线程 dump，用 `jstack` 查看阻塞线程都卡在什么调用栈和锁对象上。接着分析是不是锁粒度过大、同步块范围不合理、日志打印或共享资源竞争导致。线程阻塞的关键不是只看到 blocked，而是要找到“大家都在等谁”。

### 自建题 45：如何定位数据库慢查询问题
- tags: 性能测试, 慢查询, EXPLAIN
- difficulty: medium
- prompt: 如果怀疑数据库慢查询导致性能下降，通常按什么步骤定位和优化？
- answer: 一般先开启慢查询日志并设置阈值，再通过日志分析工具找出高频或高耗时 SQL；然后使用 `EXPLAIN` 查看执行计划，重点看是否走索引、是否全表扫描、扫描行数是否过大；最后再决定是加索引、改 SQL 写法、拆分查询还是优化表结构。数据库慢查询定位的关键在于“先找热点，再看执行计划”。

### 自建题 46：什么是性能拐点，如何找到性能拐点
- tags: 性能测试, 性能拐点, 阶梯压测
- difficulty: easy
- prompt: 请解释什么是性能拐点，以及压测时如何通过阶梯式加压识别这个拐点。
- answer: 性能拐点是系统从性能平稳增长转为不再增长甚至下降的临界点。通常采用阶梯加压法，从低并发逐步升高，观察 TPS、响应时间和错误率变化。当 TPS 不再提升、响应时间明显抬升、错误率开始增加时，往往就说明已经接近性能拐点。

### 自建题 47：压测时发现内存持续增长怎么办
- tags: 性能测试, 内存泄漏, JVM
- difficulty: medium
- prompt: 压测过程中如果发现内存持续增长，你会如何判断是不是内存泄漏，并进一步定位问题？
- answer: 先通过 `jstat -gcutil` 观察老年代占用和 GC 回收效果，如果老年代持续上涨且 Full GC 后也不明显回落，就要高度怀疑内存泄漏。接着用 `jmap -histo` 看大对象分布，必要时导出堆 dump，再借助 MAT 或 jvisualvm 分析引用链，找出哪些对象被意外长期持有。

### 自建题 48：如何分析 Full GC 频繁的问题
- tags: 性能测试, FullGC, JVM调优
- difficulty: medium
- prompt: 如果系统在压测中 Full GC 很频繁，通常有哪些常见原因？你会如何区分？
- answer: 常见原因包括堆内存设置过小、对象创建过多、内存泄漏、老年代回收压力过大等。分析时可以结合 `jstat`、GC 日志和堆使用趋势判断：如果 GC 后回收效果明显但频率高，可能是堆太小或对象产生太快；如果 GC 越来越频繁但回收效果差，往往更像内存泄漏。

### 自建题 49：如何定位接口响应慢的具体代码位置
- tags: 性能测试, Profiling, 慢代码
- difficulty: medium
- prompt: 如果已经确认是应用代码层面导致接口变慢，通常如何进一步定位到具体方法甚至具体代码段？
- answer: 这类问题通常要借助 Profiling 工具，比如 JProfiler、YourKit、jvisualvm 的采样分析等。先在压测期间抓取热点方法，按耗时和调用次数排序，再查看调用链，定位是某个循环、远程调用、对象转换还是重复查库造成的。代码慢定位的关键是先看热点，再看调用路径。

### 自建题 50：压测时错误率突然升高怎么分析
- tags: 性能测试, 错误率, 故障分析
- difficulty: medium
- prompt: 压测过程中错误率突然升高，你一般会按什么顺序分析问题？
- answer: 先看错误类型，是超时、连接失败、业务异常还是系统报错；再看应用日志、网关日志和数据库日志，确认错误发生在哪一层；最后结合监控看是否有 CPU 打满、线程池满、连接池耗尽、磁盘或网络异常。错误率分析一定要先分类错误，再反推根因，不能只看一个总百分比。

### 自建题 51：如何分析数据库连接池不够的问题
- tags: 性能测试, 数据库连接池, HikariCP
- difficulty: medium
- prompt: 如果怀疑数据库连接池配置不合理或连接数不够，通常会看哪些现象和指标？
- answer: 常见现象包括应用报获取连接超时、连接池耗尽、请求大量等待数据库连接。分析时要看数据库当前连接数、连接池最大连接数、活跃连接数、等待队列、连接使用时长和是否存在连接泄漏。连接池问题不仅可能是“池太小”，也可能是“连接没及时释放”。

### 自建题 52：如何判断是前端问题还是后端问题
- tags: 性能测试, 前后端排查, 抓包
- difficulty: easy
- prompt: 页面响应慢时，如何快速判断问题更多来自前端、网络还是后端接口？
- answer: 一般会用浏览器开发者工具或抓包工具看请求瀑布图，重点关注 DNS、连接建立、Waiting、Content Download 等阶段。如果 Waiting 很长，通常偏后端处理慢；如果下载或渲染时间长，可能是前端资源大或前端处理慢。也可以直接绕过前端压测接口，进一步确认瓶颈位置。

### 自建题 53：Redis 缓存命中率低怎么优化
- tags: 性能测试, Redis, 缓存命中率
- difficulty: medium
- prompt: Redis 命中率偏低会带来什么问题？一般有哪些常见优化手段？
- answer: 命中率低会导致更多请求打到数据库，增加后端压力并拉长响应时间。常见优化方式包括优化 key 设计、调整过期时间、增加热点数据预热、补充缓存穿透防护、评估哪些数据真正适合缓存。优化缓存命中率的关键不是一味延长过期时间，而是让缓存策略更贴近访问模式。

### 自建题 54：如何定位网络瓶颈问题
- tags: 性能测试, 网络瓶颈, 带宽
- difficulty: medium
- prompt: 如果怀疑性能问题来自网络瓶颈，通常会看哪些指标和现象？
- answer: 常见排查项包括网卡带宽利用率、网络延迟、丢包率、连接数、上下行流量峰值和单请求返回数据量。可以用 `ifstat`、`iftop`、`ping`、`sar -n` 等工具辅助判断。如果链路延迟高、带宽接近上限或返回包过大，就要进一步分析是不是网络瓶颈或报文设计问题。

### 自建题 55：消息队列 MQ 堆积怎么处理
- tags: 性能测试, MQ, 消息堆积
- difficulty: medium
- prompt: 如果压测时发现消息队列出现明显堆积，你通常会怎么判断原因并处理？
- answer: MQ 堆积本质上是生产速度大于消费速度。分析时先看是消费者数量不足、消费逻辑太慢、下游服务阻塞，还是某些消费者异常退出。处理方式一般包括扩容消费者、优化消费代码、异步化慢操作、削峰限流，必要时还要检查消息重试和死信机制是否加剧了积压。

### 自建题 56：如何分析线程池配置不合理的问题
- tags: 性能测试, 线程池, 配置调优
- difficulty: medium
- prompt: 如果怀疑线程池配置不合理导致系统吞吐下降或超时，你通常如何判断？
- answer: 常见现象是请求超时、任务堆积、拒绝执行异常，但 CPU 和内存未必很高。排查时要看活跃线程数、最大线程数、任务队列长度、拒绝策略触发情况，再结合任务类型判断线程池是不是过小或队列设计不合理。线程池调优不能只看线程数，还要结合 CPU 密集型还是 I/O 密集型任务特征。

### 自建题 57：如何排查磁盘 IO 瓶颈
- tags: 性能测试, 磁盘IO, iostat
- difficulty: medium
- prompt: 如果压测中发现磁盘 I/O 可能成为瓶颈，通常如何逐步定位根因？
- answer: 一般先用 `iostat -x` 看磁盘利用率、等待时间和队列，再用 `iotop` 找到读写最频繁的进程；然后结合日志写入量、数据库缓存命中率和应用读写模式分析原因。常见根因包括日志过多、数据库缓存不足、频繁落盘、磁盘介质性能差等。

### 自建题 58：压测时如何定位是哪个系统的瓶颈
- tags: 性能测试, 微服务, 链路追踪
- difficulty: medium
- prompt: 在多系统或微服务链路中，压测时如何判断真正的瓶颈出在哪个系统？
- answer: 通常要结合链路追踪、分系统监控和日志一起分析。先看整体调用链里哪个环节耗时最长，再对比各系统的 CPU、内存、TPS、错误率和线程状态，必要时用 mock 或隔离法把某个下游替换掉，观察整体性能变化。多系统场景下，不能只看入口服务，要看整条链路的“最长板”和“短板”。

### 自建题 59：如何分析 JVM 参数配置不合理的问题
- tags: 性能测试, JVM参数, GC调优
- difficulty: hard
- prompt: 如果怀疑 JVM 参数配置不合理影响了性能，通常会从哪些方面分析？
- answer: 重点看堆大小是否合理、年轻代和老年代比例是否合适、GC 策略是否匹配业务场景，以及是否存在频繁 Full GC 或停顿过长问题。可以结合 `jstat`、GC 日志和压测曲线看参数是否导致内存利用率低、回收频率高或停顿明显。JVM 参数问题本质是“内存分配策略和业务对象生命周期不匹配”。

### 自建题 60：如何综合分析定位性能瓶颈
- tags: 性能测试, 综合分析, 瓶颈定位
- difficulty: hard
- prompt: 如果让你系统性地定位一次性能瓶颈，你通常会按什么整体思路推进？
- answer: 我通常按“压测端 → 网关/网络 → 应用层 → JVM/线程池 → 数据库/缓存/中间件 → 代码热点”这条链路逐层排查，先从最外层排除环境和工具问题，再逐步深入到系统内部。整个过程要同时结合压测结果、监控指标、日志、线程 dump、GC 数据和链路追踪，避免只看单一指标下结论。真正有效的性能分析，核心不是背工具，而是建立分层排查思路。

### 自建题 61：数据库慢查询如何优化
- tags: 性能测试, 慢查询优化, MySQL
- difficulty: medium
- prompt: 如果已经定位到数据库慢查询，通常有哪些常见优化方向？
- answer: 常见优化方向包括给高频查询字段补充索引、优化 SQL 写法、避免 `select *`、减少函数导致的索引失效、做分页优化、引入读写分离，以及在数据量特别大时考虑分库分表。数据库优化通常优先看执行计划，因为很多性能问题本质上都是“不该扫的表被扫了”。

### 自建题 62：如何优化线程阻塞问题
- tags: 性能测试, 线程阻塞, 锁优化
- difficulty: medium
- prompt: 如果压测中已经确认有线程阻塞，通常有哪些常见优化思路？
- answer: 常见做法包括减小锁粒度、缩短锁持有时间、避免在锁内做日志和远程调用、把同步逻辑改成异步、根据场景引入 `ReentrantLock` 或读写锁等。线程阻塞优化的核心思路是：减少竞争、减少等待、减少共享资源上的串行化。

### 自建题 63：如何优化 Redis 缓存提高命中率
- tags: 性能测试, Redis, 命中率优化
- difficulty: medium
- prompt: Redis 命中率偏低时，通常有哪些有效优化手段？
- answer: 常见优化手段包括调整过期时间、提前预热热点数据、优化缓存 key 设计、防止缓存穿透和缓存雪崩、梳理哪些数据真正适合缓存。提高命中率的关键不只是“缓存更多”，而是让缓存策略和真实访问模式对齐。

### 自建题 64：如何优化 JVM 参数提升性能
- tags: 性能测试, JVM调优, G1GC
- difficulty: medium
- prompt: JVM 参数优化时，通常优先会关注哪些参数和思路？
- answer: 一般优先关注堆大小、年轻代与老年代比例、GC 策略、GC 日志和线程栈大小。常见建议包括让 `-Xms` 和 `-Xmx` 保持一致、根据机器内存和业务对象特征设置合理堆大小、选择适合并发场景的 GC 策略，并通过 GC 日志验证调优效果。JVM 调优一定要基于现象和数据，而不是只套模板参数。

### 自建题 65：数据库连接池如何优化
- tags: 性能测试, 连接池优化, HikariCP
- difficulty: medium
- prompt: 数据库连接池优化一般从哪些方面入手？
- answer: 常见优化点包括调整最大连接数、设置合理的连接获取超时和查询超时、回收空闲连接、开启连接有效性检测，以及排查连接泄漏。连接池优化既要避免连接数过小导致排队，也要避免连接数过大反而压垮数据库。

### 自建题 66：如何优化 Tomcat 性能
- tags: 性能测试, Tomcat, 线程池
- difficulty: medium
- prompt: Tomcat 在高并发场景下通常有哪些常见优化项？
- answer: 常见优化包括调整 Connector 线程池参数，例如 `maxThreads`、`minSpareThreads`、`acceptCount`，给 JVM 分配合理内存，使用更合适的连接器模式如 NIO，并关闭不必要的组件。Tomcat 优化本质上是把请求接入能力、线程处理能力和 JVM 资源配置调到相对平衡。

### 自建题 67：如何优化 MySQL 数据库性能
- tags: 性能测试, MySQL优化, buffer pool
- difficulty: medium
- prompt: 如果从更全面的角度看，MySQL 性能优化通常有哪些主要方向？
- answer: 常见方向包括索引优化、SQL 优化、参数配置优化、连接数优化、表结构优化，以及在业务量增大后做读写分离或分库分表。比如 InnoDB 的 buffer pool 设置是否合理，往往会直接影响磁盘命中率和整体查询性能。

### 自建题 68：如何优化网络性能
- tags: 性能测试, 网络优化, Gzip, CDN
- difficulty: easy
- prompt: 如果性能瓶颈主要在网络传输层，一般有哪些优化思路？
- answer: 常见做法包括提升带宽、开启 Gzip 压缩、减少接口返回字段、压缩报文、静态资源走 CDN、控制图片和文件大小等。网络优化的本质是减少传输量、降低等待时间，并尽量让重资源内容走更合适的分发路径。

### 自建题 69：如何优化接口响应时间
- tags: 性能测试, 接口优化, 响应时间
- difficulty: medium
- prompt: 如果要把一个慢接口优化到更快，通常会从哪些维度下手？
- answer: 常见方向包括数据库优化、加缓存、减少远程调用、并行独立查询、把非核心链路异步化，以及优化代码实现细节。接口优化通常不能只看一层，很多慢接口其实是“多处都不算特别慢，但串起来整体变慢”。

### 自建题 70：消息队列如何优化提升吞吐量
- tags: 性能测试, MQ优化, 吞吐量
- difficulty: medium
- prompt: 如果消息队列消费吞吐量不足，通常有哪些可落地的优化办法？
- answer: 常见方式包括增加消费者实例、批量拉取和批量处理消息、优化消费逻辑中的慢操作、异步化外部调用、合理设置消费线程数和分区数。MQ 吞吐优化的关键是提高消费效率，同时避免单条消息处理路径过重。

### 自建题 71：如何优化 Full GC 频繁的问题
- tags: 性能测试, FullGC优化, JVM
- difficulty: medium
- prompt: 如果系统 Full GC 过于频繁，通常有哪些针对性的优化手段？
- answer: 常见优化包括增大堆内存、调整年轻代比例、减少大对象和临时对象创建、修复内存泄漏、选择更适合当前业务的 GC 策略。优化之前要先确认根因，因为“堆太小”和“对象泄漏”虽然现象都像 Full GC 频繁，但处理方式完全不同。

### 自建题 72：如何优化高并发下的库存扣减问题
- tags: 性能测试, 秒杀, 库存扣减, Redis
- difficulty: hard
- prompt: 秒杀或高并发下单场景中，库存扣减为什么容易成为瓶颈？通常如何优化？
- answer: 高并发库存扣减容易遇到数据库热点行竞争、超卖和吞吐不足问题。常见优化方式包括 Redis 预扣库存、Lua 脚本做原子扣减、引入分布式锁、用消息队列削峰填谷、再异步回写数据库。这里的核心目标是既保证一致性，又避免所有请求直接打到数据库。

### 自建题 73：如何优化日志打印对性能的影响
- tags: 性能测试, 日志优化, 异步日志
- difficulty: easy
- prompt: 日志打印为什么可能影响系统性能？一般有哪些优化方式？
- answer: 日志会带来字符串拼接、I/O 写盘、锁竞争和磁盘压力，尤其在高并发场景下更明显。常见优化方式包括提高日志级别、减少无意义日志、不要在循环里打印大量日志、使用异步日志框架、配置日志滚动和压缩。日志优化的关键是“保留有价值的信息，减少对主流程的打扰”。

### 自建题 74：如何优化大数据量分页查询
- tags: 性能测试, 分页优化, 深度分页
- difficulty: medium
- prompt: 大数据量分页为什么会慢？通常有哪些常见优化方案？
- answer: 深度分页慢的根本原因是数据库往往要先扫描或跳过大量数据。常见优化方式包括延迟关联、基于主键或游标的翻页、记录上一页最大 ID，以及在搜索场景下引入 Elasticsearch 等更适合检索和分页的系统。分页优化的关键是减少“无效扫描”。

### 自建题 75：如何优化接口加解密性能
- tags: 性能测试, 加解密优化, AES, RSA
- difficulty: medium
- prompt: 如果接口因为加解密导致性能偏低，一般有哪些优化思路？
- answer: 常见思路包括选择更高效的加密算法、减少加解密字段范围、不要对整个报文做不必要的重加密、在安全前提下减少重复加解密次数，必要时对结果做缓存。性能优化不能脱离安全边界，所以这类问题要在合规前提下做权衡。

### 自建题 76：如何优化线程池配置
- tags: 性能测试, 线程池优化, 线程数
- difficulty: medium
- prompt: 线程池参数优化时，核心线程数、最大线程数、队列长度和拒绝策略一般如何考虑？
- answer: 线程池优化要结合任务类型。CPU 密集型任务线程数通常接近 CPU 核数，I/O 密集型可以适当更大；最大线程数决定峰值承载能力；队列长度影响缓冲能力；拒绝策略决定系统在满载时如何退化。线程池调优本质上是在吞吐、延迟、资源占用和系统稳定性之间做平衡。

### 自建题 77：如何优化静态资源加载性能
- tags: 性能测试, 静态资源, CDN, 缓存
- difficulty: easy
- prompt: 页面静态资源加载慢时，常见的优化方式有哪些？
- answer: 常见优化包括把图片、JS、CSS 放到 CDN，设置合理浏览器缓存，压缩和合并资源文件，使用 WebP、懒加载和按需加载，减少首屏资源体积。静态资源优化往往对页面体验提升非常直接，属于投入产出比很高的一类优化。

### 自建题 78：如何优化代码层面的性能问题
- tags: 性能测试, 代码优化, 批量查询
- difficulty: medium
- prompt: 如果问题已经定位到代码实现本身，常见的性能优化手段有哪些？
- answer: 常见方式包括减少循环查库、改成批量查询、避免在循环里频繁创建对象、选择更合适的数据结构、优化字符串拼接、加入合理缓存、减少重复计算。代码层优化的关键不是“写得更炫”，而是减少不必要的资源消耗和重复劳动。

### 自建题 79：如何优化服务间调用性能
- tags: 性能测试, 微服务调用, 并行调用
- difficulty: medium
- prompt: 微服务之间调用较多时，如何优化跨服务调用的整体性能？
- answer: 常见优化思路包括减少调用次数、把多个小接口合并成批量接口、对独立调用做并行化、设置合理超时和降级策略、对低频变化数据做缓存。服务间调用优化本质上是在减少链路长度、减少等待和减少重复请求。

### 自建题 80：性能优化的整体思路和优先级是什么
- tags: 性能测试, 性能调优, 优先级
- difficulty: hard
- prompt: 如果让你总结性能优化的整体思路和优先级，你会怎么回答？
- answer: 我的思路一般是先定位、再优化，优先处理收益高、风险低、见效快的问题。通常会先看数据库和缓存，再看代码实现和调用链，然后再考虑架构调整，最后才考虑扩容和硬件升级。也就是说，优先优化“结构性浪费”，再优化“资源不足”。每次优化后都必须回归压测验证，不能只凭感觉判断是否优化成功。

## 中间件面试题

### 自建题 1：Redis 是什么，有什么特点和应用场景
- tags: 中间件, Redis, 高频
- difficulty: easy
- prompt: 请解释 Redis 是什么，并从特点和典型应用场景两个角度展开说明。
- answer: Redis 是一个高性能的键值型内存数据库，支持多种数据结构，读写速度非常快。它的典型特点包括基于内存、支持持久化、支持丰富数据结构、天然适合高并发场景。常见应用包括缓存、分布式锁、计数器、排行榜、Session 共享、秒杀库存预扣减等。

### 自建题 2：Redis 的五种基本数据类型及使用场景
- tags: 中间件, Redis, 数据类型
- difficulty: easy
- prompt: Redis 常用的五种基本数据类型分别是什么？各自适合哪些典型业务场景？
- answer: `String` 适合缓存、计数器和分布式锁；`Hash` 适合存储对象字段；`List` 适合消息队列和最新列表；`Set` 适合去重和关系集合；`ZSet` 适合排行榜和延迟任务。面试里不仅要会背类型，还要能说出“为什么这个场景适合这个结构”。

### 自建题 3：什么是缓存穿透，如何解决
- tags: 中间件, Redis, 缓存穿透
- difficulty: easy
- prompt: 什么是缓存穿透？它为什么会给数据库带来压力？通常有哪些解决方案？
- answer: 缓存穿透指查询的数据本身不存在，导致缓存查不到、数据库也查不到，但请求每次都会继续打到数据库。这样如果请求量很大，数据库就会被无效流量拖垮。常见解决方式包括缓存空值、布隆过滤器和接口层参数校验。

### 自建题 4：什么是缓存击穿，如何解决
- tags: 中间件, Redis, 缓存击穿
- difficulty: easy
- prompt: 什么是缓存击穿？它和缓存穿透有什么区别？热点 key 过期时通常如何保护数据库？
- answer: 缓存击穿通常指某个热点 key 失效后，大量并发请求同时穿透到数据库。它和缓存穿透的区别在于：击穿的数据本身是存在的，只是热点缓存刚好过期。常见解决方案包括热点 key 永不过期、互斥锁重建缓存、逻辑过期和后台异步刷新。

### 自建题 5：什么是缓存雪崩，如何解决
- tags: 中间件, Redis, 缓存雪崩
- difficulty: easy
- prompt: 什么是缓存雪崩？为什么大量 key 同时过期会比较危险？
- answer: 缓存雪崩指大量缓存 key 在同一时间集中失效，导致请求瞬间大规模回源数据库，可能把数据库压垮。常见应对方式包括给过期时间加随机值、做集群分流、热点数据提前预热、以及在高峰时做限流和降级。

### 自建题 6：Redis 的持久化机制有哪些
- tags: 中间件, Redis, RDB, AOF
- difficulty: easy
- prompt: Redis 持久化主要有哪些机制？RDB 和 AOF 各自的优缺点是什么？
- answer: Redis 主要有 RDB 和 AOF 两种持久化机制。RDB 是定期快照，优点是恢复快、文件紧凑，缺点是可能丢失最近一段时间数据；AOF 是记录写命令日志，优点是数据更完整，缺点是文件更大、恢复更慢。很多生产环境会两者结合使用，兼顾恢复效率和数据安全。

### 自建题 7：Redis 如何实现分布式锁
- tags: 中间件, Redis, 分布式锁
- difficulty: medium
- prompt: Redis 实现分布式锁的基本思路是什么？为什么加锁和释放锁都不能只写最简单版本？
- answer: 常见做法是使用 `SET key value NX EX seconds` 实现“只在 key 不存在时加锁，并同时设置过期时间”。释放锁时不能直接删 key，而应该校验锁值是不是自己，再通过 Lua 脚本原子释放。否则会出现误删别人的锁或死锁风险。分布式锁的关键不是“抢到锁”，而是“安全地加和安全地解”。

### 自建题 8：Redis 的过期策略有哪些
- tags: 中间件, Redis, 过期策略
- difficulty: medium
- prompt: Redis 是如何删除过期 key 的？为什么不是所有过期 key 都会立刻被删掉？
- answer: Redis 主要通过惰性删除和定期删除配合处理过期 key。惰性删除是在访问时发现过期就删除；定期删除是后台随机抽查部分 key 做过期清理。另外在内存不足时还可能触发淘汰策略。因为 Redis 要兼顾性能，不可能对所有 key 实时逐一扫描，所以过期 key 不一定会立即被删除。

### 自建题 9：Redis 如何保证高可用
- tags: 中间件, Redis, 高可用, 哨兵, 集群
- difficulty: medium
- prompt: Redis 在生产环境中通常如何实现高可用？主从、哨兵和集群分别解决什么问题？
- answer: 主从复制解决数据同步和读写分离问题；哨兵模式负责监控主从节点状态，并在主节点故障时自动完成故障转移；集群模式除了高可用，还支持数据分片和水平扩容。三者关注点不同：主从偏复制，哨兵偏故障切换，集群偏扩展和分片。

### 自建题 10：Redis 的内存淘汰策略有哪些
- tags: 中间件, Redis, 内存淘汰
- difficulty: medium
- prompt: Redis 内存满了以后会怎么处理？常见淘汰策略有哪些，生产中一般怎么选？
- answer: 当 Redis 达到 `maxmemory` 上限后，会按配置的淘汰策略处理。常见策略有 `noeviction`、`allkeys-lru`、`volatile-lru`、`allkeys-random`、LFU 等。生产中如果 Redis 主要做缓存，`allkeys-lru` 或 LFU 往往更常见，因为它们更符合热点数据保留的需求。

### 自建题 11：Redis 单线程为什么这么快
- tags: 中间件, Redis, 单线程, IO多路复用
- difficulty: easy
- prompt: Redis 核心执行模型为什么是单线程却依然很快？
- answer: Redis 快的原因主要有四点：基于内存操作、数据结构简单高效、单线程避免了锁竞争和线程切换开销、网络层使用了 I/O 多路复用。也就是说，Redis 的高性能不靠多线程算力堆出来，而是靠“少做无意义的开销”。

### 自建题 12：如何保证缓存和数据库的一致性
- tags: 中间件, Redis, 一致性
- difficulty: medium
- prompt: 缓存和数据库双写时，为什么很容易出现不一致？常见的一致性方案有哪些？
- answer: 因为更新数据库和更新缓存通常不是一个原子操作，所以在并发场景下容易出现脏数据。常见方案包括先更新数据库再删除缓存、延迟双删、异步订阅 binlog 回写缓存等。多数业务场景采用“更新数据库后删除缓存”即可，但要清楚它解决的是“最终一致”，不是绝对强一致。

### 自建题 13：Redis 的事务如何使用
- tags: 中间件, Redis, 事务, WATCH
- difficulty: medium
- prompt: Redis 事务是怎么实现的？它和传统关系型数据库事务最大的不同点是什么？
- answer: Redis 事务通过 `MULTI`、`EXEC`、`WATCH` 等命令实现。`MULTI` 后命令先入队，`EXEC` 时再顺序执行；`WATCH` 可以实现乐观锁控制。它和关系型数据库事务最大的不同点是：Redis 不提供传统意义上的事务回滚，一条命令失败不会回退前面已经成功执行的命令。

### 自建题 14：Redis 如何实现消息队列
- tags: 中间件, Redis, 消息队列, Stream
- difficulty: medium
- prompt: Redis 可以如何实现消息队列？List、Pub/Sub 和 Stream 分别适合什么场景？
- answer: 用 `List` 可以实现简单队列，用 `Pub/Sub` 可以做发布订阅，用 `Stream` 可以做更完整的消息流和消费组。`List` 简单但功能有限，`Pub/Sub` 不持久化且离线会丢消息，`Stream` 支持消费组和消息确认，能力最完整。如果业务可靠性要求高，Redis 队列通常只适合轻量场景，更复杂场景还是更推荐专业 MQ。

### 自建题 15：Redis 的慢查询如何排查
- tags: 中间件, Redis, 慢查询, slowlog
- difficulty: medium
- prompt: Redis 如果出现慢命令，通常怎么排查？
- answer: 一般会先配置 `slowlog` 阈值，再用 `slowlog get` 查看具体慢命令，分析是否存在大 key 操作、复杂度过高命令、批量数据操作过大等问题。Redis 的慢查询和关系型数据库不同，它往往不是“SQL 慢”，而是“命令本身复杂度太高或数据量太大”。

### 自建题 16：什么是大 key 问题，如何解决
- tags: 中间件, Redis, 大key
- difficulty: medium
- prompt: 什么是 Redis 大 key？它会带来哪些性能和稳定性问题？
- answer: 大 key 指 value 很大或集合元素特别多的 key，比如几 MB 的字符串、几万条成员的集合等。它会带来内存占用过高、单次操作阻塞、删除耗时长、主从同步压力大等问题。优化思路包括拆分 key、限制数据规模、压缩存储和定期清理无用数据。

### 自建题 17：Redis 如何实现限流
- tags: 中间件, Redis, 限流, 计数器, 滑动窗口
- difficulty: medium
- prompt: Redis 做接口限流时，常见实现方式有哪些？计数器法和滑动窗口法有什么区别？
- answer: 常见方式有固定窗口计数器、滑动窗口、令牌桶等。计数器法实现简单，但边界不够平滑；滑动窗口通常结合 `ZSet` 实现，更精确但复杂度更高。Redis 限流适合用在验证码、登录、短信发送、开放接口等高频访问控制场景。

### 自建题 18：Redis 集群的数据分片原理是什么
- tags: 中间件, Redis, Cluster, 哈希槽
- difficulty: medium
- prompt: Redis Cluster 是怎么做数据分片的？为什么说它不是简单地按节点平均分配 key？
- answer: Redis Cluster 使用 16384 个哈希槽分片，key 通过 CRC16 计算后映射到某个槽，再由槽归属到具体主节点。这样分片单位是“槽”而不是“节点”，好处是扩容缩容时只需要迁移部分槽位，灵活性更高。客户端访问错误节点时还会收到重定向信息。

### 自建题 19：Redis 性能优化有哪些方法
- tags: 中间件, Redis, 性能优化
- difficulty: medium
- prompt: 如果要系统性提升 Redis 性能，通常有哪些高频优化点？
- answer: 常见优化点包括避免大 key、合理设置过期时间、使用 pipeline 批量操作、避免 `keys *` 等高复杂度命令、使用连接池、设置合适的 `maxmemory` 和淘汰策略、优化热点 key 分布等。Redis 调优核心还是两件事：减少单次操作成本，减少无效网络往返。

### 自建题 20：Redis 在电商项目中通常怎么用
- tags: 中间件, Redis, 项目实战
- difficulty: easy
- prompt: 如果面试官问 Redis 在你们电商项目里具体怎么用，你可以从哪些典型场景展开回答？
- answer: 常见回答可以围绕商品详情缓存、用户 Session 共享、秒杀库存预扣减、分布式锁、计数器、排行榜等场景展开。关键不是只说“用了 Redis”，而是说清楚为什么选 Redis、解决了什么问题、带来了什么效果，以及是否遇到过缓存一致性、击穿或大 key 等实际问题。

### 自建题 21：什么是消息队列，有什么作用
- tags: 中间件, MQ, 高频
- difficulty: easy
- prompt: 请解释什么是消息队列，并说明它在系统设计中通常解决哪些问题。
- answer: 消息队列是一种异步通信机制，生产者把消息发送到队列，消费者异步获取并处理。它主要解决三类问题：异步处理提升响应速度、削峰填谷缓冲突发流量、系统解耦降低模块间直接依赖。很多高并发场景下，MQ 的价值不是“能发消息”，而是“能把系统从同步重链路改成异步松耦合链路”。

### 自建题 22：常见消息队列有哪些，它们有什么区别
- tags: 中间件, MQ, Kafka, RabbitMQ, RocketMQ
- difficulty: easy
- prompt: 常见的消息队列中，Kafka、RabbitMQ、RocketMQ 分别更适合什么场景？
- answer: Kafka 吞吐量高，适合日志、埋点、大数据流式处理等高吞吐场景；RabbitMQ 功能丰富、路由灵活，更适合业务消息和可靠性要求高的场景；RocketMQ 在事务消息、延迟消息、顺序消息等方面能力较强，比较适合电商业务链路。面试时最好不要只背“谁快谁慢”，还要能说出“为什么场景不同选择不同”。

### 自建题 23：消息队列如何保证消息不丢失
- tags: 中间件, MQ, 消息不丢失
- difficulty: medium
- prompt: 如果面试官问你“MQ 如何保证消息不丢失”，你通常会从哪几个环节来回答？
- answer: 一般会从生产者、Broker、消费者三个环节回答。生产者端要有发送确认和失败重试；Broker 端要做消息持久化和副本冗余；消费者端要在处理成功后再确认消费位点，失败时支持重试。MQ 可靠性不能只盯某一层，而是要看整条链路上的可靠投递和可靠消费。

### 自建题 24：消息队列如何保证消息不重复消费
- tags: 中间件, MQ, 幂等性
- difficulty: medium
- prompt: 为什么 MQ 很难天然做到“绝对不重复消费”？业务上通常如何解决重复消费问题？
- answer: 因为在网络抖动、消费失败重试、位点提交异常等场景下，MQ 很容易出现“至少一次”投递，从而带来重复消费。所以业务侧通常通过幂等性设计兜底，比如基于业务唯一 ID 去重、数据库唯一索引、状态机校验或 Redis 记录已处理消息。核心思路不是强行避免所有重复，而是让重复消费不会出错。

### 自建题 25：什么是消息积压，如何解决
- tags: 中间件, MQ, 消息积压
- difficulty: medium
- prompt: 如果队列中的消息越积越多，通常意味着什么？常见处理手段有哪些？
- answer: 消息积压通常说明生产速度大于消费速度，或者某一类消费者异常变慢。常见处理方式包括增加消费者实例、增加分区或队列并行度、优化消费逻辑、批量消费、把慢外部调用异步化，必要时还要做限流和临时扩容。处理积压时要先分清是“消费能力不够”还是“消费链路出问题”。

### 自建题 26：消息队列如何保证消息顺序性
- tags: 中间件, MQ, 顺序消息
- difficulty: medium
- prompt: 如果某类业务消息必须按顺序处理，通常如何在 MQ 中实现顺序消费？
- answer: 核心思路是让同一业务主键的消息进入同一个分区或队列，并保证该分区在消费侧按顺序串行处理。比如可以按订单号做 hash 路由到固定分区，再由单消费者或单线程顺序消费。需要注意，顺序性通常会牺牲并行度和吞吐量，所以要按业务粒度而不是全局强顺序来设计。

### 自建题 27：什么是死信队列，如何使用
- tags: 中间件, MQ, 死信队列
- difficulty: easy
- prompt: 什么是死信队列？为什么不能让消费失败的消息无限重试？
- answer: 死信队列是用来存放多次消费失败、过期或被拒绝处理的消息的特殊队列。它的作用是把异常消息隔离出去，避免一直阻塞正常消息流。无限重试不仅不能解决问题，还可能让系统一直卡在同一批坏消息上，所以通常会设置最大重试次数，超过后转入死信队列再人工或补偿处理。

### 自建题 28：什么是延迟消息，如何实现
- tags: 中间件, MQ, 延迟消息
- difficulty: medium
- prompt: 延迟消息是什么？订单超时取消这类场景通常可以怎么实现？
- answer: 延迟消息指消息发送后不会立即被消费，而是等到指定时间后再投递给消费者。实现方式可以依赖 MQ 原生延迟能力，也可以用 Redis 的 ZSet 加定时扫描、或借助时间轮等方案实现。像订单超时未支付自动取消，就是延迟消息的典型场景。

### 自建题 29：消息队列如何实现高可用
- tags: 中间件, MQ, 高可用, 副本
- difficulty: medium
- prompt: MQ 集群通常如何设计高可用？为什么副本和故障切换都很关键？
- answer: MQ 高可用一般依赖集群部署、多副本机制和自动故障转移。副本保证某台机器宕机后数据不至于丢失，故障切换保证服务还能继续对外提供能力。真正的高可用不只是“节点多”，而是“节点挂了以后数据还在、服务还能继续用”。

### 自建题 30：Kafka 的分区和副本是什么
- tags: 中间件, Kafka, 分区, 副本
- difficulty: easy
- prompt: Kafka 中分区和副本分别是什么概念？它们分别解决什么问题？
- answer: 分区是 Topic 的并行存储和消费单元，主要解决吞吐量和并发扩展问题；副本是分区的数据冗余拷贝，主要解决可靠性和高可用问题。简单理解：分区负责“快”，副本负责“稳”。

### 自建题 31：Kafka 如何保证高吞吐量
- tags: 中间件, Kafka, 高吞吐
- difficulty: medium
- prompt: Kafka 为什么能支撑很高的吞吐量？常见原因有哪些？
- answer: Kafka 高吞吐主要来自顺序写磁盘、零拷贝、批量发送、消息压缩和分区并行。它并不是靠单条消息处理很快，而是靠整套链路把磁盘写入、网络传输和并发处理的成本降到更低。面试里如果能把这几个点连起来讲，通常会比较完整。

### 自建题 32：什么是消费者组，有什么作用
- tags: 中间件, Kafka, 消费者组
- difficulty: easy
- prompt: Kafka 中消费者组是什么？它为什么既能实现负载均衡，又能实现一份消息被多个业务分别消费？
- answer: 消费者组是 Kafka 的消费管理单位。组内多个消费者共享一个 Topic 的分区，实现负载均衡；不同消费者组之间互不影响，每个组都能独立消费同一份消息。这样一份订单消息可以被订单系统、库存系统、积分系统分别消费，但在每个组内部又不会重复消费同一个分区。

### 自建题 33：offset 是什么，如何管理
- tags: 中间件, Kafka, offset
- difficulty: medium
- prompt: Kafka 的 offset 是什么？自动提交和手动提交分别有什么优缺点？
- answer: offset 可以理解为消费者在某个分区里的消费位置。自动提交实现简单，但可能在消息还没真正处理完时就提交，带来丢消息风险；手动提交更安全，可以确保处理成功后再提交，但需要业务自己更谨慎地控制提交流程。生产环境中，关键业务通常更偏向手动提交加幂等控制。

### 自建题 34：如何监控消息队列的健康状态
- tags: 中间件, MQ, 监控, Lag
- difficulty: medium
- prompt: 监控 MQ 时，通常最关键的几个指标是什么？为什么消息堆积量和消费延迟特别重要？
- answer: 常见关键指标包括消息堆积量（Lag）、消费延迟、消费者存活状态、Broker 资源使用率、分区副本状态等。堆积量大说明消费赶不上生产，消费延迟高说明业务已经开始感知滞后。它们往往比单纯看 CPU 或 TPS 更能直接反映消息系统是否健康。

### 自建题 35：推模式和拉模式有什么区别
- tags: 中间件, MQ, push, pull
- difficulty: medium
- prompt: MQ 的推模式和拉模式分别是什么？为什么 Kafka 采用拉模式？
- answer: 推模式由 Broker 主动把消息推给消费者，实时性好，但容易压垮处理能力弱的消费者；拉模式由消费者主动拉取消息，更容易按自身处理能力控制节奏，也更适合批量拉取。Kafka 采用拉模式，核心就是把消费节奏控制权交给消费者，从而更利于高吞吐和批量处理。

### 自建题 36：什么是事务消息，如何使用
- tags: 中间件, MQ, 事务消息
- difficulty: hard
- prompt: 什么是事务消息？它通常解决的是哪类分布式一致性问题？
- answer: 事务消息主要用于保证“本地事务执行结果”和“消息是否投递成功”之间的一致性，避免出现本地业务成功但消息没发出去，或者消息发出去了但本地事务失败的问题。它常用于订单创建、库存扣减、状态变更通知等场景。本质上是在分布式场景下协调业务状态和消息状态的一致性。

### 自建题 37：如何设计一个高可用的消息队列架构
- tags: 中间件, MQ, 架构设计, 高可用
- difficulty: hard
- prompt: 如果让你设计一个高可用的 MQ 架构，你会重点考虑哪些方面？
- answer: 我会重点考虑集群部署、分区和副本策略、生产者确认和重试、消费者幂等和位点提交、监控告警、死信队列和故障恢复机制。高可用设计不能只关注“服务别挂”，还要关注“消息别丢、消费别乱、恢复要快、异常可观测”。

### 自建题 38：消息队列的性能优化有哪些方法
- tags: 中间件, MQ, 性能优化
- difficulty: medium
- prompt: 如果要提升 MQ 的整体吞吐量和消费效率，通常有哪些高频优化手段？
- answer: 常见优化方式包括批量发送、批量消费、异步发送、消息压缩、增加分区数、优化消费者处理逻辑、减少阻塞调用、合理配置线程池和网络参数。MQ 优化本质上还是在减少网络往返、提高并行度、缩短单条消息处理耗时。

### 自建题 39：如何处理消费失败的消息
- tags: 中间件, MQ, 重试, 死信队列
- difficulty: medium
- prompt: 如果消费者处理消息失败，通常有哪些常见处理策略？
- answer: 常见策略包括立即重试、延迟重试、达到上限后转死信队列、记录日志并告警、后续人工补偿或自动补偿。关键是要区分“偶发失败”和“确定性失败”：前者适合重试，后者不能无限重试，否则只会不断放大问题。

### 自建题 40：MQ 在电商项目中通常怎么用
- tags: 中间件, MQ, 项目实战
- difficulty: easy
- prompt: 如果面试官问你 MQ 在电商项目中具体有哪些落地场景，你可以从哪些方面回答？
- answer: 常见场景包括订单异步处理、秒杀削峰、库存扣减解耦、短信和积分异步发放、订单状态变更通知、数据同步到搜索或数仓系统等。回答时最好按“业务场景 → 为什么用 MQ → 带来了什么收益 → 做过哪些可靠性设计”这条思路展开，会更像真实项目经验。

## 数据库面试题

### 自建题 1：什么是数据库、DBMS 和 SQL？它们之间有什么关系
- tags: 数据库, DBMS, SQL, 基础理论, 高频
- difficulty: easy
- prompt: 请解释什么是数据库、DBMS 和 SQL，并说明三者之间的关系。
- answer: 数据库是有组织存储数据的集合；DBMS 是用来创建、管理和操作数据库的软件，例如 MySQL、Oracle、SQL Server；SQL 是和数据库通信的结构化查询语言。三者关系可以理解为：用户通过 SQL，借助 DBMS，去访问和管理数据库中的数据。

### 自建题 2：SQL 语言主要分为哪几类
- tags: 数据库, SQL分类, DDL, DML, DCL, TCL
- difficulty: easy
- prompt: SQL 语言通常分为哪几类？每一类分别用于做什么？
- answer: SQL 通常分为四类：DDL 用于定义数据库结构，例如 `CREATE`、`ALTER`、`DROP`；DML 用于增删改查数据，例如 `SELECT`、`INSERT`、`UPDATE`、`DELETE`；DCL 用于权限控制，例如 `GRANT`、`REVOKE`；TCL 用于事务控制，例如 `COMMIT`、`ROLLBACK`、`SAVEPOINT`。

### 自建题 3：CHAR 和 VARCHAR 数据类型有什么区别
- tags: 数据库, CHAR, VARCHAR, 数据类型
- difficulty: easy
- prompt: 数据库里 `CHAR` 和 `VARCHAR` 有什么区别？从存储方式和适用场景两个角度说明。
- answer: `CHAR` 是定长字符串，长度不足会自动补空格，读取速度通常更稳定，但可能浪费空间；`VARCHAR` 是变长字符串，只占用实际长度加额外长度标记，节省空间，但处理上会稍复杂一些。通常长度固定的数据更适合 `CHAR`，长度变化明显的数据更适合 `VARCHAR`。

### 自建题 4：DELETE、TRUNCATE 和 DROP 有什么区别
- tags: 数据库, DELETE, TRUNCATE, DROP
- difficulty: easy
- prompt: 请说明 `DELETE`、`TRUNCATE` 和 `DROP` 的区别。
- answer: `DELETE` 是 DML，删除表中的部分或全部数据，通常可回滚，且不会默认重置自增 ID；`TRUNCATE` 是 DDL，用于快速清空整张表，通常不可回滚，并会重置自增 ID；`DROP` 是 DDL，直接删除整张表的结构和数据。三者差别核心在于：删数据、清空表、删表本身。

### 自建题 5：WHERE 和 HAVING 子句的区别是什么
- tags: 数据库, WHERE, HAVING, GROUP BY
- difficulty: easy
- prompt: SQL 中 `WHERE` 和 `HAVING` 有什么区别？为什么 `HAVING` 常和 `GROUP BY` 一起使用？
- answer: `WHERE` 是在分组前过滤数据，不能直接对聚合结果做过滤；`HAVING` 是在分组后过滤结果，通常和 `GROUP BY` 配合使用，并且可以使用聚合函数，比如 `COUNT()`、`SUM()`。简单记就是：`WHERE` 过滤原始行，`HAVING` 过滤分组后的结果。

### 自建题 6：INNER JOIN 和 OUTER JOIN 的区别
- tags: 数据库, JOIN, INNER JOIN, OUTER JOIN
- difficulty: easy
- prompt: 请解释 `INNER JOIN` 和 `OUTER JOIN` 的区别，并说明 `LEFT JOIN`、`RIGHT JOIN`、`FULL JOIN` 的含义。
- answer: `INNER JOIN` 只返回两个表中能够匹配上的记录，也就是交集；外连接则除了匹配记录外，还会保留一侧或两侧未匹配的数据。`LEFT JOIN` 保留左表全部数据，`RIGHT JOIN` 保留右表全部数据，`FULL JOIN` 只要任意一侧有匹配就返回，类似并集效果。

### 自建题 7：如何查询表中存在重复值的记录
- tags: 数据库, GROUP BY, HAVING, 重复数据
- difficulty: easy
- prompt: 如果要查出某个字段存在重复值的记录，通常怎么写 SQL？
- answer: 常见做法是先按该字段 `GROUP BY`，再用 `HAVING COUNT(*) > 1` 找出重复值。例如 `SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > 1;`。如果要进一步查出完整重复记录，可以再结合子查询或 JOIN 把这些重复值关联回来。

### 自建题 8：如何从数据库中随机获取 N 条记录
- tags: 数据库, 随机取数, RAND
- difficulty: easy
- prompt: 如何从数据库中随机获取 N 条记录？不同数据库常见写法有什么差异？
- answer: 不同数据库写法不同。MySQL 常用 `ORDER BY RAND() LIMIT N`，SQL Server 常用 `ORDER BY NEWID()`，Oracle 可以用 `DBMS_RANDOM.VALUE`。但要注意，这类全表随机排序在大数据量场景下性能不高，面试时最好顺带提一句性能问题。

### 自建题 9：什么是子查询？有哪些类型
- tags: 数据库, 子查询, SQL
- difficulty: easy
- prompt: 什么是子查询？常见的子查询类型有哪些？
- answer: 子查询就是嵌套在另一个 SQL 查询中的查询。常见类型包括标量子查询（返回单个值）、行子查询（返回单行多列）、列子查询（返回单列多行）和表子查询（返回一个临时结果集，可在 `FROM` 中当虚拟表使用）。

### 自建题 10：UNION 和 UNION ALL 有什么区别
- tags: 数据库, UNION, UNION ALL
- difficulty: easy
- prompt: `UNION` 和 `UNION ALL` 有什么区别？为什么通常说 `UNION ALL` 性能更高？
- answer: `UNION` 会合并结果集并自动去重，因此通常会有额外排序或去重开销；`UNION ALL` 直接把两个结果集合并，不去重，所以性能通常更高。选择哪一个，关键看业务上是否需要去重。

### 自建题 11：什么是数据库事务？它的 ACID 属性是什么
- tags: 数据库, 事务, ACID, 高频
- difficulty: easy
- prompt: 请解释什么是数据库事务，并说明 ACID 四个属性分别代表什么。
- answer: 事务是一组要么全部成功、要么全部失败的数据库操作集合。ACID 分别是：原子性，事务不可分割；一致性，事务执行前后数据要保持一致；隔离性，并发事务之间互不干扰；持久性，事务提交后结果永久生效。

### 自建题 12：事务的隔离级别有哪些？分别解决了哪些并发问题
- tags: 数据库, 事务隔离级别, 并发问题
- difficulty: medium
- prompt: 数据库事务常见隔离级别有哪些？它们分别能解决哪些并发问题？
- answer: 常见隔离级别有读未提交、读已提交、可重复读、串行化。读未提交几乎不解决并发一致性问题；读已提交解决脏读；可重复读解决脏读和不可重复读；串行化解决脏读、不可重复读和幻读，但性能最低。面试里要注意“隔离越强，性能通常越差”。

### 自建题 13：什么是脏读、不可重复读和幻读
- tags: 数据库, 脏读, 不可重复读, 幻读
- difficulty: medium
- prompt: 请解释数据库中的脏读、不可重复读和幻读分别是什么。
- answer: 脏读是一个事务读到了另一个事务未提交的数据；不可重复读是同一个事务内多次读取同一条记录，结果因别的事务提交更新而变化；幻读是同一个事务多次按范围查询时，结果集中多出了原来没有的行，通常是其他事务插入导致的。

### 自建题 14：什么是索引？它的作用和优缺点是什么
- tags: 数据库, 索引, 查询优化
- difficulty: easy
- prompt: 请解释什么是数据库索引，并说明它的作用、优点和缺点。
- answer: 索引可以理解为数据库的目录结构，用来提高数据检索效率。优点是能显著提升查询性能；缺点是会占用额外空间，并且会增加 `INSERT`、`UPDATE`、`DELETE` 的维护成本，因为索引本身也要同步更新。

### 自建题 15：哪些字段适合创建索引
- tags: 数据库, 索引设计, WHERE, JOIN
- difficulty: easy
- prompt: 哪些字段通常比较适合创建索引？
- answer: 常见适合建索引的字段包括主键、外键、经常出现在 `WHERE` 条件中的字段、经常参与 `JOIN` 的字段，以及常用于 `ORDER BY`、`GROUP BY` 的字段。核心原则是：查询里经常被高频用来筛选或关联的字段，才更值得建索引。

### 自建题 16：索引是不是越多越好？为什么
- tags: 数据库, 索引, 性能平衡
- difficulty: easy
- prompt: 索引是不是越多越好？为什么数据库设计里不能盲目加索引？
- answer: 索引不是越多越好。因为索引会占空间，也会增加写入、更新、删除时的维护成本。索引设计本质上是在“读性能提升”和“写性能下降”之间做平衡，所以要结合实际查询场景，而不是机械地多建索引。

### 自建题 17：什么是聚簇索引和非聚簇索引
- tags: 数据库, 聚簇索引, 非聚簇索引
- difficulty: medium
- prompt: 请解释聚簇索引和非聚簇索引的区别。
- answer: 聚簇索引决定了数据在磁盘上的物理存储顺序，所以一张表通常只能有一个聚簇索引；非聚簇索引则不改变数据物理顺序，只保存索引顺序和数据行定位信息，因此一张表可以有多个非聚簇索引。简单理解：聚簇索引更像“数据本体按索引排好序”，非聚簇索引更像“额外建了一本目录”。

### 自建题 18：如何判断一条 SQL 查询是否使用了索引
- tags: 数据库, EXPLAIN, 执行计划, 索引命中
- difficulty: medium
- prompt: 如果想判断一条 SQL 是否使用了索引，通常应该怎么做？
- answer: 常见做法是使用 `EXPLAIN` 查看执行计划。在 MySQL 中可以重点关注 `key` 字段是否命中索引，以及 `type` 字段的访问方式，例如 `ref`、`range` 通常比 `ALL` 更好。面试里如果能顺带提到 `rows`、`extra`，会更完整。

### 自建题 19：什么是数据库范式
- tags: 数据库, 范式, 1NF, 2NF, 3NF
- difficulty: medium
- prompt: 什么是数据库范式？第一、第二、第三范式分别强调什么？
- answer: 范式是关系数据库设计时用于减少冗余、提高一致性的规范。第一范式要求字段原子不可再分；第二范式要求在满足 1NF 的基础上，非主键字段完全依赖整个主键；第三范式要求在满足 2NF 的基础上，非主键字段之间不能存在传递依赖。

### 自建题 20：什么是数据库死锁？如何避免
- tags: 数据库, 死锁, 事务
- difficulty: medium
- prompt: 什么是数据库死锁？在实际开发中通常如何避免或缓解死锁问题？
- answer: 死锁是多个事务互相等待对方持有的资源，导致谁也无法继续执行的状态。常见规避方式包括按统一顺序访问资源、缩短事务时间、及时提交事务、降低隔离级别、以及在应用层对死锁异常做重试机制。

### 自建题 21：主键和外键的作用是什么
- tags: 数据库, 主键, 外键, 参照完整性
- difficulty: easy
- prompt: 主键和外键分别有什么作用？为什么说外键有助于保证参照完整性？
- answer: 主键用于唯一标识表中的一条记录，不能为空且必须唯一；外键用于建立表与表之间的关联，引用另一张表的主键或唯一键。外键的核心作用是约束数据关系，避免出现引用了不存在数据的“脏关联”。

### 自建题 22：什么是存储过程？它有什么优缺点
- tags: 数据库, 存储过程
- difficulty: medium
- prompt: 什么是存储过程？从性能、维护和移植性角度看，它有哪些优缺点？
- answer: 存储过程是一组为了完成特定功能而预先编译并保存在数据库中的 SQL 语句集合。优点包括执行效率高、减少网络传输、权限控制更集中；缺点包括调试困难、数据库耦合高、跨数据库移植性差、业务逻辑可能分散难维护。

### 自建题 23：什么是触发器？它的作用是什么
- tags: 数据库, 触发器, 审计
- difficulty: easy
- prompt: 什么是触发器？它通常用在什么场景？
- answer: 触发器是一种特殊的数据库程序，会在 `INSERT`、`UPDATE`、`DELETE` 等事件发生前后自动执行。常见用途包括实现审计日志、自动补充字段、执行业务规则检查、保持数据一致性等。但触发器逻辑过重时，也可能增加维护和性能负担。

### 自建题 24：从测试角度，如何测试存储过程和触发器
- tags: 数据库, 测试, 存储过程, 触发器
- difficulty: medium
- prompt: 从测试工程师角度，存储过程和触发器分别应该怎么测？
- answer: 存储过程重点测试输入输出参数、边界值、异常分支和业务逻辑是否正确；触发器重点验证指定事件是否真的触发了逻辑，以及触发后数据状态、日志、性能是否符合预期。数据库对象测试不仅要看结果对不对，还要关注副作用和性能影响。

### 自建题 25：如何备份和恢复数据库
- tags: 数据库, 备份, 恢复, mysqldump
- difficulty: easy
- prompt: 数据库常见备份和恢复方式有哪些？从测试角度应重点关注什么？
- answer: 常见备份方式包括完全备份、差异备份和事务日志备份；恢复方式则取决于备份策略和恢复目标时间点。像 MySQL 常用 `mysqldump` 等工具。对测试来说，除了知道怎么备份，更要验证恢复流程能否真正执行成功，以及恢复后的数据完整性和可用性是否符合预期。

### 自建题 26：作为测试工程师，你在进行数据库测试时主要关注哪些方面
- tags: 数据库, 数据库测试, 高频
- difficulty: medium
- prompt: 作为测试工程师，做数据库测试时通常会重点关注哪些方面？
- answer: 主要关注六个方面。数据完整性要看主键、外键、唯一约束、非空约束是否生效；数据准确性要看 CRUD 后数据是否按预期落库和更新；业务规则要验证存储过程、触发器、函数中的复杂逻辑；性能要关注 SQL 效率、索引有效性、慢查询和死锁；安全性要关注权限控制和 SQL 注入；并发性要关注多用户同时操作时是否会出现数据不一致。

### 自建题 27：如何设计测试用例来验证数据库的完整性
- tags: 数据库, 完整性, 测试设计
- difficulty: medium
- prompt: 如果要验证数据库完整性，测试用例通常应该怎么设计？
- answer: 可以从实体完整性、参照完整性和域完整性三个方向设计用例。实体完整性可以尝试插入重复主键或空主键，预期失败；参照完整性可以尝试删除被外键引用的主表记录，或插入不存在的外键值；域完整性可以尝试插入超长字符串、错误类型或违反 CHECK 约束的值，预期都应失败。核心是验证约束是否真的在数据库层生效。

### 自建题 28：什么是 SQL 注入，如何在测试中发现它
- tags: 数据库, SQL注入, 安全测试
- difficulty: medium
- prompt: 什么是 SQL 注入？在测试中通常如何发现这类问题？
- answer: SQL 注入是攻击者把恶意 SQL 片段拼进输入参数里，诱导服务器执行非预期 SQL 的漏洞。测试时可以在输入框、URL 参数、Cookie 等位置尝试特殊字符和注入片段，比如单引号、逻辑恒真表达式或注释符，并观察页面返回、错误信息和数据是否出现异常。发现明显数据库报错、结果集异常扩大，或非预期数据变化时，就要重点怀疑注入风险。

### 自建题 29：如何测试数据库的性能
- tags: 数据库, 性能测试, 慢查询
- difficulty: medium
- prompt: 如果要测试数据库性能，通常应该关注哪些指标和方法？
- answer: 可以使用 JMeter、LoadRunner 等工具模拟并发请求，同时监控数据库服务器的 CPU、内存、磁盘 I/O、网络流量和连接数。还要开启慢查询日志，结合 `EXPLAIN` 分析执行计划，找出全表扫描、索引失效或回表过多等问题。通常还会做不同负载下的基准测试，观察吞吐量和响应时间的变化。

### 自建题 30：你如何验证一个前端操作是否成功写入了数据库
- tags: 数据库, 数据验证, 联调
- difficulty: easy
- prompt: 前端做了新增、修改或删除操作后，你通常如何验证数据库里真的生效了？
- answer: 最直接的方法就是在前端操作后，使用数据库客户端或命令行直接查询相关表，确认数据是否按业务预期变化。比如新增后检查记录是否存在，修改后检查字段值是否更新，删除后检查记录是否消失。这样可以绕过前端页面表现，直接验证最终数据状态。

### 自建题 31：什么是数据迁移测试，需要注意什么
- tags: 数据库, 数据迁移, 测试
- difficulty: medium
- prompt: 什么是数据迁移测试？做这类测试时通常需要注意什么？
- answer: 数据迁移测试是验证数据从一个系统或数据库迁移到另一个系统或数据库的过程是否正确。重点要看数据是否完整、字段映射是否准确、迁移后是否满足新系统约束，以及迁移后的业务功能和性能是否正常。还要特别关注迁移窗口、回滚方案和数据一致性问题。

### 自建题 32：如何测试数据库的并发问题
- tags: 数据库, 并发, JMeter
- difficulty: medium
- prompt: 如果要验证数据库在并发场景下的表现，通常应该如何设计测试？
- answer: 可以通过多线程或 JMeter 等工具模拟多个用户同时执行相同或相关操作，例如同时抢购库存、同时更新同一条记录。测试时要重点检查最终数据是否正确、是否出现脏读不可重复读幻读、是否有死锁、以及系统在高并发下的稳定性和吞吐表现。

### 自建题 33：遇到过慢查询吗？你是如何协助分析的
- tags: 数据库, 慢查询, EXPLAIN, 排查
- difficulty: medium
- prompt: 如果线上或测试环境里出现慢查询，你通常会如何协助分析和处理？
- answer: 通常先通过慢查询日志或 APM 定位具体 SQL，再用 `EXPLAIN` 或 `EXPLAIN ANALYZE` 看执行计划，重点关注是否全表扫描、索引是否合理、扫描行数是否过多。接着会建议优化 SQL 写法、增加合适索引，必要时和开发一起评估业务逻辑是否要调整或做数据归档。

### 自建题 34：简述一下你使用过的数据库工具
- tags: 数据库, 工具, 高频
- difficulty: easy
- prompt: 你常用的数据库相关工具有哪些？分别适合做什么？
- answer: 常见数据库客户端或管理工具有 Navicat、DBeaver、MySQL Workbench、SSMS、pgAdmin、Oracle SQL Developer。做性能监控时可以结合 Prometheus + Grafana，分析 MySQL 慢日志时可以用 pt-query-digest。命令行工具也很常见，比如 `mysql` 和 `psql`。测试框架里则通常通过 JDBC、ODBC、MyBatis、Hibernate 等方式验证数据库结果。

### 自建题 35：什么是连接池？它对性能有什么影响
- tags: 数据库, 连接池, 性能优化
- difficulty: medium
- prompt: 什么是数据库连接池？它对系统性能有什么影响？
- answer: 连接池是预先创建并统一管理数据库连接的机制，应用需要连接时直接从池里取，用完再归还，而不是每次都重新建立连接。它能显著减少频繁创建和关闭连接带来的网络握手、认证和资源开销，因此对性能提升非常明显。

### 自建题 36：乐观锁和悲观锁的区别
- tags: 数据库, 乐观锁, 悲观锁
- difficulty: medium
- prompt: 乐观锁和悲观锁有什么区别？分别适合什么场景？
- answer: 悲观锁假定并发冲突很常见，所以会先上锁再操作，例如 `SELECT ... FOR UPDATE`；乐观锁假定冲突较少，通常在更新时通过版本号或时间戳检测是否被修改。悲观锁适合写冲突严重的场景，乐观锁更适合读多写少、冲突较少的场景。

### 自建题 37：什么是数据库的读写分离，它解决了什么问题
- tags: 数据库, 读写分离, 架构
- difficulty: medium
- prompt: 什么是读写分离？它通常解决哪些数据库层面的问题？
- answer: 读写分离是把写操作交给主库，读操作交给一个或多个从库，从而减轻主库压力并提升整体读性能。它常用于读多写少的业务场景，也能提升系统可扩展性和可用性。不过它需要处理主从延迟和数据一致性问题。

### 自建题 38：如何在 Linux 环境下连接并操作数据库
- tags: 数据库, Linux, 命令行
- difficulty: easy
- prompt: 在 Linux 环境下，通常如何连接数据库并执行 SQL？
- answer: 以 MySQL 为例，可以使用 `mysql -h hostname -u username -p` 连接数据库，然后在命令行里直接执行 SQL。也可以通过 `mysql -u username -p database_name < file.sql` 的方式执行 SQL 文件。其他数据库通常也有各自的命令行客户端。

### 自建题 39：作为测试工程师，你为什么认为数据库知识很重要
- tags: 数据库, 测试工程师, 高频
- difficulty: easy
- prompt: 为什么测试工程师需要掌握数据库知识？请从定位问题、验证数据和性能分析几个角度回答。
- answer: 数据库知识很重要，因为很多前端表现出来的问题本质上都和数据库相关，掌握数据库能更快定位 Bug 来源。它也能帮助验证数据是否真正落地、是否满足业务规则，并且在性能分析时协助发现慢查询、索引问题或事务并发问题。对测试工程师来说，数据库能力直接影响问题定位深度和质量。

### 自建题 40：什么是触发器？它的作用是什么
- tags: 数据库, 触发器, 审计
- difficulty: easy
- prompt: 什么是触发器？它通常用于哪些场景？
- answer: 触发器是一种在 `INSERT`、`UPDATE`、`DELETE` 等事件发生前或后自动执行的数据库对象。它常用于强制业务规则、记录审计日志、自动更新派生字段、或在某些场景下同步数据。触发器能力强，但也要注意性能和维护成本。

### 自建题 41：如何查询一张表的所有数据
- tags: 数据库, SQL, SELECT, 基础
- difficulty: easy
- prompt: 如何查询一张表的所有数据？请写出最基础的 SQL。
- answer: 最基础的写法是 `SELECT * FROM 表名;`。例如 `SELECT * FROM employees;` 会返回 `employees` 表中的所有行和所有列。这里的 `*` 代表所有列。

### 自建题 42：如何查询特定的列
- tags: 数据库, SQL, SELECT, 列查询
- difficulty: easy
- prompt: 如果只想查询表中的部分列，SQL 应该怎么写？
- answer: 在 `SELECT` 后指定需要的列名即可，多个列用逗号分隔。例如 `SELECT first_name, last_name, email FROM employees;`，这样只会返回姓名和邮箱列。

### 自建题 43：如何使用 WHERE 子句过滤数据
- tags: 数据库, SQL, WHERE, 过滤
- difficulty: easy
- prompt: `WHERE` 子句有什么作用？请举例说明。
- answer: `WHERE` 用于给查询增加过滤条件，只返回满足条件的数据。例如 `SELECT * FROM employees WHERE department_id = 10;` 表示查询部门 ID 为 10 的员工，`WHERE salary > 50000` 表示查询薪资大于 5 万的员工。

### 自建题 44：如何查询满足多个条件的数据
- tags: 数据库, SQL, WHERE, AND, OR
- difficulty: easy
- prompt: 如果查询条件不止一个，通常如何组合多个条件？
- answer: 可以使用 `AND` 或 `OR` 连接多个条件。`AND` 表示所有条件都要满足，`OR` 表示满足任意一个即可。例如 `SELECT * FROM employees WHERE department_id = 10 AND salary > 50000;` 表示查询部门 10 中薪资超过 5 万的员工。

### 自建题 45：如何对查询结果排序
- tags: 数据库, SQL, ORDER BY, 排序
- difficulty: easy
- prompt: 查询结果如果要按某个字段排序，应该怎么写？
- answer: 使用 `ORDER BY` 子句。升序用 `ASC`，降序用 `DESC`，其中升序通常可以省略。例如 `SELECT * FROM employees ORDER BY salary DESC;` 表示按薪资从高到低排序；也可以多字段排序，如 `ORDER BY last_name ASC, first_name ASC`。

### 自建题 46：如何去除查询结果中的重复行
- tags: 数据库, SQL, DISTINCT, 去重
- difficulty: easy
- prompt: 如何把查询结果中的重复值去掉？
- answer: 可以使用 `DISTINCT` 关键字。例如 `SELECT DISTINCT department_id FROM employees;` 表示查询所有不重复的部门 ID。它常用于去重场景，但也要注意大数据量时的性能开销。

### 自建题 47：如何使用 LIKE 进行模糊查询
- tags: 数据库, SQL, LIKE, 模糊查询
- difficulty: easy
- prompt: `LIKE` 一般怎么用？`%` 和 `_` 分别表示什么？
- answer: `LIKE` 用于模糊匹配。`%` 表示匹配任意多个字符，`_` 表示匹配任意一个字符。例如 `last_name LIKE 'S%'` 表示姓氏以 S 开头，`LIKE '%son'` 表示以 son 结尾，`LIKE '_a%'` 表示第二个字母是 a。

### 自建题 48：如何查询值在某个列表中的数据
- tags: 数据库, SQL, IN
- difficulty: easy
- prompt: 如果要查询字段值属于某个列表的数据，SQL 应该怎么写？
- answer: 可以使用 `IN` 操作符。例如 `SELECT * FROM employees WHERE department_id IN (10, 20, 30);` 表示查询部门 ID 为 10、20、30 的员工。相比写多个 `OR`，这种写法更简洁。

### 自建题 49：如何查询值在两个值之间的数据
- tags: 数据库, SQL, BETWEEN
- difficulty: easy
- prompt: 如果要查询某个字段在一个区间范围内的数据，通常怎么写？
- answer: 可以使用 `BETWEEN ... AND ...`。例如 `SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;` 表示查询薪资在 4 万到 6 万之间的员工，并且包含边界值。

### 自建题 50：如何查询为 NULL 的值
- tags: 数据库, SQL, NULL
- difficulty: easy
- prompt: 数据库中如果要查询某个字段为空的记录，为什么不能直接写 `= NULL`？正确写法是什么？
- answer: 因为 `NULL` 不是普通值，不能直接用 `=` 判断。正确写法是 `IS NULL` 或 `IS NOT NULL`。例如 `SELECT * FROM employees WHERE manager_id IS NULL;` 表示查询没有经理的员工。

### 自建题 51：如何使用 LIMIT 限制返回的行数
- tags: 数据库, SQL, LIMIT
- difficulty: easy
- prompt: 如果只想返回查询结果中的前几行数据，通常怎么写？
- answer: 在 MySQL 中通常使用 `LIMIT` 子句。例如 `SELECT * FROM employees ORDER BY salary DESC LIMIT 5;` 表示返回薪资最高的前 5 名员工。不同数据库写法略有差异，比如 Oracle 里常用 `ROWNUM` 或 `FETCH FIRST n ROWS ONLY`。

### 自建题 52：如何使用 COUNT 函数计数
- tags: 数据库, SQL, COUNT, 聚合函数
- difficulty: easy
- prompt: `COUNT(*)` 和 `COUNT(column_name)` 有什么区别？
- answer: `COUNT(*)` 统计所有行数，不管字段是不是 `NULL`；`COUNT(column_name)` 只统计该列非 `NULL` 的行数。例如 `COUNT(manager_id)` 只会统计有经理 ID 的员工数量，不会把 `NULL` 算进去。

### 自建题 53：还有哪些常用的聚合函数
- tags: 数据库, SQL, 聚合函数, SUM, AVG, MAX, MIN
- difficulty: easy
- prompt: 除了 `COUNT` 以外，SQL 里还有哪些常用聚合函数？
- answer: 常见聚合函数还有 `SUM()`、`AVG()`、`MAX()`、`MIN()`。比如 `SUM` 用于求和，`AVG` 用于求平均值，`MAX` 和 `MIN` 分别用于取最大值和最小值。它们通常配合 `GROUP BY` 一起使用。

### 自建题 54：如何使用 GROUP BY 对数据进行分组
- tags: 数据库, SQL, GROUP BY
- difficulty: easy
- prompt: `GROUP BY` 的作用是什么？请举一个典型例子。
- answer: `GROUP BY` 用于按照某个字段把数据分组，通常配合聚合函数一起使用。例如 `SELECT department_id, AVG(salary) FROM employees GROUP BY department_id;` 表示按部门分组，统计每个部门的平均薪资。

### 自建题 55：如何过滤分组后的数据
- tags: 数据库, SQL, HAVING, GROUP BY
- difficulty: easy
- prompt: 如果要对分组后的结果继续筛选，为什么要用 `HAVING` 而不是 `WHERE`？
- answer: 因为 `WHERE` 是在分组前过滤原始行，`HAVING` 是在分组后过滤聚合结果。例如 `SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) > 50000;` 表示只保留平均薪资大于 5 万的部门。

### 自建题 56：表连接 INNER JOIN 有什么用
- tags: 数据库, SQL, INNER JOIN, 多表查询
- difficulty: easy
- prompt: `INNER JOIN` 一般用来解决什么问题？
- answer: `INNER JOIN` 用于把两个表中满足关联条件的数据拼接起来，返回交集结果。例如员工表和部门表通过部门 ID 关联后，就可以查询“员工姓名 + 部门名称”这样的组合结果。没有匹配上的记录不会出现在结果中。

### 自建题 57：LEFT JOIN 和 INNER JOIN 有什么区别
- tags: 数据库, SQL, LEFT JOIN, INNER JOIN
- difficulty: easy
- prompt: `LEFT JOIN` 和 `INNER JOIN` 的核心区别是什么？
- answer: `INNER JOIN` 只返回左右表都能匹配上的记录；`LEFT JOIN` 会保留左表的全部记录，即使右表没有匹配，右表字段也会显示为 `NULL`。所以 `LEFT JOIN` 更适合查“主表全部数据 + 从表补充信息”的场景。

### 自建题 58：什么是子查询
- tags: 数据库, SQL, 子查询
- difficulty: easy
- prompt: 什么是子查询？通常会在什么场景下使用？
- answer: 子查询是嵌套在另一个查询中的查询。它可以放在 `SELECT`、`FROM`、`WHERE`、`HAVING` 等位置。比如 `SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);` 就是通过子查询先算平均薪资，再筛出高于平均薪资的员工。

### 自建题 59：如何使用 EXISTS 子查询
- tags: 数据库, SQL, EXISTS, 子查询
- difficulty: medium
- prompt: `EXISTS` 子查询通常用来做什么？为什么它常和相关子查询一起出现？
- answer: `EXISTS` 用于判断子查询是否至少返回一行数据，如果返回，则条件为真。它常用于相关子查询，因为这种写法特别适合做“是否存在关联记录”的判断。例如查询“有员工的部门”时，用 `EXISTS` 就很直观。

### 自建题 60：如何插入一条新记录
- tags: 数据库, SQL, INSERT
- difficulty: easy
- prompt: 往表里插入一条新记录，常见写法有哪些？
- answer: 常见写法是 `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`，这是最推荐的方式，因为显式指定了列名。也可以直接写 `INSERT INTO table_name VALUES (...)`，但这种方式依赖表结构顺序，不够稳妥。

### 自建题 61：如何更新现有记录
- tags: 数据库, SQL, UPDATE
- difficulty: easy
- prompt: 更新表中已有数据时，为什么一定要谨慎使用 `WHERE`？
- answer: 因为 `UPDATE` 如果不加 `WHERE`，会把整张表满足更新语句的所有行都改掉，风险非常大。标准写法是 `UPDATE 表名 SET 字段 = 值 WHERE 条件;`。面试里通常也要强调生产环境执行更新前先确认条件范围。

### 自建题 62：如何删除记录
- tags: 数据库, SQL, DELETE
- difficulty: easy
- prompt: 删除表中部分记录时，SQL 一般怎么写？
- answer: 一般使用 `DELETE FROM 表名 WHERE 条件;`。和 `UPDATE` 一样，如果不加 `WHERE`，就会删除整张表的数据，所以一定要非常谨慎。如果是清空整表，有时也会使用 `TRUNCATE TABLE`，但它和 `DELETE` 的特性不同。

### 自建题 63：DELETE、TRUNCATE 和 DROP 有什么区别
- tags: 数据库, SQL, DELETE, TRUNCATE, DROP
- difficulty: easy
- prompt: 从范围、回滚、自增和对象是否保留几个角度，说一下 `DELETE`、`TRUNCATE`、`DROP` 的区别。
- answer: `DELETE` 是 DML，可以删除部分或全部数据，通常可回滚，不重置自增 ID；`TRUNCATE` 是 DDL，快速清空整张表，通常不可回滚，会重置自增和高水位；`DROP` 是 DDL，直接删除整张表，包括结构和数据。它们的差别本质上是“删数据”“清空表”“删表对象”。

### 自建题 64：如何创建一个简单的表
- tags: 数据库, SQL, CREATE TABLE
- difficulty: easy
- prompt: 如何使用 SQL 创建一张简单的数据表？
- answer: 可以使用 `CREATE TABLE` 定义表名、字段名、数据类型和约束。例如创建学生表时，可以定义主键、姓名字段的 `NOT NULL` 约束以及日期字段。核心点是把字段类型和约束同时设计清楚。

### 自建题 65：如何为表添加一列
- tags: 数据库, SQL, ALTER TABLE, ADD COLUMN
- difficulty: easy
- prompt: 如果要给已有表新增一个字段，通常怎么写 SQL？
- answer: 可以使用 `ALTER TABLE ... ADD COLUMN`。例如 `ALTER TABLE employees ADD COLUMN middle_name VARCHAR(50);`，表示给员工表新增一个中间名字段。这类操作在生产环境也要注意锁表和兼容性影响。

### 自建题 66：如何修改列的数据类型
- tags: 数据库, SQL, ALTER TABLE, MODIFY COLUMN
- difficulty: medium
- prompt: 如果要修改某个字段的数据类型，不同数据库为什么写法可能不同？
- answer: 因为不同数据库对 DDL 语法支持不完全一致。比如 MySQL 常用 `ALTER TABLE ... MODIFY COLUMN`，有些数据库则用 `ALTER COLUMN`。面试时最好说明：虽然核心目标一样，但具体 SQL 语法和限制要结合具体数据库实现来看。

### 自建题 67：如何删除一列
- tags: 数据库, SQL, ALTER TABLE, DROP COLUMN
- difficulty: easy
- prompt: 如果要从表里删除一个字段，SQL 一般怎么写？
- answer: 一般使用 `ALTER TABLE ... DROP COLUMN`。例如 `ALTER TABLE employees DROP COLUMN middle_name;`。这种操作会直接影响表结构，所以在真实项目里通常要先确认字段是否仍被代码、报表或历史逻辑依赖。

### 自建题 68：如何给表添加主键约束
- tags: 数据库, SQL, 主键, 约束
- difficulty: easy
- prompt: 给表添加主键约束有哪些常见方式？
- answer: 可以在建表时直接定义主键，也可以后续通过 `ALTER TABLE ... ADD PRIMARY KEY` 添加。例如建表时写 `id INT PRIMARY KEY`，或者后期通过 `ALTER TABLE employees ADD PRIMARY KEY (employee_id);` 补充主键约束。

### 自建题 69：如何给表添加外键约束
- tags: 数据库, SQL, 外键, 约束
- difficulty: medium
- prompt: 外键约束通常怎么加？它的核心作用是什么？
- answer: 常见写法是 `ALTER TABLE ... ADD FOREIGN KEY (...) REFERENCES 主表(...);`。它的核心作用是保证参照完整性，确保子表中的关联值必须在主表中真实存在，从而避免无效引用或脏数据关系。

### 自建题 70：什么是事务，如何控制事务
- tags: 数据库, SQL, 事务, COMMIT, ROLLBACK
- difficulty: medium
- prompt: 什么是事务？在 SQL 里通常如何开始、提交和回滚事务？
- answer: 事务是把一组数据库操作当成一个不可分割的整体来执行，要么全部成功，要么全部失败。通常可以通过 `START TRANSACTION` 或 `BEGIN` 开始事务，用 `COMMIT` 提交，用 `ROLLBACK` 回滚。经典场景就是转账：一边扣款、一边加款，必须同时成功或同时失败。

### 自建题 71：什么是索引？为什么要使用它
- tags: 数据库, SQL, 索引, 基础
- difficulty: easy
- prompt: 什么是索引？为什么数据库里通常要使用索引？
- answer: 索引是一种帮助数据库高效定位数据的数据结构，常见实现有 B 树等，作用有点像书的目录。它最大的价值是显著提升 `SELECT` 查询效率，尤其是在大表筛选、排序和关联场景下更明显。但索引也有代价，会占用额外存储空间，并增加插入、更新、删除时的维护成本。

### 自建题 72：如何创建索引
- tags: 数据库, SQL, CREATE INDEX, 索引
- difficulty: easy
- prompt: 如何给一张表的某个字段创建索引？
- answer: 一般使用 `CREATE INDEX` 语句。例如 `CREATE INDEX idx_last_name ON employees (last_name);`，表示在 `employees` 表的 `last_name` 列上创建一个名为 `idx_last_name` 的索引。这样按姓氏查询时通常会更快。

### 自建题 73：如何使用 CASE 表达式
- tags: 数据库, SQL, CASE, 条件逻辑
- difficulty: medium
- prompt: `CASE` 表达式有什么用？在 SQL 查询里通常怎么使用？
- answer: `CASE` 用于在 SQL 中实现条件判断，作用类似编程语言里的 `if-else`。它常用于分类展示、条件计算、分段统计等场景。比如可以根据员工薪资范围，把薪资分成低、中、高三个等级，并作为新字段输出。

### 自建题 74：如何计算两个日期之间的差值
- tags: 数据库, SQL, 日期函数, DATEDIFF
- difficulty: easy
- prompt: 如果要计算两个日期之间相差多少天，通常怎么做？
- answer: 一般会使用数据库提供的日期函数，例如 MySQL 常见的是 `DATEDIFF(date1, date2)`。有些数据库也支持直接做日期减法。不同数据库语法略有差异，但核心思路都是调用日期差值函数或日期运算来计算间隔时间。

### 自建题 75：如何从日期时间值中提取部分信息
- tags: 数据库, SQL, YEAR, MONTH, DAY
- difficulty: easy
- prompt: 如果要从日期字段中提取年份、月份或日期，通常用什么方式？
- answer: 一般使用数据库内置日期函数，例如 `YEAR()`、`MONTH()`、`DAY()`。例如可以从订单日期里提取年份和月份，用于做按月统计、年度汇总等分析场景。面试里答题时可以顺带说明不同数据库函数名可能略有不同。

### 自建题 76：如何将多个字符串连接起来
- tags: 数据库, SQL, CONCAT, 字符串函数
- difficulty: easy
- prompt: SQL 中如果要把多个字符串字段拼接成一个完整结果，常见写法是什么？
- answer: 常见做法是使用字符串连接函数，比如 MySQL 中常用 `CONCAT()`。例如把 `first_name` 和 `last_name` 中间加空格拼成完整姓名。不同数据库在字符串拼接符号或函数上可能有差异，但核心思路一样。

### 自建题 77：什么是视图？如何创建它
- tags: 数据库, SQL, 视图, CREATE VIEW
- difficulty: medium
- prompt: 什么是视图？为什么项目里有时会用视图而不是直接写复杂查询？
- answer: 视图是基于查询结果生成的虚拟表，本身通常不直接存数据，而是封装一段 SQL 逻辑。它的好处是可以简化复杂查询、复用查询逻辑、统一对外展示的数据结构。创建时一般使用 `CREATE VIEW` 语句。

### 自建题 78：如何使用 COALESCE 函数处理 NULL 值
- tags: 数据库, SQL, COALESCE, NULL
- difficulty: easy
- prompt: `COALESCE` 的作用是什么？为什么它在查询里很常见？
- answer: `COALESCE` 会从参数列表中返回第一个非 `NULL` 的值，所以很适合给空值补默认值。例如手机号为空时，可以显示 `N/A`。它常用于报表展示、字段兜底和防止空值影响结果计算。

### 自建题 79：如何复制一张表的结构和数据
- tags: 数据库, SQL, CREATE TABLE AS SELECT, 备份
- difficulty: easy
- prompt: 如果要快速复制一张表的结构和数据，通常怎么做？
- answer: 常见做法是使用 `CREATE TABLE ... AS SELECT ...`。例如 `CREATE TABLE employees_backup AS SELECT * FROM employees;`，这样会生成一张新的备份表，并把原表数据一起复制过去。不过不同数据库在语法和约束保留方面会有差异。

### 自建题 80：如何找出一个表中存在而另一个表中不存在的记录
- tags: 数据库, SQL, NOT EXISTS, LEFT JOIN
- difficulty: medium
- prompt: 如何查出“表 A 中有，但表 B 中没有”的数据？
- answer: 常见写法有两种：一种是用 `NOT EXISTS`，另一种是 `LEFT JOIN ... WHERE 右表字段 IS NULL`。这类写法非常适合查缺失关联数据，比如找“没有下单的客户”“没有员工的部门”等场景。核心思路是判断关联记录是否不存在。

### 自建题 81：如何计算分组内的排名
- tags: 数据库, SQL, 窗口函数, RANK, ROW_NUMBER
- difficulty: medium
- prompt: 如果要计算每个分组内部的排名，通常应该用什么方法？
- answer: 这类需求通常用窗口函数处理，比如 `RANK()`、`ROW_NUMBER()`。可以通过 `PARTITION BY` 指定分组依据，再用 `ORDER BY` 指定排序依据。比如按部门分组后，对部门内员工薪资做排名，就是一个典型场景。

### 自建题 82：如何查询第 N 高的薪资
- tags: 数据库, SQL, 第N高, DENSE_RANK
- difficulty: medium
- prompt: 如果要查询第 N 高的薪资，常见的实现思路有哪些？
- answer: 常见思路有两种：一种是通过去重后排序，再结合 `LIMIT` 和 `OFFSET` 获取；另一种是使用窗口函数，比如 `DENSE_RANK()` 或 `RANK()`，再筛选排名等于 N 的记录。窗口函数方案通常更通用，也更适合扩展成复杂排名需求。

### 自建题 83：如何实现分页查询
- tags: 数据库, SQL, LIMIT, OFFSET, 分页
- difficulty: easy
- prompt: SQL 中分页查询通常怎么实现？
- answer: 在 MySQL 中最常见的是 `LIMIT` 加 `OFFSET`。比如 `LIMIT 5 OFFSET 5` 表示跳过前 5 条，再取后 5 条。不同数据库分页语法不同，但本质上都是指定“从哪开始”和“取多少条”。

### 自建题 84：如何统计不同条件下的数量
- tags: 数据库, SQL, CASE, 条件统计
- difficulty: medium
- prompt: 如果要在一条 SQL 里统计不同条件下的数量，比如不同薪资等级的人数，通常怎么做？
- answer: 常见做法是把 `CASE` 放进 `COUNT` 或 `SUM` 里，利用条件表达式做分段统计。比如低薪、中薪、高薪分别统计一列。这样可以在一条 SQL 中同时得到多个条件维度的计数结果，很适合做报表和数据透视类查询。

### 自建题 85：如何批量插入数据
- tags: 数据库, SQL, INSERT, 批量插入
- difficulty: easy
- prompt: 如果一次要插入多条数据，为什么通常不建议一条一条地执行 `INSERT`？
- answer: 因为逐条执行 `INSERT` 往往会带来更多网络往返和事务开销。更高效的方式是在一条 `INSERT` 的 `VALUES` 后面放多组数据。这样可以减少执行次数，通常性能会更好，特别适合批量初始化或导入场景。

### 自建题 86：如何重命名表
- tags: 数据库, SQL, RENAME TABLE, ALTER TABLE
- difficulty: easy
- prompt: 如果要给一张表改名，常见 SQL 写法有哪些？
- answer: 常见方式有 `RENAME TABLE`，也有些数据库支持 `ALTER TABLE ... RENAME TO`。具体语法取决于数据库类型。比如在 MySQL 中既可以直接重命名表，也可以通过 `ALTER TABLE` 改表名。

### 自建题 87：如何备份一张表
- tags: 数据库, SQL, 备份表
- difficulty: easy
- prompt: 如果只是想快速备份一张表，常见方式有哪些？
- answer: 如果既要结构也要数据，可以用 `CREATE TABLE backup_table AS SELECT * FROM original_table;`。如果只备份结构，有些数据库比如 MySQL 支持 `CREATE TABLE backup_table LIKE original_table;`。另外，也可以用数据库工具自带的导出或备份功能。

### 自建题 88：如何恢复或还原一张表
- tags: 数据库, SQL, 恢复表
- difficulty: medium
- prompt: 如果已经有备份表，通常如何恢复原表数据？
- answer: 常见思路是先清空原表，再把备份表的数据插回去，例如 `INSERT INTO original_table SELECT * FROM backup_table;`。如果结构也有问题，可能还要先删表再重建。实际项目里更稳妥的方式通常还是用正式的导入恢复工具，而不是手工改表。

### 自建题 89：作为测试工程师，你如何验证 SQL 查询结果的正确性
- tags: 数据库, SQL, 测试验证, 高频
- difficulty: medium
- prompt: 作为测试工程师，验证一条 SQL 查询结果是否正确时，你通常会从哪些角度入手？
- answer: 我通常会从五个角度验证：先对简单场景做手工计算比对；再尝试用另一种 SQL 写法交叉验证；然后重点检查边界条件，比如 `NULL`、重复值、极端值；同时确保 SQL 逻辑和业务规则一致；如果条件允许，还会准备一小批结果已知的测试数据做精确校验。这样能更系统地验证 SQL 是否真的写对了。

### 自建题 90：如何测试数据库的存储过程或函数
- tags: 数据库, 存储过程, 函数, 测试
- difficulty: medium
- prompt: 如果要测试数据库中的存储过程或函数，通常怎么设计测试思路？
- answer: 一般先准备覆盖正常路径、边界值和异常路径的输入数据，然后在数据库客户端中直接调用存储过程或函数，观察返回值、输出参数和数据库数据变化是否符合预期。除此之外，还要检查异常是否正确抛出，并尽量把这些测试集成进自动化框架，提升回归效率。

### 自建题 91：如何查询所有员工及其所在的部门名称
- tags: 数据库, 多表SQL, INNER JOIN, 高频
- difficulty: easy
- prompt: 如何查询所有员工及其所在的部门名称？请说明这是哪种最基础的多表查询场景。
- answer: 这是最基础的 `INNER JOIN` 场景，一般通过员工表和部门表按 `department_id` 关联。核心作用是把员工信息和部门名称拼接起来，只返回两张表都能匹配上的记录。测试时要重点确认部门名称是否和员工所属部门正确对应。

### 自建题 92：如何查询所有员工信息，包括那些还没有分配部门的员工
- tags: 数据库, 多表SQL, LEFT JOIN
- difficulty: easy
- prompt: 如果要查询所有员工，包括还没有分配部门的员工，应该使用什么连接方式？
- answer: 这种场景应该使用 `LEFT JOIN`，以员工表作为左表，部门表作为右表。这样即使员工没有分配部门，员工记录也不会丢失，只是部门字段会显示为 `NULL`。测试时要重点验证这些“未分配部门员工”是否真的被保留下来。

### 自建题 93：如何查询所有部门信息，包括那些还没有任何员工的部门
- tags: 数据库, 多表SQL, LEFT JOIN, RIGHT JOIN
- difficulty: easy
- prompt: 如果要查出所有部门，包括没有任何员工的部门，通常怎么写 SQL？
- answer: 常见写法是以部门表为主表做 `LEFT JOIN` 员工表，也可以从员工表反向写 `RIGHT JOIN`。更常见且可读性更高的方式是：`FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id`。这样没有员工的部门也会被保留，员工字段则为 `NULL`。

### 自建题 94：如何查询每个员工的名字及其经理的名字
- tags: 数据库, 多表SQL, 自连接, Self Join
- difficulty: medium
- prompt: 员工表和经理表其实是同一张表时，如何查询“员工姓名 + 经理姓名”？
- answer: 这类题本质上是自连接，也就是同一张表用两个别名参与关联。通常员工表用一个别名，经理表用另一个别名，再通过 `e.manager_id = m.employee_id` 关联。为了保留没有经理的最高层管理者，通常要使用 `LEFT JOIN`。

### 自建题 95：如何查询每个部门的名称和该部门的员工人数
- tags: 数据库, 多表SQL, GROUP BY, COUNT
- difficulty: medium
- prompt: 如何统计每个部门的员工人数，并确保没有员工的部门也能显示出来？
- answer: 这类题通常使用部门表 `LEFT JOIN` 员工表，再配合 `GROUP BY` 和 `COUNT` 统计人数。之所以要用 `LEFT JOIN`，是为了让员工数为 0 的部门也能出现在结果里。测试时可以用单部门手工计数结果做交叉验证。

### 自建题 96：如何查询在“上海”工作的所有员工
- tags: 数据库, 多表SQL, 三表连接, WHERE
- difficulty: medium
- prompt: 如果员工通过部门再关联到地点表，如何查询在“上海”工作的所有员工？
- answer: 这类题通常要做三表连接：员工表先连部门表，再由部门表连地点表，最后通过 `WHERE city = 'Shanghai'` 过滤。它考察的是多表连接链路是否清晰。测试时要注意覆盖“一个城市多个部门、一个部门多个员工”的场景。

### 自建题 97：如何查询薪资高于其所在部门平均薪资的员工
- tags: 数据库, 多表SQL, 子查询, 聚合
- difficulty: hard
- prompt: 如何查询那些薪资高于本部门平均薪资的员工？常见实现思路有哪些？
- answer: 常见思路有两种：一种是相关子查询，外层查员工，内层按该员工所在部门求平均薪资；另一种是先按部门算平均薪资生成派生表，再和员工表关联后做比较。第二种通常更适合面试口述，也更清晰。测试时要特别验证“部门只有一个人”或“所有人薪资相同”的边界情况。

### 自建题 98：如何查询所有没有员工的部门
- tags: 数据库, 多表SQL, LEFT JOIN, IS NULL
- difficulty: medium
- prompt: 如果要查询所有没有员工的部门，经典写法是什么？
- answer: 经典写法是部门表 `LEFT JOIN` 员工表，然后在 `WHERE` 里判断员工主键字段为 `NULL`。这种写法本质上是在查“左表有、右表没有”的记录。它也是数据质量检查和参照完整性验证里非常常见的 SQL 模式。

### 自建题 99：如何查询每个员工的项目参与情况
- tags: 数据库, 多表SQL, 多对多, LEFT JOIN
- difficulty: medium
- prompt: 如果员工和项目是多对多关系，如何列出所有员工及其项目参与情况，并且没参与项目的员工也要显示？
- answer: 这类题一般会涉及三张表：员工表、项目关联表、项目表。通常以员工表为左表，先 `LEFT JOIN` 关联表，再 `LEFT JOIN` 项目表，这样即使员工没有参与任何项目，员工信息也不会丢失，只是项目名显示为 `NULL`。测试时要重点验证“一人多项目”和“未参与项目员工”这两类场景。

### 自建题 100：如何查询“张三”所在部门的所有其他员工
- tags: 数据库, 多表SQL, 子查询, 部门筛选
- difficulty: medium
- prompt: 如果要查询“张三”所在部门的所有其他员工，通常怎么设计 SQL？
- answer: 常见做法是先通过子查询找出“张三”的 `department_id`，再用这个部门 ID 去查同部门其他员工，并在外层把“张三”自己排除掉。更严谨的做法是使用员工唯一 ID，而不是只用名字，因为重名会导致查询范围扩大。测试时也要特别验证是否错误包含了“张三”本人或其他重名员工带来的干扰。

## Linux面试题

### 自建题 1：ls 命令有什么用
- tags: Linux, 命令, ls, 高频
- difficulty: easy
- prompt: `ls` 命令有什么作用？`ls -la` 常用于什么场景？
- answer: `ls` 用于列出目录内容，`ls -la` 会显示所有文件（包括隐藏文件）的详细信息。测试环境里常用它快速查看目录结构、文件权限和日志文件是否存在。

### 自建题 2：cd 命令有什么用
- tags: Linux, 命令, cd
- difficulty: easy
- prompt: `cd` 命令的作用是什么？测试排查时为什么它很常用？
- answer: `cd` 用于切换目录，例如进入日志目录、部署目录或配置目录。排查问题时，经常需要先进入对应路径再查看日志、配置或脚本。

### 自建题 3：pwd 命令有什么用
- tags: Linux, 命令, pwd
- difficulty: easy
- prompt: `pwd` 命令通常用来做什么？
- answer: `pwd` 用于显示当前工作目录的完整路径。它常用于确认自己当前所在位置，避免在错误目录里执行命令。

### 自建题 4：cat 命令有什么用
- tags: Linux, 命令, cat
- difficulty: easy
- prompt: `cat` 命令常见用途是什么？
- answer: `cat` 用于查看文件内容，适合快速查看配置文件、脚本或小日志文件。比如用它直接看 `config.yml` 的配置项是否正确。

### 自建题 5：grep 命令有什么用
- tags: Linux, 命令, grep, 日志排查
- difficulty: easy
- prompt: `grep` 命令为什么是测试排查日志时的高频命令？
- answer: `grep` 用于文本搜索，特别适合在日志里查关键字，例如 `error`、`exception`、请求 ID、接口名等。像 `grep -n` 还能显示行号，方便快速定位问题位置。

### 自建题 6：tail 命令有什么用
- tags: Linux, 命令, tail, 日志监控
- difficulty: easy
- prompt: `tail` 和 `tail -f` 在测试环境里常怎么用？
- answer: `tail` 用于查看文件尾部内容，而 `tail -f` 可以实时跟踪日志追加。测试联调和线上排查时，经常边操作系统边 `tail -f` 看日志输出。

### 自建题 7：head 命令有什么用
- tags: Linux, 命令, head
- difficulty: easy
- prompt: `head` 命令适合用在什么场景？
- answer: `head` 用于查看文件开头几行内容，比如 `head -20 app.log` 查看日志前 20 行。它适合快速确认文件格式、头部配置或日志起始内容。

### 自建题 8：cp 命令有什么用
- tags: Linux, 命令, cp
- difficulty: easy
- prompt: `cp` 命令常见用法有哪些？
- answer: `cp` 用于复制文件或目录，带 `-r` 可以递归复制目录。测试环境里常用它做配置备份、日志备份或复制脚本到目标目录。

### 自建题 9：mv 命令有什么用
- tags: Linux, 命令, mv
- difficulty: easy
- prompt: `mv` 命令除了移动文件，还常用于什么？
- answer: `mv` 既可以移动文件，也常用于重命名文件。例如把旧日志改名备份，或把下载好的包改成统一命名格式。

### 自建题 10：rm 命令有什么用
- tags: Linux, 命令, rm, 风险操作
- difficulty: easy
- prompt: `rm -rf` 为什么是高风险命令？
- answer: `rm` 用于删除文件或目录，`rm -rf` 会强制递归删除目标路径，风险非常高。测试环境里执行前必须反复确认路径，避免误删重要数据或部署目录。

### 自建题 11：mkdir 命令有什么用
- tags: Linux, 命令, mkdir
- difficulty: easy
- prompt: `mkdir -p` 和普通 `mkdir` 有什么区别？
- answer: `mkdir` 用于创建目录，`mkdir -p` 可以一次性创建多级目录，即使父目录不存在也能自动补齐。测试时常用于快速准备日志目录、临时数据目录或脚本目录。

### 自建题 12：rmdir 命令有什么用
- tags: Linux, 命令, rmdir
- difficulty: easy
- prompt: `rmdir` 和 `rm -r` 的区别是什么？
- answer: `rmdir` 只能删除空目录，而 `rm -r` 可以删除包含内容的目录。`rmdir` 更适合安全地清理空目录，不容易误删内容。

### 自建题 13：touch 命令有什么用
- tags: Linux, 命令, touch
- difficulty: easy
- prompt: `touch` 命令常见用途有哪些？
- answer: `touch` 可以创建空文件，也可以更新文件的时间戳。测试时常用它快速生成占位文件、模拟输入文件或刷新文件修改时间。

### 自建题 14：find 命令有什么用
- tags: Linux, 命令, find, 查找文件
- difficulty: easy
- prompt: `find` 命令为什么在 Linux 排查中很常用？
- answer: `find` 用于在指定路径下按名称、时间、大小等条件查找文件。比如查所有 `.log` 文件、查最新生成的包、查某个配置文件位置，排查效率很高。

### 自建题 15：which 命令有什么用
- tags: Linux, 命令, which
- difficulty: easy
- prompt: `which` 命令主要解决什么问题？
- answer: `which` 用于查找可执行命令所在路径。测试环境里可以用来确认当前实际使用的是哪个 `python`、`java`、`mysql`，避免环境变量混乱。

### 自建题 16：whereis 命令有什么用
- tags: Linux, 命令, whereis
- difficulty: easy
- prompt: `whereis` 和 `which` 有什么区别？
- answer: `which` 主要找当前可执行命令路径，而 `whereis` 会查找命令、源码、man 手册等相关文件位置。排查安装位置时，`whereis` 提供的信息更丰富。

### 自建题 17：locate 命令有什么用
- tags: Linux, 命令, locate
- difficulty: easy
- prompt: `locate` 为什么查文件通常比 `find` 更快？
- answer: `locate` 基于文件索引数据库查找路径，所以通常比实时遍历目录的 `find` 更快。缺点是索引可能不是最新的，适合快速找配置文件或已知文件名。

### 自建题 18：chmod 命令有什么用
- tags: Linux, 命令, chmod, 权限
- difficulty: easy
- prompt: `chmod +x script.sh` 这条命令做了什么？
- answer: 它给脚本增加执行权限，让脚本可以直接运行。测试环境里常见于部署脚本、启动脚本或自动化脚本无法执行时的处理。

### 自建题 19：chown 命令有什么用
- tags: Linux, 命令, chown, 权限
- difficulty: easy
- prompt: `chown` 命令通常在什么场景下使用？
- answer: `chown` 用于修改文件或目录的所有者和所属组。测试环境里如果服务没权限读写日志、上传目录或配置目录，经常要检查并调整 owner。

### 自建题 20：ps 命令有什么用
- tags: Linux, 命令, ps, 进程
- difficulty: easy
- prompt: `ps aux | grep nginx` 这类命令通常用来做什么？
- answer: `ps` 用于查看进程状态，配合 `grep` 常用来确认某个服务是否启动、启动了几个进程、对应 PID 是多少。是最基础的进程排查命令之一。

### 自建题 21：top 命令有什么用
- tags: Linux, 命令, top, 性能排查
- difficulty: easy
- prompt: `top` 在测试和性能排查中通常看什么？
- answer: `top` 用于实时查看进程、CPU、内存等资源使用情况。测试时常用它判断系统是否打满、哪个进程最耗资源，以及负载是否异常。

### 自建题 22：kill 命令有什么用
- tags: Linux, 命令, kill, 进程
- difficulty: easy
- prompt: `kill -9` 为什么要谨慎使用？
- answer: `kill` 用于终止指定 PID 的进程，`-9` 是强制杀死，进程来不及做清理操作。通常建议先尝试正常停止，再考虑 `kill -9`，避免造成文件损坏或状态不一致。

### 自建题 23：killall 命令有什么用
- tags: Linux, 命令, killall
- difficulty: easy
- prompt: `killall` 和 `kill` 的核心区别是什么？
- answer: `kill` 是按 PID 杀进程，`killall` 是按进程名终止同名进程。它适合快速清理某类进程，但也更容易误伤多个同名实例，所以要谨慎使用。

### 自建题 24：pkill 命令有什么用
- tags: Linux, 命令, pkill
- difficulty: easy
- prompt: `pkill -f` 常见用途是什么？
- answer: `pkill` 可以按模式匹配进程名或命令行，`-f` 会匹配完整命令。比如按脚本名杀掉某个后台 Python 任务，比单纯记 PID 更方便。

### 自建题 25：bg 命令有什么用
- tags: Linux, 命令, bg, 作业控制
- difficulty: medium
- prompt: `bg` 命令主要解决什么问题？
- answer: `bg` 用于把暂停或前台作业放到后台继续运行。它属于 shell 作业控制命令，适合临时把一个正在执行的任务切到后台，不阻塞当前终端。

### 自建题 26：fg 命令有什么用
- tags: Linux, 命令, fg, 作业控制
- difficulty: medium
- prompt: `fg` 和 `bg` 是什么关系？
- answer: `fg` 用于把后台作业切回前台运行，和 `bg` 相反。排查时如果某个任务放后台后想重新接管它，就可以用 `fg %1` 这类命令把它拉回前台。

### 自建题 27：jobs 命令有什么用
- tags: Linux, 命令, jobs, 作业控制
- difficulty: medium
- prompt: `jobs` 命令通常和哪些场景搭配使用？
- answer: `jobs` 用于查看当前终端会话里的后台作业状态。它通常和 `bg`、`fg` 一起用，帮助确认哪些任务还在跑、对应的作业号是多少。

### 自建题 28：nohup 命令有什么用
- tags: Linux, 命令, nohup, 后台运行
- difficulty: easy
- prompt: 为什么长期运行任务经常会用 `nohup ... &`？
- answer: 因为 `nohup` 可以让进程在终端退出后仍继续运行，配合 `&` 可直接放到后台。测试环境里常用于后台启动服务、长时间跑脚本、执行压测任务等。

### 自建题 29：df 命令有什么用
- tags: Linux, 命令, df, 磁盘
- difficulty: easy
- prompt: `df -h` 通常用来检查什么？
- answer: `df -h` 用于查看磁盘分区的使用情况，`-h` 以易读格式显示。测试排查时经常先看磁盘是否满了，因为磁盘空间不足会引发日志写不进、数据库异常、服务启动失败等问题。

### 自建题 30：du 命令有什么用
- tags: Linux, 命令, du, 磁盘
- difficulty: easy
- prompt: `du -sh /var/log` 这类命令适合解决什么问题？
- answer: `du` 用于查看目录或文件占用空间，`du -sh` 可以快速看某个目录总大小。常用于找出哪个日志目录、上传目录或缓存目录占空间过大。

### 自建题 31：free 命令有什么用
- tags: Linux, 命令, free, 内存
- difficulty: easy
- prompt: `free -h` 在测试环境排查里通常怎么看？
- answer: `free -h` 用于查看内存和 swap 使用情况。它常用于判断机器是否存在内存紧张、缓存占用过高或 swap 被打满的问题。

### 自建题 32：uname 命令有什么用
- tags: Linux, 命令, uname
- difficulty: easy
- prompt: `uname -a` 可以帮助确认哪些信息？
- answer: `uname -a` 可以查看内核版本、系统架构、主机名等系统信息。做环境确认、兼容性排查或提缺陷时，这些信息都很有用。

### 自建题 33：uptime 命令有什么用
- tags: Linux, 命令, uptime, 负载
- difficulty: easy
- prompt: `uptime` 除了看开机时长，还常看什么？
- answer: `uptime` 除了显示系统运行时间，还会显示平均负载。测试和运维排查时，负载值能帮助快速判断机器是否处于高压状态。

### 自建题 34：who 命令有什么用
- tags: Linux, 命令, who
- difficulty: easy
- prompt: `who` 命令能看到什么？
- answer: `who` 用于查看当前登录用户信息。多用户共享测试环境时，它有助于确认当前有哪些人在线、谁可能正在操作环境。

### 自建题 35：w 命令有什么用
- tags: Linux, 命令, w
- difficulty: easy
- prompt: `w` 和 `who` 有什么区别？
- answer: `w` 不仅能看到当前登录用户，还能看到他们正在执行的活动命令和负载情况。相比 `who`，它更适合看“谁在这台机器上做什么”。

### 自建题 36：last 命令有什么用
- tags: Linux, 命令, last
- difficulty: easy
- prompt: `last` 命令通常在什么场景下使用？
- answer: `last` 用于查看用户登录历史。排查环境被谁登录过、什么时候重启过、某账号是否近期使用过时，都可能用到它。

### 自建题 37：history 命令有什么用
- tags: Linux, 命令, history
- difficulty: easy
- prompt: `history` 对测试排查有什么帮助？
- answer: `history` 用于查看当前 shell 的命令历史。它可以帮助回溯刚刚执行过哪些命令，避免重复输入，也有助于复盘一次排查过程。

### 自建题 38：tar 命令有什么用
- tags: Linux, 命令, tar, 压缩
- difficulty: easy
- prompt: `tar -czvf` 常见用途是什么？
- answer: `tar` 常用于把多个文件或目录打包压缩成一个归档文件，`-czvf` 表示创建 gzip 压缩包。测试时常用来打包日志、备份目录或上传排查材料。

### 自建题 39：gzip 命令有什么用
- tags: Linux, 命令, gzip
- difficulty: easy
- prompt: `gzip` 命令和 `tar` 有什么不同？
- answer: `gzip` 主要用于压缩单个文件，而 `tar` 常用于先打包再压缩多个文件。日志归档时，经常会看到 `.gz` 文件就是通过 `gzip` 生成的。

### 自建题 40：gunzip 命令有什么用
- tags: Linux, 命令, gunzip
- difficulty: easy
- prompt: 如果遇到 `.gz` 文件，通常如何解压？
- answer: 常见方式是用 `gunzip` 解压，例如 `gunzip file.txt.gz`。排查历史日志、查看归档输出时经常会用到。

### 自建题 41：zip 命令有什么用
- tags: Linux, 命令, zip
- difficulty: easy
- prompt: `zip` 适合哪些压缩场景？
- answer: `zip` 用于创建 zip 压缩包，适合跨平台共享文件。测试环境里如果要把日志、截图、脚本打包给其他同事或发到 Windows 环境，zip 很常见。

### 自建题 42：unzip 命令有什么用
- tags: Linux, 命令, unzip
- difficulty: easy
- prompt: 遇到 zip 压缩包时，Linux 下通常怎么解压？
- answer: 一般使用 `unzip archive.zip`。它适合快速解压测试包、构建产物或别人传过来的附件文件。

### 自建题 43：ssh 命令有什么用
- tags: Linux, 命令, ssh, 远程登录
- difficulty: easy
- prompt: `ssh` 为什么是测试环境里最基础的远程命令之一？
- answer: `ssh` 用于远程登录 Linux 主机，是进入测试环境、执行命令、排查日志、查看服务状态的基础入口。很多测试工作其实都是从 `ssh user@host` 开始的。

### 自建题 44：scp 命令有什么用
- tags: Linux, 命令, scp, 文件传输
- difficulty: easy
- prompt: `scp` 命令一般在什么场景下使用？
- answer: `scp` 用于在本地和远程主机之间安全复制文件。测试时经常用它上传脚本、下载日志、传输构建包或配置文件。

### 自建题 45：rsync 命令有什么用
- tags: Linux, 命令, rsync, 同步
- difficulty: medium
- prompt: 为什么 `rsync` 常被认为比普通复制更适合做目录同步？
- answer: `rsync` 支持增量同步，只传输变化部分，效率通常比直接整体复制更高。测试环境里同步日志、部署目录或备份文件时很常用。

### 自建题 46：ping 命令有什么用
- tags: Linux, 命令, ping, 网络
- difficulty: easy
- prompt: `ping` 命令最常用于确认什么？
- answer: `ping` 用于测试与目标主机的网络连通性和延迟情况。排查接口超时、服务不可达、环境网络问题时，`ping` 通常是第一步。

### 自建题 47：traceroute 命令有什么用
- tags: Linux, 命令, traceroute, 网络路径
- difficulty: medium
- prompt: `traceroute` 相比 `ping` 更适合解决什么问题？
- answer: `traceroute` 用于查看数据包经过的网络路径，适合排查网络链路在哪一跳出现问题。`ping` 只能告诉你通不通，`traceroute` 更像是在查“卡在哪”。

### 自建题 48：netstat 命令有什么用
- tags: Linux, 命令, netstat, 端口
- difficulty: easy
- prompt: `netstat -tuln` 常用来做什么？
- answer: `netstat` 用于查看网络状态、连接和监听端口。`netstat -tuln` 很适合快速确认服务是否在监听某个端口，是端口排查的经典命令。

### 自建题 49：ss 命令有什么用
- tags: Linux, 命令, ss, 端口
- difficulty: easy
- prompt: 为什么现在很多场景更推荐 `ss` 而不是 `netstat`？
- answer: `ss` 用于查看套接字和网络连接统计，通常速度更快、信息更现代，所以很多系统里更推荐它来替代 `netstat`。比如 `ss -tuln` 就常用来查监听端口。

### 自建题 50：ifconfig 命令有什么用
- tags: Linux, 命令, ifconfig, 网络接口
- difficulty: easy
- prompt: `ifconfig` 命令通常看什么？
- answer: `ifconfig` 用于查看或配置网络接口信息，比如 IP 地址、广播地址、网卡状态等。虽然新系统更多推荐 `ip` 命令，但它仍然是很多人熟悉的经典命令。

### 自建题 51：ip 命令有什么用
- tags: Linux, 命令, ip, 网络接口
- difficulty: easy
- prompt: 为什么现在很多场景会用 `ip addr show` 替代 `ifconfig`？
- answer: 因为 `ip` 命令功能更全，适合查看和操作地址、路由、网卡等信息，是更现代的网络管理工具。`ip addr show` 常用于查看当前所有网络接口及其 IP。

### 自建题 52：route 命令有什么用
- tags: Linux, 命令, route, 路由表
- difficulty: medium
- prompt: `route -n` 常用于排查什么？
- answer: `route -n` 用于查看路由表，适合排查机器为什么访问不到某个网段、默认网关是否正确、路由是否配置异常等网络问题。

### 自建题 53：hostname 命令有什么用
- tags: Linux, 命令, hostname
- difficulty: easy
- prompt: `hostname` 命令在测试环境里有什么价值？
- answer: `hostname` 用于显示或设置主机名。多台机器环境里，确认自己当前到底连的是哪台机器非常重要，避免在错误节点上排查或操作。

### 自建题 54：curl 命令有什么用
- tags: Linux, 命令, curl, HTTP
- difficulty: easy
- prompt: `curl -I` 和普通 `curl` 常见用途是什么？
- answer: `curl` 用于和 URL 交互，测试 HTTP/HTTPS 请求非常方便。`curl -I` 只获取响应头，适合快速验证接口是否可达、状态码是否正确、网关是否正常。

### 自建题 55：wget 命令有什么用
- tags: Linux, 命令, wget, 下载
- difficulty: easy
- prompt: `wget` 和 `curl` 有什么常见使用区别？
- answer: `wget` 更偏向下载文件，适合拉取安装包、测试数据包或构建产物；`curl` 更偏向接口交互和调试。测试环境里两者都很常见，但用途侧重点不同。

### 自建题 56：lynx 命令有什么用
- tags: Linux, 命令, lynx, 文本浏览器
- difficulty: medium
- prompt: `lynx` 这种文本浏览器可能在什么场景下有用？
- answer: `lynx` 可以在纯终端环境中以文本方式浏览网页。对于没有图形界面的服务器，临时查看页面输出或文档内容时会比较方便。

### 自建题 57：telnet 命令有什么用
- tags: Linux, 命令, telnet, 端口测试
- difficulty: easy
- prompt: 为什么测试工程师有时会用 `telnet host port`？
- answer: 因为它可以快速验证某个主机某个端口是否能连通。虽然 `telnet` 本身是远程登录协议，但在很多排查场景里更常被拿来做简单端口连通性测试。

### 自建题 58：nc 命令有什么用
- tags: Linux, 命令, nc, 端口测试
- difficulty: easy
- prompt: `nc -zv` 适合排查什么问题？
- answer: `nc` 也叫 netcat，是非常灵活的网络工具。`nc -zv host port` 常用于快速测试端口是否开放，相比 `telnet` 更轻量，也更适合脚本化使用。

### 自建题 59：ssh-keygen 命令有什么用
- tags: Linux, 命令, ssh-keygen, SSH
- difficulty: easy
- prompt: `ssh-keygen` 一般在什么场景下用？
- answer: `ssh-keygen` 用于生成 SSH 密钥对，方便后续做免密登录。多台测试机频繁连接时，配置 SSH key 可以明显提升效率。

### 自建题 60：ssh-copy-id 命令有什么用
- tags: Linux, 命令, ssh-copy-id, SSH
- difficulty: easy
- prompt: `ssh-copy-id` 的作用是什么？
- answer: 它用于把本机公钥复制到远程主机，从而实现免密 SSH 登录。测试环境里经常用于批量部署、自动化脚本执行或多节点巡检。

### 自建题 61：sed 命令有什么用
- tags: Linux, 命令, sed, 文本处理
- difficulty: medium
- prompt: `sed` 命令在测试环境里最常用来做什么？
- answer: `sed` 是流编辑器，常用于替换文本、删除行、提取行等批处理操作。比如快速替换配置项、修改脚本中的变量值、处理日志文本等。

### 自建题 62：awk 命令有什么用
- tags: Linux, 命令, awk, 文本处理
- difficulty: medium
- prompt: `awk` 为什么常被用来处理结构化文本？
- answer: `awk` 很适合按列处理文本，比如按空格、冒号等分隔符提取指定字段。测试和运维排查时，分析日志、统计命令输出、抽取关键列时非常高效。

### 自建题 63：cut 命令有什么用
- tags: Linux, 命令, cut
- difficulty: easy
- prompt: `cut -d: -f1 /etc/passwd` 这类命令体现了 `cut` 的什么能力？
- answer: `cut` 用于按分隔符提取指定字段。像 `/etc/passwd` 这种冒号分隔文件，常用 `cut` 快速取用户名、UID 等某一列信息。

### 自建题 64：paste 命令有什么用
- tags: Linux, 命令, paste
- difficulty: easy
- prompt: `paste` 命令适合什么场景？
- answer: `paste` 用于把多个文件按行合并输出。它适合做简单数据拼接，比如把两列结果临时合成一个对照表。

### 自建题 65：sort 命令有什么用
- tags: Linux, 命令, sort
- difficulty: easy
- prompt: `sort` 命令通常如何配合其他命令使用？
- answer: `sort` 用于对文本内容排序，常配合 `uniq`、`grep`、`awk` 一起做日志统计、去重计数、结果整理等工作。

### 自建题 66：uniq 命令有什么用
- tags: Linux, 命令, uniq
- difficulty: easy
- prompt: `uniq` 为什么经常和 `sort` 一起出现？
- answer: 因为 `uniq` 只能处理相邻重复行，所以通常要先 `sort` 再 `uniq` 才能得到全局去重效果。日志分析和数据统计时这种组合很常见。

### 自建题 67：wc 命令有什么用
- tags: Linux, 命令, wc
- difficulty: easy
- prompt: `wc -l` 在测试排查里经常统计什么？
- answer: `wc` 用于统计文件的行数、单词数、字符数，其中 `wc -l` 最常用于统计日志行数、结果条数、匹配数量等。

### 自建题 68：diff 命令有什么用
- tags: Linux, 命令, diff, 文件对比
- difficulty: easy
- prompt: `diff` 命令通常用来比较什么？
- answer: `diff` 用于比较两个文件的差异。测试环境里常用于对比两份配置、两个接口结果样本、两次导出数据或两个版本脚本之间的变化。

### 自建题 69：patch 命令有什么用
- tags: Linux, 命令, patch
- difficulty: medium
- prompt: `patch -p1 < patchfile` 主要解决什么问题？
- answer: `patch` 用于根据补丁文件把改动应用到代码或文本上。它在代码修复、版本差异同步或快速应用别人给的修改时很有用。

### 自建题 70：ln 命令有什么用
- tags: Linux, 命令, ln, 软链接
- difficulty: easy
- prompt: `ln -s` 创建的是什么？为什么测试环境里常用？
- answer: `ln -s` 创建的是软链接，相当于给原文件或目录建一个快捷入口。测试环境里常用于统一路径、切换版本目录、快速引用配置或脚本。

### 自建题 71：readlink 命令有什么用
- tags: Linux, 命令, readlink
- difficulty: easy
- prompt: `readlink` 适合查什么问题？
- answer: `readlink` 用于查看符号链接实际指向的路径。比如排查 `/usr/bin/python` 最终指向哪个版本时就很实用。

### 自建题 72：stat 命令有什么用
- tags: Linux, 命令, stat
- difficulty: easy
- prompt: `stat` 和 `ls -l` 相比有什么优势？
- answer: `stat` 可以显示更详细的文件状态信息，例如权限、大小、inode、访问时间、修改时间、变更时间等。排查文件是否被更新、何时变更时很有帮助。

### 自建题 73：file 命令有什么用
- tags: Linux, 命令, file
- difficulty: easy
- prompt: `file document.pdf` 这类命令通常用于什么？
- answer: `file` 用于判断文件类型。测试环境里遇到扩展名不可信、压缩包异常、导出文件格式不确定时，常用它快速确认真实类型。

### 自建题 74：md5sum 命令有什么用
- tags: Linux, 命令, md5sum, 校验
- difficulty: easy
- prompt: 为什么下载或传输文件后常会校验 `md5sum`？
- answer: `md5sum` 用于计算文件 MD5 校验值，可用于确认文件在下载、拷贝、传输过程中是否发生损坏或被替换。虽然 MD5 不适合强安全场景，但做完整性校验仍很常见。

### 自建题 75：sha256sum 命令有什么用
- tags: Linux, 命令, sha256sum, 校验
- difficulty: easy
- prompt: `sha256sum` 和 `md5sum` 有什么区别？
- answer: 两者都能做文件校验，但 `sha256sum` 在安全性和碰撞抗性上更强。现在很多安装包、镜像文件更常提供 SHA256 值给用户核对。

### 自建题 76：date 命令有什么用
- tags: Linux, 命令, date
- difficulty: easy
- prompt: `date` 在测试环境里除了看时间，还有什么价值？
- answer: `date` 可用于查看或格式化当前系统时间。排查日志时间、比对时区、确认定时任务触发点时，经常要先看机器时间是否准确。

### 自建题 77：cal 命令有什么用
- tags: Linux, 命令, cal
- difficulty: easy
- prompt: `cal` 命令虽简单，但可能在什么场景下有用？
- answer: `cal` 用于显示日历。虽然它不是高频排查命令，但在核对日期、回看排期、定位某天发生的问题时会有点用。

### 自建题 78：time 命令有什么用
- tags: Linux, 命令, time, 性能
- difficulty: easy
- prompt: `time ls -la` 这类命令体现了 `time` 的什么作用？
- answer: `time` 用于测量命令执行耗时。测试时可以用它粗略评估脚本、接口调用命令或批处理任务执行时间。

### 自建题 79：timeout 命令有什么用
- tags: Linux, 命令, timeout
- difficulty: easy
- prompt: `timeout 5s ping example.com` 这类写法能解决什么问题？
- answer: `timeout` 用于给命令设置最长执行时间，超时就终止。它非常适合防止网络命令、脚本、巡检命令长时间卡住。

### 自建题 80：watch 命令有什么用
- tags: Linux, 命令, watch, 实时监控
- difficulty: easy
- prompt: `watch -n 1 'date'` 这种用法适合类比到哪些测试排查场景？
- answer: `watch` 可以定期重复执行命令并实时刷新输出。比如每秒看一次磁盘、连接数、队列长度、文件变化，在排查动态问题时很方便。

### 自建题 81：at 命令有什么用
- tags: Linux, 命令, at, 定时任务
- difficulty: medium
- prompt: `at` 和 `crontab` 在定时任务场景下有什么区别？
- answer: `at` 更适合执行一次性的定时任务，比如“今晚 12 点执行某条命令”；`crontab` 更适合周期性任务。测试环境里偶尔会用 `at` 做一次性延迟任务。

### 自建题 82：crontab 命令有什么用
- tags: Linux, 命令, crontab, 定时任务
- difficulty: easy
- prompt: `crontab -l` 为什么是排查定时任务的第一步之一？
- answer: `crontab -l` 用于查看当前用户的定时任务列表。排查“任务有没有配”“是不是这个用户在跑”“时间表达式对不对”时都很有帮助。

### 自建题 83：systemctl 命令有什么用
- tags: Linux, 命令, systemctl, 服务管理
- difficulty: easy
- prompt: `systemctl status nginx` 这类命令在测试环境里通常用来做什么？
- answer: `systemctl` 用于控制 systemd 管理的服务，比如查看状态、启动、停止、重启服务。测试环境里查服务是否活着、启动失败原因是什么，常常会先看它。

### 自建题 84：service 命令有什么用
- tags: Linux, 命令, service, 服务管理
- difficulty: easy
- prompt: `service nginx restart` 这种命令和 `systemctl` 有什么关系？
- answer: `service` 是较传统的服务管理方式，在一些系统上仍然可用。它和 `systemctl` 目标相似，都是用于启动、停止、重启服务，只是底层机制和系统版本相关。

### 自建题 85：journalctl 命令有什么用
- tags: Linux, 命令, journalctl, 日志
- difficulty: medium
- prompt: `journalctl -u nginx` 主要用于查什么？
- answer: `journalctl` 用于查看 systemd 管理的系统日志，`-u nginx` 表示看 nginx 服务日志。服务启动失败、崩溃重启、权限异常时经常要看这里。

### 自建题 86：dmesg 命令有什么用
- tags: Linux, 命令, dmesg, 内核日志
- difficulty: medium
- prompt: `dmesg | grep error` 适合排查哪类问题？
- answer: `dmesg` 用于查看内核消息，常用于排查硬件、驱动、磁盘、内存、系统级错误。应用层问题不一定看得到，但系统底层异常常能在这里找到线索。

### 自建题 87：lsof 命令有什么用
- tags: Linux, 命令, lsof, 端口排查
- difficulty: easy
- prompt: `lsof -i :80` 常用于解决什么问题？
- answer: `lsof` 用于列出打开文件和网络连接。`lsof -i :80` 常用于查是谁占用了 80 端口，定位端口冲突、僵尸服务或异常监听进程非常高效。

### 自建题 88：strace 命令有什么用
- tags: Linux, 命令, strace, 系统调用
- difficulty: hard
- prompt: `strace` 在排查程序问题时为什么很强？
- answer: `strace` 能跟踪进程的系统调用和信号，适合排查程序卡在哪、读写了什么文件、访问了哪些系统资源。它对深入分析“程序为什么不工作”非常有帮助，但输出信息也比较底层。

### 自建题 89：vmstat 命令有什么用
- tags: Linux, 命令, vmstat, 性能监控
- difficulty: medium
- prompt: `vmstat 1` 通常用来观察哪些系统指标？
- answer: `vmstat` 主要看虚拟内存、进程状态、CPU、上下文切换、I/O 等系统整体指标。它适合做快速系统体检，判断是否有内存、CPU 或 I/O 异常。

### 自建题 90：iostat 命令有什么用
- tags: Linux, 命令, iostat, 磁盘IO
- difficulty: medium
- prompt: `iostat -x 1` 最适合排查什么问题？
- answer: `iostat` 用于查看 CPU 和磁盘 I/O 统计，`-x` 会显示更详细的扩展指标。排查磁盘利用率高、I/O 等待长、数据库或日志写入慢时很常用。

### 自建题 91：mpstat 命令有什么用
- tags: Linux, 命令, mpstat, CPU
- difficulty: medium
- prompt: `mpstat` 和 `top` 都看 CPU，它更适合什么场景？
- answer: `mpstat` 更适合看多核 CPU 各核的使用情况。排查 CPU 负载不均、单核打满、并发任务分布不均时比总览型命令更直观。

### 自建题 92：pidstat 命令有什么用
- tags: Linux, 命令, pidstat, 进程监控
- difficulty: medium
- prompt: `pidstat -u 1` 这种命令适合看什么？
- answer: `pidstat` 用于查看进程级别的 CPU、内存、I/O 等统计信息。排查“到底哪个进程持续吃资源”时，它比只看一眼 `top` 更适合做持续观察。

### 自建题 93：sar 命令有什么用
- tags: Linux, 命令, sar, 系统活动
- difficulty: medium
- prompt: `sar` 命令为什么适合做历史性能分析？
- answer: `sar` 可以查看系统活动报告，包括 CPU、内存、网络、I/O 等指标，而且很多环境会保留历史数据。它适合分析“某个时间段系统到底发生了什么”。

### 自建题 94：ulimit 命令有什么用
- tags: Linux, 命令, ulimit, 资源限制
- difficulty: medium
- prompt: `ulimit -a` 排查时为什么很重要？
- answer: `ulimit` 用于查看或设置 shell 资源限制，比如最大打开文件数、进程数、栈大小等。很多“连接不够用”“文件句柄耗尽”的问题，最后都会查到这里。

### 自建题 95：env 命令有什么用
- tags: Linux, 命令, env, 环境变量
- difficulty: easy
- prompt: `env` 命令在环境排查里最常看什么？
- answer: `env` 用于查看当前环境变量。测试环境里经常要确认 `JAVA_HOME`、`PATH`、代理配置、应用配置变量是否正确生效。

### 自建题 96：export 命令有什么用
- tags: Linux, 命令, export, 环境变量
- difficulty: easy
- prompt: `export PATH=$PATH:/new/path` 这种操作的本质是什么？
- answer: `export` 用于设置当前 shell 会话中的环境变量，并让子进程可见。常见场景包括临时补 PATH、设置应用配置变量、切换测试环境参数。

### 自建题 97：unset 命令有什么用
- tags: Linux, 命令, unset
- difficulty: easy
- prompt: `unset VARIABLE` 主要解决什么问题？
- answer: `unset` 用于删除环境变量或 shell 函数。排查环境变量污染、临时变量冲突、旧配置残留时会用到它。

### 自建题 98：alias 命令有什么用
- tags: Linux, 命令, alias
- difficulty: easy
- prompt: `alias ll='ls -alF'` 体现了什么能力？
- answer: `alias` 用于给命令创建别名，方便把高频命令简化。比如把 `ls -alF` 简化成 `ll`，提升日常操作效率。

### 自建题 99：unalias 命令有什么用
- tags: Linux, 命令, unalias
- difficulty: easy
- prompt: `unalias ll` 这类操作通常用于什么场景？
- answer: `unalias` 用于删除之前定义的命令别名。排查某个命令行为异常、怀疑被 alias 改写时，经常需要先取消别名确认真实命令行为。

### 自建题 100：source 命令有什么用
- tags: Linux, 命令, source, shell配置
- difficulty: easy
- prompt: 为什么修改完 `.bashrc` 后经常要执行 `source ~/.bashrc`？
- answer: `source` 用于在当前 shell 中执行脚本文件。修改 `.bashrc`、环境变量或 alias 后，用 `source ~/.bashrc` 可以立即生效，而不用重新登录终端。

## 测试工程化与CI/CD
