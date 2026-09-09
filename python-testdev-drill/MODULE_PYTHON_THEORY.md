# Python编程基础理论面试题

### 1. *args 和 **kwargs 的区别
- tags: 函数参数, 基础语法
- difficulty: easy
- prompt: Python 中 `*args` 和 `**kwargs` 有什么区别？
- answer: `*args` 用于接收不定长位置参数，打包成 tuple；`**kwargs` 用于接收不定长关键字参数，打包成 dict。常用于封装通用函数接口。

### 2. 深拷贝和浅拷贝的区别
- tags: 拷贝, 数据类型
- difficulty: easy
- prompt: 解释 Python 中深拷贝和浅拷贝的区别，并举例说明。
- answer: 浅拷贝只复制最外层对象，内部可变子对象仍共享；深拷贝会递归复制内部对象，彼此独立。可用 `copy.copy` 和 `copy.deepcopy` 区分。

### 3. 装饰器是什么
- tags: 装饰器, 闭包
- difficulty: easy
- prompt: 什么是装饰器？它解决什么问题？
- answer: 装饰器本质上是接收函数并返回新函数的高阶函数，常用于在不改原函数代码的前提下添加日志、鉴权、缓存等横切逻辑。

### 4. 生成器和迭代器的区别
- tags: 生成器, 迭代器
- difficulty: easy
- prompt: 解释生成器和迭代器的区别与联系。
- answer: 迭代器实现 `__iter__` / `__next__` 协议；生成器是创建迭代器的一种更便捷方式，通常由带 `yield` 的函数生成。

### 5. GIL 是什么
- tags: GIL, 并发
- difficulty: medium
- prompt: Python 的 GIL 是什么？它对多线程有什么影响？
- answer: GIL 是 CPython 的全局解释器锁，同一时刻只允许一个线程执行 Python 字节码。CPU 密集型任务受限明显，I/O 密集型任务仍可从多线程获益。

### 6. 协程和线程区别
- tags: 协程, 并发
- difficulty: medium
- prompt: 协程和线程有什么区别？
- answer: 线程由操作系统调度，开销较大；协程在用户态协作切换，开销更小，更适合大量 I/O 等待场景。

### 7. Python 的垃圾回收机制是怎样的
- tags: 垃圾回收, 内存管理
- difficulty: medium
- prompt: Python 的垃圾回收机制是怎样的？
- answer: Python 主要通过引用计数回收对象，同时用分代回收处理循环引用。引用计数实时回收大多数无用对象，分代 GC 负责周期性扫描容器对象。

### 8. 什么是闭包
- tags: 闭包, 作用域
- difficulty: medium
- prompt: 什么是闭包？闭包要满足什么条件？
- answer: 闭包是内部函数引用了外部函数作用域中的变量，并且外部函数执行结束后这些变量仍被保留。通常满足嵌套函数、引用外部变量、返回内部函数三个条件。

### 9. try / except / else / finally 分别有什么作用
- tags: 异常处理, 基础语法
- difficulty: easy
- prompt: `try`、`except`、`else`、`finally` 分别有什么作用？
- answer: `try` 放可能出错的代码；`except` 捕获异常；`else` 在没有异常时执行；`finally` 无论是否异常都会执行，常用于资源释放。

### 10. __new__ 和 __init__ 有什么区别，它们分别在什么时候执行
- tags: 面向对象, 魔术方法
- difficulty: medium
- prompt: `__new__` 和 `__init__` 有什么区别？它们分别在什么时候执行？
- answer: `__new__` 负责创建并返回实例对象，在对象创建前执行；`__init__` 负责初始化实例属性，在对象创建后执行。`__new__` 更底层，常见于单例、不可变对象定制。

### 11. with 语句和上下文管理器的原理
- tags: 上下文管理器, 文件操作
- difficulty: medium
- prompt: `with` 语句和上下文管理器的原理是什么？
- answer: `with` 本质上是调用上下文管理器对象的 `__enter__` 和 `__exit__` 方法。常用于自动申请和释放资源，如文件、锁、数据库连接。

### 12. lambda 表达式的适用场景和限制
- tags: lambda, 函数式编程
- difficulty: easy
- prompt: `lambda` 表达式适用什么场景？有什么限制？
- answer: `lambda` 适合写简单、一次性的匿名小函数，常配合 `sorted`、`map`、`filter` 使用。限制是只能写单个表达式，不适合复杂逻辑。

### 13. 列表推导式和生成器表达式有什么区别
- tags: 列表推导式, 生成器
- difficulty: easy
- prompt: 列表推导式和生成器表达式有什么区别？
- answer: 列表推导式会直接生成完整列表，占用更多内存；生成器表达式按需生成值，更节省内存，适合大数据量场景。

### 14. 可变类型默认参数的问题与规避方式
- tags: 函数参数, 易错点
- difficulty: medium
- prompt: 可变类型默认参数有什么坑？怎么规避？
- answer: 默认参数只在函数定义时创建一次，如果默认值是 list、dict 等可变对象，多次调用会共享状态。通常用 `None` 作为默认值，在函数内部再初始化。

### 15. @classmethod 和 @staticmethod 的区别与使用场景
- tags: 面向对象, 类方法
- difficulty: easy
- prompt: `@classmethod` 和 `@staticmethod` 有什么区别？各自适合什么场景？
- answer: `@classmethod` 第一个参数是 `cls`，可访问类属性和类方法，常用于工厂方法；`@staticmethod` 不自动传 `self/cls`，更像放在类里的普通函数。

### 16. __str__ 和 __repr__ 的区别与使用场景
- tags: 魔术方法, 面向对象
- difficulty: easy
- prompt: `__str__` 和 `__repr__` 有什么区别？各自什么时候用？
- answer: `__str__` 面向用户，强调可读性；`__repr__` 面向开发者，强调明确和调试信息。打印对象时优先用 `__str__`，没有时回退到 `__repr__`。

### 17. set 和 list 的区别与适用场景
- tags: 数据结构, 集合
- difficulty: easy
- prompt: `set` 和 `list` 的区别是什么？`set` 适合解决什么问题？
- answer: `list` 有序可重复，`set` 无序且元素唯一。`set` 适合去重、成员判断、交并差集等场景。

### 18. read()、readline()、readlines() 的区别
- tags: 文件操作, IO
- difficulty: easy
- prompt: Python 中 `read()`、`readline()`、`readlines()` 有什么区别？
- answer: `read()` 一次性读取全部内容；`readline()` 每次读一行；`readlines()` 读取所有行并返回列表。大文件场景通常更推荐逐行读。

### 19. sorted() 和 list.sort() 的区别
- tags: 排序, 基础语法
- difficulty: easy
- prompt: Python 中 `sorted()` 和 `list.sort()` 有什么区别？
- answer: `list.sort()` 是列表方法，原地排序，返回 `None`；`sorted()` 是内置函数，不修改原对象，返回新列表，适用于任意可迭代对象。

### 20. global 和 nonlocal 的区别
- tags: 作用域, 基础语法
- difficulty: medium
- prompt: Python 中 `global` 和 `nonlocal` 有什么区别？
- answer: `global` 用于声明修改全局作用域变量；`nonlocal` 用于声明修改外层但非全局作用域中的变量，常见于闭包场景。

### 21. hasattr()、getattr()、setattr() 的区别与作用
- tags: 反射, 面向对象
- difficulty: medium
- prompt: `hasattr()`、`getattr()`、`setattr()` 分别是做什么的？
- answer: `hasattr` 判断对象是否有某属性；`getattr` 动态获取属性值；`setattr` 动态设置属性值。它们常用于配置驱动和反射式调用。

### 22. isinstance() 和 type() 的区别
- tags: 类型判断, 面向对象
- difficulty: easy
- prompt: `isinstance()` 和 `type()` 有什么区别？
- answer: `type()` 更强调精确类型判断；`isinstance()` 会考虑继承关系。开发里通常更推荐 `isinstance()`。

### 23. __name__ == "__main__" 的作用
- tags: 模块, 基础语法
- difficulty: easy
- prompt: `if __name__ == "__main__"` 是做什么的？
- answer: 用来区分当前文件是被直接运行还是被导入。直接运行时 `__name__` 为 `__main__`，常用于脚本入口和测试代码隔离。

### 24. @staticmethod 为什么不需要 self
- tags: 面向对象, 静态方法
- difficulty: easy
- prompt: `@staticmethod` 为什么不需要 `self`？
- answer: 因为静态方法不会自动绑定实例对象或类对象，本质上只是定义在类命名空间中的普通函数，所以不需要 `self`。

### 25. strip()、lstrip()、rstrip() 的区别
- tags: 字符串, 基础语法
- difficulty: easy
- prompt: `strip()`、`lstrip()`、`rstrip()` 有什么区别？
- answer: `strip()` 去掉两端字符；`lstrip()` 去掉左边；`rstrip()` 去掉右边。默认处理空白字符，也可以指定字符集合。

### 26. join() 和 + 拼接字符串的区别
- tags: 字符串, 性能
- difficulty: easy
- prompt: `join()` 是做什么的？和 `+` 拼接字符串有什么区别？
- answer: `join()` 用于把一组字符串按指定分隔符拼接起来，适合批量拼接；`+` 更适合少量字符串连接。大量拼接时 `join()` 通常更高效。

### 27. append() 和 extend() 的区别
- tags: 列表, 基础语法
- difficulty: easy
- prompt: `append()` 和 `extend()` 有什么区别？
- answer: `append()` 把整个对象作为一个元素追加；`extend()` 会把可迭代对象拆开后逐个追加。

### 28. remove()、pop()、del 的区别
- tags: 列表, 删除操作
- difficulty: easy
- prompt: `remove()`、`pop()`、`del` 有什么区别？
- answer: `remove()` 按值删除第一个匹配项；`pop()` 按索引删除并返回元素；`del` 是通用删除语句，可删元素、切片甚至变量。

### 29. sort() 和 sorted() 的区别
- tags: 排序, 列表
- difficulty: easy
- prompt: `sort()` 和 `sorted()` 有什么区别？
- answer: `sort()` 是列表的原地排序方法，会修改原列表；`sorted()` 是内置函数，返回新列表，不改原对象。

### 30. tuple 和 list 有什么区别
- tags: 数据结构, 基础语法
- difficulty: easy
- prompt: `tuple` 和 `list` 有什么区别？
- answer: `list` 可变，适合频繁增删改；`tuple` 不可变，更适合表达固定结构和只读语义，也更适合做字典 key（元素需可哈希）。

### 31. dict.get(key) 和 dict[key] 的区别
- tags: 字典, 基础语法
- difficulty: easy
- prompt: `dict.get(key)` 和 `dict[key]` 有什么区别？
- answer: `dict[key]` 在 key 不存在时会抛 `KeyError`；`dict.get(key)` 不报错，默认返回 `None` 或指定默认值，更适合处理可选字段。

### 32. lambda 和 def 有什么区别
- tags: lambda, 函数定义
- difficulty: easy
- prompt: `lambda` 和 `def` 有什么区别？
- answer: `lambda` 用于定义简单匿名函数，只能写单个表达式；`def` 用于定义正式函数，支持多行逻辑，更适合复杂、可复用场景。

### 33. map() 和列表推导式有什么区别
- tags: map, 列表推导式
- difficulty: easy
- prompt: `map()` 和列表推导式有什么区别？
- answer: `map()` 是函数式写法，返回迭代器；列表推导式更直观，直接返回列表。简单转换场景通常优先用列表推导式。

### 34. is 和 == 有什么区别
- tags: 运算符, 易错点
- difficulty: easy
- prompt: `is` 和 `==` 有什么区别？
- answer: `==` 比较值是否相等；`is` 比较是否是同一个对象。判断 `None` 时通常推荐用 `is`。

### 35. mutable 和 immutable 对象有哪些，区别是什么
- tags: 数据类型, 内存模型
- difficulty: medium
- prompt: Python 中常见的可变对象和不可变对象有哪些？区别是什么？
- answer: list、dict、set 是可变对象；int、float、str、tuple 通常是不可变对象。可变对象内容可原地修改，不可变对象修改时会创建新对象。

### 36. Python 的参数传递方式怎么理解
- tags: 函数参数, 内存模型
- difficulty: medium
- prompt: Python 的函数参数传递方式应该怎么理解？
- answer: Python 不是传统意义上的值传递或引用传递，更准确说是“对象引用传递”。函数接收到的是对象引用，是否影响外部取决于对象是否可变以及是否原地修改。

### 37. 迭代器协议是什么
- tags: 迭代器, 协议
- difficulty: medium
- prompt: 什么是 Python 的迭代器协议？
- answer: 一个对象如果实现了 `__iter__()` 返回迭代器对象，并且该迭代器实现了 `__next__()`，就符合迭代器协议。`for` 循环正是基于这个协议工作的。

### 38. 为什么说生成器更省内存
- tags: 生成器, 性能
- difficulty: easy
- prompt: 为什么说生成器比列表更省内存？
- answer: 因为生成器按需逐个产出值，不会一次性把所有结果都放进内存；而列表会一次性构造完整结果，在大数据场景下内存开销更大。

### 39. Python 的字典为什么查找快
- tags: 字典, 数据结构
- difficulty: medium
- prompt: Python 的字典为什么查找速度快？
- answer: 因为字典底层基于哈希表，通过 key 的哈希值快速定位存储位置，平均时间复杂度通常是 O(1)。

### 40. 面向对象三大特性是什么
- tags: 面向对象, 理论基础
- difficulty: easy
- prompt: Python 中面向对象的三大特性是什么？
- answer: 封装、继承、多态。封装强调隐藏实现细节，继承强调代码复用，多态强调同一接口在不同对象上的不同表现。

### 41. 什么是多态，在 Python 里怎么理解
- tags: 面向对象, 多态
- difficulty: medium
- prompt: 什么是多态？在 Python 里怎么理解多态？
- answer: 多态指同一接口可作用于不同类型对象，并表现出不同结果。Python 更强调鸭子类型，不强依赖继承关系，只要对象实现了所需行为即可使用。

### 42. 什么是鸭子类型
- tags: 面向对象, 鸭子类型
- difficulty: medium
- prompt: 什么是鸭子类型？
- answer: 鸭子类型强调“只关心对象有没有某种行为，而不关心它是不是某个具体类型”。如果对象实现了需要的方法，就可以被当成对应角色来用。

### 43. super() 的作用是什么
- tags: 面向对象, 继承
- difficulty: medium
- prompt: `super()` 的作用是什么？
- answer: `super()` 用于在子类中调用父类方法，避免直接写死父类名。它在多继承场景下还能按照 MRO 顺序正确分发调用。

### 44. 什么是 MRO
- tags: 面向对象, 多继承
- difficulty: medium
- prompt: 什么是 MRO？为什么它重要？
- answer: MRO 是方法解析顺序，决定了多继承场景下属性和方法的查找路径。Python 使用 C3 线性化算法来保证查找顺序一致且可预测。

### 45. property 的作用是什么
- tags: 面向对象, property
- difficulty: easy
- prompt: `property` 是做什么的？有什么好处？
- answer: `property` 可以把方法伪装成属性访问，既保留属性式调用体验，又能在读取/设置时加入校验和控制逻辑。

### 46. Python 中常见的魔术方法有哪些
- tags: 面向对象, 魔术方法
- difficulty: medium
- prompt: Python 中常见的魔术方法有哪些？各自大概做什么？
- answer: 常见如 `__init__` 初始化对象、`__str__` 用户可读输出、`__repr__` 调试输出、`__len__` 定义 `len()` 行为、`__iter__` 定义迭代行为、`__call__` 让对象像函数一样可调用。

### 47. 什么是可哈希对象
- tags: 哈希, 数据类型
- difficulty: medium
- prompt: 什么是可哈希对象？为什么字典 key 要求可哈希？
- answer: 可哈希对象拥有稳定不变的哈希值，并且实现相等比较。字典 key 依赖哈希值定位存储位置，所以要求 key 可哈希且通常不可变。

### 48. Python 中异常为什么不建议裸 except
- tags: 异常处理, 代码质量
- difficulty: easy
- prompt: 为什么不建议直接写裸 `except`？
- answer: 因为裸 `except` 会捕获几乎所有异常，容易把真正的问题吞掉，导致排查困难。更推荐捕获明确异常类型。

### 49. pass、continue、break 的区别
- tags: 控制流, 基础语法
- difficulty: easy
- prompt: `pass`、`continue`、`break` 有什么区别？
- answer: `pass` 是占位语句，什么都不做；`continue` 跳过本轮循环剩余代码，进入下一轮；`break` 直接结束整个循环。

### 50. enumerate() 的作用是什么
- tags: 迭代, 基础语法
- difficulty: easy
- prompt: `enumerate()` 是做什么的？
- answer: `enumerate()` 用于在遍历可迭代对象时，同时拿到索引和值，常见写法是 `for i, item in enumerate(data):`，比手动维护下标更清晰。

### 51. zip() 的作用是什么
- tags: 迭代, 基础语法
- difficulty: easy
- prompt: `zip()` 是做什么的？
- answer: `zip()` 用于把多个可迭代对象按位置打包在一起，常用于并行遍历。最短的可迭代对象耗尽后就停止。

### 52. 为什么不建议在遍历列表时直接删除元素
- tags: 列表, 易错点
- difficulty: medium
- prompt: 为什么不建议在遍历列表时直接删除元素？
- answer: 因为删除元素会导致后续元素前移，容易跳过部分元素或引发逻辑错误。更稳妥的方式是生成新列表，或倒序遍历后删除。

### 53. Python 中常见的数据结构时间复杂度要掌握哪些
- tags: 数据结构, 复杂度
- difficulty: medium
- prompt: Python 面试里常见的数据结构时间复杂度，通常需要掌握哪些？
- answer: 通常要掌握 list 的尾部 append 平均 O(1)、中间插入删除 O(n)，dict/set 查找平均 O(1)，排序通常 O(n log n)。重点不是背表，而是知道何时选什么结构。

### 54. Python 为什么适合写脚本和自动化
- tags: Python 特性, 工程实践
- difficulty: easy
- prompt: Python 为什么特别适合写脚本和自动化？
- answer: 因为语法简洁、标准库丰富、开发效率高，生态完善，适合快速处理文件、网络请求、数据清洗、测试自动化和运维脚本。

### 55. Python 面试里说“可读性强”具体强在哪
- tags: Python 特性, 语言设计
- difficulty: easy
- prompt: Python 经常被说“可读性强”，具体强在哪？
- answer: 主要体现在语法简洁、强制缩进、标准写法统一、内置高层抽象多，很多逻辑能用更少、更直观的代码表达出来，团队协作成本也更低。

### 56. Python 的 LEGB 作用域规则是什么
- tags: Python 基础, 作用域
- difficulty: medium
- prompt: Python 查找变量时遵循什么顺序？LEGB 是什么意思？
- answer: LEGB 就是 Python 找变量的四层顺序：Local（当前函数内部）→ Enclosing（外层函数）→ Global（模块级全局）→ Builtin（内置命名空间）。找变量时从里往外一层层找，找到就用，全找不到才报 NameError。可以补一句：函数里想改全局变量要声明 global，改外层函数的变量要声明 nonlocal，这就是 LEGB 规则的直接应用。

### 57. 推导式有哪几种？怎么加条件
- tags: Python 基础, 推导式
- difficulty: easy
- prompt: 列表、字典、集合推导式分别怎么写？怎么加筛选条件？
- answer: 推导式就是一行表达式生成一个序列，核心格式是「表达式 for 变量 in 可迭代对象」。列表用方括号 `[x*x for x in range(10)]`，集合把方括号换成花括号，字典是 `{k: v for k, v in d.items()}`。筛选条件写在 for 后面，如 `[x for x in nums if x > 0]`；if-else 二选一则写在 for 前面，如 `[x if x > 0 else 0 for x in nums]`。收尾提一句：推导式适合简单逻辑，一旦嵌套超过两层就该老老实实写 for 循环，别牺牲可读性。

### 58. 星号解包有哪几种用法
- tags: Python 基础, 解包
- difficulty: medium
- prompt: a, *b = [1,2,3,4] 是什么意思？星号在赋值和函数调用里分别怎么用？
- answer: 星号在 Python 里就是「打包/解包」。赋值时 `a, *b = [1,2,3,4]` 会把 1 给 a，剩下的 [2,3,4] 打包成列表给 b；函数定义里的 `*args` 把多余位置参数收成元组、`**kwargs` 收成字典。反过来，函数调用时 `f(*list)` 把列表拆成一个个位置参数、`f(**dict)` 拆成关键字参数。一句话总结：定义时星号是收集，调用时星号是打散。

### 59. 切片的规则是什么？负步长怎么理解
- tags: Python 基础, 切片
- difficulty: medium
- prompt: s[a:b:c] 各参数什么含义？[::-1] 为什么能反转字符串？
- answer: 切片格式是 s[起:止:步长]，三个都可选。规则两条：左闭右开（包含起、不包含止），省略时起点默认开头、终点默认结尾。步长为负就是倒着取，起点默认变成末尾，所以 `s[::-1]` 就是整个字符串反转，这是最常用的记忆点。再比如 `s[::2]` 是隔一个取一个。切片越界不报错（返回能取到的部分），这点和直接下标访问不一样。

### 60. Python 的 dict 是有序的吗
- tags: Python 基础, 字典
- difficulty: medium
- prompt: 字典的插入顺序能保证吗？从哪个版本开始？
- answer: 能。Python 3.7 起字典正式保证「按插入顺序遍历」，3.6 是 CPython 的实现顺带支持。原理是字典内部除了哈希表还维护了一条插入顺序链，遍历时按链走而不是按哈希槽走。面试加分点：在这之前如果想用有序字典得用 `collections.OrderedDict`，现在它只剩两个场景——需要 move_to_end 之类的方法，或者要显式表达「顺序很重要」这个意图。

### 61. 什么是字符串驻留
- tags: Python 底层, 字符串
- difficulty: hard
- prompt: 为什么有时候两个内容相同的字符串 is 判断是 True？
- answer: 字符串驻留是 Python 的一个优化：内容相同的字符串可能共用同一个对象，这样比较和内存都省。触发条件有讲究——编译期能确定的字面量（比如代码里直接写的 "abc"）、短的、长得像标识符的更容易被驻留；运行时拼接出来的、长的就不一定。所以两个相同内容的字符串 is 可能是 True 也可能是 False，结果不稳定。结论就一句：判断内容相等永远用 ==，is 只留给 None / True / False 这些单例。

### 62. 小整数缓存池是什么
- tags: Python 底层, 对象模型
- difficulty: hard
- prompt: 为什么 a = 100; b = 100 时 a is b 是 True，换成 1000 就不一定了？
- answer: CPython 启动时会把 -5 到 256 这段常用小整数提前创建好，所有用到这些数的地方引用同一批对象，所以 100 is 100 是 True。超过这个范围的整数是按需新建的，两个 1000 可能是两个对象，is 就是 False。这个设计的出发点是小整数使用频率极高，缓存能省大量创建开销。面试要点就两个：缓存范围是 -5~256；这再次说明 is 只该用于 None 等单例，数值比较用 ==。

### 63. 带参数的装饰器怎么写
- tags: Python 进阶, 装饰器
- difficulty: hard
- prompt: @deco(arg) 这种带参数的装饰器怎么实现？
- answer: 普通装饰器是两层（外层收函数、内层收参数），带参数的装饰器要三层：最外层收装饰器参数，中间层收被装饰函数，最里层收调用参数。结构记成「参数层、函数层、调用层」。写法上就是再包一层函数，装饰器参数在参数层闭包住，最里层正常执行 func(*args, **kwargs) 并做增强。典型应用是 @repeat(3) 这种控制执行次数、或给接口测试加 @retry(times=5) 重试逻辑。收尾提一句：这也是面试里判断装饰器是否真懂的常见分水岭题。

### 64. functools.wraps 是做什么的
- tags: Python 进阶, 装饰器
- difficulty: medium
- prompt: 写装饰器时为什么通常要加 @functools.wraps(func)？
- answer: 因为装饰器本质是用内层函数替换原函数，替换后原函数的 __name__、__doc__ 这些元信息全变成内层函数的了，日志和调试信息会错乱。`@functools.wraps(func)` 放在内层函数上，作用就是把原函数的元信息拷贝过来。写法是固定的：在 def wrapper 上加一行 `@functools.wraps(func)`。一句话总结：这是装饰器的标准礼仪，不加功能上大多没事，但面试写装饰器不加会被认为不严谨。

### 65. 多个装饰器叠加时执行顺序是怎样的
- tags: Python 进阶, 装饰器
- difficulty: medium
- prompt: @A @B def f() 两个装饰器，执行顺序是什么？
- answer: 记住一句话：装饰时从下往上（离函数近的先包装），调用时从上往下（离函数远的先执行）。`@A @B def f` 等价于 `f = A(B(f))`，所以 B 先把 f 包一层，A 再把结果包一层；调用 f 时自然先进入 A 的逻辑，再进 B，最后才是原函数。这个顺序和数学里复合函数完全一致。面试常拿日志+计时两个装饰器叠加密码问「哪条日志先打印」，用「下装上调」四个字就能答对。

### 66. 偏函数 functools.partial 是什么
- tags: Python 进阶, 函数式
- difficulty: medium
- prompt: functools.partial 是干什么的？什么时候用？
- answer: partial 就是「预先固定一部分参数，生成一个新函数」。比如 `int2 = functools.partial(int, base=2)`，之后 int2("1010") 就自动按二进制转，不用每次传 base。它解决的是「一个函数某几个参数总是固定值」的重复问题。和默认参数的区别：默认参数要改原函数，partial 不动原函数、随时按需造新函数。典型场景是回调注册、多进程 map 时固定额外参数。一句话：partial 是运行时的「参数模板」。

### 67. 回调函数是什么
- tags: Python 进阶, 函数式
- difficulty: easy
- prompt: 什么是回调函数？Python 里怎么体现？
- answer: 回调就是「把函数当参数传给别人，让别人在合适的时机替你调用」。核心依据是 Python 函数是一等公民，能赋值、能当参数、能当返回值。最常见的就是 `sorted(data, key=len)`，把 len 交给 sorted，sorted 在比较时回调它；再比如定时任务、事件绑定、requests 的 hooks 也是回调。写测试时用 unittest.mock 打桩，本质也是替换回调行为。一句话：回调是控制反转的基础，框架和库到处都在用。

### 68. Python 的递归深度有限制吗
- tags: Python 基础, 递归
- difficulty: easy
- prompt: Python 递归能无限深吗？默认限制是多少？
- answer: 不能。CPython 默认递归深度限制是 1000 层，超过就抛 RecursionError，这是为了防止栈溢出直接崩掉解释器。用 `sys.getrecursionlimit()` 能查，`sys.setrecursionlimit(n)` 能改，但面试时要主动补一句：改大只是治标，深度递归本身就不对劲，正确做法是改成循环（迭代）或者用显式的栈/队列。这个「知道限制 + 给出正确替代方案」的组合才是面试官想听的。

### 69. 什么是尾递归？Python 支持吗
- tags: Python 进阶, 递归
- difficulty: hard
- prompt: 尾递归优化是什么？Python 为什么不做？
- answer: 尾递归是指递归调用是函数最后一步操作、返回值直接向上传，不再有后续计算。理论上这种递归可以优化成循环，不增长调用栈。但 CPython 官方明确不做尾递归优化，Guido 的态度是保留完整的调用栈对调试更有价值。所以结论是：Python 里再标准的尾递归也一样吃栈、一样撞 1000 层限制，深度递归必须手动改成 while 循环。这题答出「知道概念 + Python 不支持 + 怎么改写」三层就满分。

### 70. 单下划线和双下划线开头的名字有什么区别
- tags: Python 面向对象, 命名约定
- difficulty: medium
- prompt: _name、__name、__name__ 三种写法分别代表什么？
- answer: 三种含义完全不同。`_name` 是弱私有，纯约定：告诉别人“这是内部用的，别从外面调”，但语法上拦不住。`__name` 是强私有，类内部会触发名称改写（name mangling），实际存成 `_类名__name`，子类和外部直接按原名访问不到，主要用于避免继承时的命名冲突。`__name__` 是魔术方法/魔法属性，是 Python 自己的协议预留，比如 __init__、__len__，我们自己不要发明这种名字。一句话：一条下划线靠自觉，两条下划线靠改写，两条夹着是 Python 的保留地。

### 71. 什么是猴子补丁
- tags: Python 进阶, 动态性
- difficulty: medium
- prompt: 猴子补丁（monkey patch）是什么？测试里有什么用？
- answer: 猴子补丁就是在运行时直接替换模块、类或对象的属性，比如 `requests.get = my_fake_get`，让后续调用全走你的假实现。这依赖 Python 一切皆对象、属性可动态改的特性。测试里它就是 mock 的底层原理——把依赖的外部接口（网络请求、数据库、时间）替换成可控的假对象，让用例不依赖外部环境。也要主动提风险：补丁影响是全局的，测试里要用 mock 框架自动打补丁和还原，避免污染其他用例；生产代码里打猴子补丁一般被认为是坏味道。

### 72. 什么是序列化？Python 里怎么做
- tags: Python 基础, 序列化
- difficulty: easy
- prompt: 序列化和反序列化是什么？Python 里常用什么实现？
- answer: 序列化就是把内存里的对象转成可以存储或传输的格式（字符串/字节），反序列化就是反过来还原成对象。Python 里最常用的是 json 模块：`json.dumps()` 转字符串、`json.loads()` 还原，另外 `json.dump/load` 直接对接文件。做接口测试时天天用——发请求前 dumps 把参数转成 JSON 字符串，拿到响应后 loads 解析再断言。要点是 json 只认基础类型（dict/list/str/数字等），自定义对象要先转成 dict 才能序列化。

### 73. pickle 和 json 有什么区别
- tags: Python 基础, 序列化
- difficulty: medium
- prompt: pickle 和 json 都能序列化，怎么选？
- answer: 三个维度对比。格式上：json 是文本、跨语言通用，pickle 是 Python 专用的二进制。能力上：json 只支持基础类型，pickle 几乎能存任何 Python 对象，包括自定义类实例、函数。安全性上：pickle 反序列化会执行代码，加载不可信来源的 pickle 文件等于远程执行漏洞。所以结论很明确：对外交互、接口传输一律用 json；pickle 只用于自己程序内部的临时缓存，且绝不能加载来路不明的文件。安全这条是面试的关键得分点。

### 74. 什么是元类
- tags: Python 高阶, 元类
- difficulty: hard
- prompt: 元类是什么？什么场景会用到？
- answer: 一句话定义：类是用来创建实例的模板，元类就是用来创建类的模板——type 就是所有类默认的元类。验证方式是 `type(Foo)` 返回 type，而 `type(f)` 返回 Foo。执行顺序上，元类的 __new__ 和 __init__ 在 class 定义时（而不是实例化时）就被调用，所以能用它拦截、检查、改写类的定义。实际场景：ORM 框架（如 Django Model 把字段映射成数据库列）、自动注册子类的插件系统、接口契约检查。面试收尾可以降调：业务开发很少直接写元类，但理解它能解释“框架为什么能在类定义时做那么多事”。

### 75. __init__.py 的作用是什么
- tags: Python 工程化, 包管理
- difficulty: easy
- prompt: 包目录下的 __init__.py 是干什么的？可以为空吗？
- answer: 两个作用：一是把一个目录标记成包（package），让 Python 能 import 里面的模块；二是作为包的初始化入口，包被导入时它先执行。可以为空，纯粹起标记作用。进阶用法：在里面写 `from .module import xxx`，让外部直接 `import mypkg` 就能用功能，不用关心内部文件结构；还能定义 __all__ 控制 `from mypkg import *` 的范围。补充一句：Python 3.3+ 有命名空间包可以没有 __init__.py，但工程实践里还是建议保留，兼容性和意图都更清晰。

### 76. 模块和包有什么区别
- tags: Python 工程化, 包管理
- difficulty: easy
- prompt: module 和 package 是一回事吗？
- answer: 不是一回事但关系简单：模块就是一个 .py 文件，包是一个带 __init__.py 的目录，包可以嵌套包和模块，本质上是「用目录组织的模块集合」。两者在 import 语法上没区别，`import a.b.c` 时 a、b 是包、c 是模块。从导入机制看，包在被导入时会先变成一个模块对象（执行 __init__.py），所以说「包是一种特殊的模块」也对。一句话总结：模块是文件，包是目录，import 用起来一样。

### 77. import 一个模块时 Python 怎么找它
- tags: Python 工程化, 导入机制
- difficulty: medium
- prompt: import 的搜索顺序是什么？
- answer: 按顺序查四层：先查 sys.modules 缓存（已导入过直接用，所以模块只会真正执行一次）；再查内置模块；然后按 sys.path 列表从前往后找——sys.path 依次包含脚本所在目录、PYTHONPATH 环境变量、安装的第三方库 site-packages；都找不到就报 ModuleNotFoundError。排查导入问题的套路就是顺着这个顺序来：先确认模块名没写错，再 print(sys.path) 看目标目录在不在里面。面试加分点：提到 sys.modules 缓存和「模块天然是单例」这个推论。

### 78. 循环导入是什么？怎么解决
- tags: Python 工程化, 导入机制
- difficulty: medium
- prompt: 两个模块互相 import 会怎样？怎么破？
- answer: 循环导入就是 A import B、B 又 import A，结果谁都没加载完就互相要对方的东西，典型报错是 `cannot import name 'xxx' (most likely due to a circular import)`。解决三招：一是把 import 挪到函数内部（延迟导入），用的时候才触发；二是把两个模块互相依赖的部分抽到第三个公共模块，让依赖变成单向；三是调整 import 位置到模块底部。根治办法是第二招——循环依赖本质是设计问题，说明职责没切干净。测试框架里 conftest 和工具模块之间最容易犯这个错。

### 79. 为什么每个项目要用虚拟环境
- tags: Python 工程化, 环境
- difficulty: easy
- prompt: 虚拟环境解决什么问题？怎么创建？
- answer: 解决的是「多个项目依赖打架」的问题：A 项目要 requests 2.20、B 项目要 2.31，都装在全局必然冲突。虚拟环境给每个项目一份独立的 site-packages，互不干扰，还能锁版本保证「我这里能跑、你那里也能跑」。用法三步：`python -m venv .venv` 创建，Windows 下 `.venv\Scripts\activate` 激活（Linux 是 source .venv/bin/activate），然后 pip install 的所有东西都只进这个环境。做自动化测试时多项目并行、CI 里隔离依赖，虚拟环境都是标配。

### 80. requirements.txt 是干什么的
- tags: Python 工程化, 依赖管理
- difficulty: easy
- prompt: requirements.txt 怎么生成和使用？
- answer: 它是项目的依赖清单，一行一个「包名==版本」，让别人或 CI 一条命令装出一模一样的环境：`pip install -r requirements.txt`。生成方式是激活虚拟环境后 `pip freeze > requirements.txt`。两个实践要点：一是要锁版本（==），否则别人装到新版本可能不兼容，用例莫名挂掉；二是只把直接依赖写进去、从干净环境生成，freeze 会把传递依赖也带出来，列表会很臃肿。面试可补一句：新项目可以用 pyproject.toml 管理依赖，是更现代的方式。

### 81. 怎么观察一个对象的引用计数
- tags: Python 底层, 内存管理
- difficulty: medium
- prompt: 引用计数是什么？怎么验证？
- answer: Python 里每个对象都记着「有多少个名字在引用我」，计数归零就立刻回收，这是垃圾回收的第一层机制。用 `sys.getrefcount(obj)` 能查看，但打印出来的值比真实多 1，因为 getrefcount 调用本身临时多引用了一次——这个细节是常见考点。引用计数的问题是解决不了循环引用（a 引用 b、b 又引用 a，计数永远不为 0），所以 Python 还配了第二层：标记-清除和分代回收专门处理循环垃圾。这样「两层机制 + getrefcount 多 1」三个点答全就是满分。

### 82. Python 里怎么排查内存泄漏
- tags: Python 底层, 内存管理
- difficulty: hard
- prompt: 服务或长时间跑的脚本内存一直涨，怎么排查？
- answer: 排查思路四步。第一步确认现象：用 psutil 或容器监控确认内存确实持续增长、不是缓存正常的涨。第二步找增长对象：标准库 tracemalloc 对比两个时间点的对象快照，看是哪类对象在涨、在哪行代码分配的。第三步分析原因：常见元凶是全局容器只增不减（列表/字典当缓存不清理）、循环引用挂在大对象上、闭包或缓存把大对象一直带着。第四步修复并验证：改成弱引用或 LRU 上限（functools.lru_cache(maxsize=...)），再跑同样的监控确认平稳。能报出 tracemalloc 和 lru_cache 这两个工具名，面试官就知道你真排查过。

### 83. weakref 弱引用是干什么的
- tags: Python 底层, 内存管理
- difficulty: hard
- prompt: 弱引用是什么？解决什么问题？
- answer: 弱引用是「引用一个对象但不增加它的引用计数」，对象只被弱引用指着时，垃圾回收照样可以回收它。它解决的是「想缓存/跟踪一个对象，又不想因为缓存的存在导致对象永远释放不掉」的问题。典型场景两个：缓存（functools.lru_cache 内部思路就是弱引用思想）、对象注册表/观察者模式（通知列表不该强持有订阅者）。用法上 `weakref.ref(obj)` 拿到的引用要调用一次才返回原对象，对象没了就返回 None，用之前必须判空。一句话：强引用决定生死，弱引用只是旁观。

### 84. collections 模块里有哪些常用的类
- tags: Python 标准库, collections
- difficulty: medium
- prompt: collections 里常用的类有哪些？各自解决什么问题？
- answer: 记住五个高频的。defaultdict：取不存在的 key 不报错、按工厂函数给默认值，做分组统计特别顺手。Counter：一行搞定计数，`Counter(words).most_common(3)` 直接出 top3。deque：双端队列，两头进出都是 O(1)，做滑动窗口、任务队列用它。namedtuple：给元组字段命名，代码可读性好还不失轻量。OrderedDict：有序字典，3.7 之后普通 dict 已经有序，主要用它的 move_to_end 方法（LRU 缓存经典实现）。答的时候最好每个带一个测试场景例子，比如用 Counter 统计接口返回的 status_code 分布。

### 85. itertools 里常用哪些函数
- tags: Python 标准库, itertools
- difficulty: medium
- prompt: itertools 常用函数有哪些？
- answer: 挑五个最常用的。chain：把多个可迭代对象串起来遍历，不用手动拼接。product：笛卡尔积，做测试用例的参数组合神器，两组参数全组合直接出。combinations / permutations：组合和排列，用例覆盖场景时很好用。groupby：按 key 分组连续元素（先排序再分组）。islice：给迭代器做切片，生成器没法直接下标，用它取前 N 个。做测试开发要重点记 product——参数化用例的笛卡尔积组合它一行搞定，比写嵌套循环优雅得多。

### 86. functools 里有哪些常用工具
- tags: Python 标准库, functools
- difficulty: medium
- prompt: 除了 wraps，functools 还有什么常用的？
- answer: 四个高频。lru_cache：给函数加缓存，重复入参直接返回上次结果，测试里 mock 数据源、加速重复计算常用，注意设 maxsize 防内存无限涨。partial：固定部分参数造新函数。reduce：把序列迭代收敛成一个值，比如算阶乘、多层 dict 取值，不过可读性争议大，能用循环就用循环。singledispatch：按第一个参数类型分派到不同实现，写多态工具函数时用。面试重点讲 lru_cache 的作用和 maxsize 注意点，其他顺带提名字即可。

### 87. pathlib 和 os.path 有什么区别
- tags: Python 标准库, 文件操作
- difficulty: easy
- prompt: 处理文件路径用 pathlib 还是 os.path？
- answer: 优先 pathlib，它是 3.4 引入的面向对象路径库。区别三点：写法上 pathlib 用 `/` 运算符拼接路径（`base / "data" / "x.json"`），比 os.path.join 一层套一层直观；能力上 Path 对象自带方法，`.exists()`、`.read_text()`、`.glob("**/*.py")` 一条链下来，os.path 只是拼字符串还得配 open/os.listdir；跨平台上 pathlib 自动处理 Windows 和 Linux 的分隔符差异。测试里递归找用例文件、读配置，pathify 写法明显更短。os.path 不是不能用，只是新代码没必要再选它。

### 88. 字符串格式化有哪几种方式
- tags: Python 基础, 字符串
- difficulty: easy
- prompt: %、format、f-string 三种格式化怎么选？
- answer: 三种从老到新。% 是最老的 C 风格（`"%s-%d" % (name, age)`），现在基本只在日志模块里见到。str.format() 是中间代（`"{}-{}".format(a, b)`），支持按位置、按名、按属性取值，还能嵌套模板复用。f-string 是 3.6+ 的首选（`f"{name}-{age}"`），表达式直接写在花括号里，性能也最好。结论一句话：新代码一律 f-string，需要「模板定义和使用分离」的场景（比如配置里的模板）用 format，% 能看懂就行。接口测试拼 URL、拼断言消息时 f-string 效率最高。

### 89. f-string 有哪些好用的写法
- tags: Python 基础, 字符串
- difficulty: medium
- prompt: f-string 除了 {} 里放变量，还有什么进阶用法？
- answer: 四个实用进阶。一是直接放表达式：`f"{a+b}"`、`f"{user.name}"`，不用提前定义中间变量。二是格式说明符：`f"{x:.2f}"` 保留两位小数、`f"{n:>10}"` 右对齐、`f"{ratio:.1%}"` 直接百分号，测试报告对齐输出靠这个。三是 `=` 调试写法：`f"{x=}"` 会输出成 `x=10`，打印中间变量特别省事。四是日期格式化：`f"{dt:%Y-%m-%d %H:%M}"`，跟 strftime 同一套占位符。记住 .2f 和 % 这两个，写断言消息和报告基本够用了。

### 90. 不用类怎么写上下文管理器
- tags: Python 进阶, 上下文管理器
- difficulty: medium
- prompt: 除了写 __enter__/__exit__ 类，还有什么更轻的方式？
- answer: 用 `contextlib.contextmanager` 装饰器加生成器，把两行代码拆成 yield 前后两段：yield 之前相当于 __enter__，之后相当于 __exit__，yield 出去的值就是 as 拿到的东西。比如做接口计时：函数里写 start = time.time()，yield requests.get(url)，finally 里算耗时——三五行就完成一个计时上下文。注意异常处理：with 块里抛的异常会在 yield 处重新抛出，所以收尾逻辑要么 try/finally 包住，要么明确要吞异常。测试框架里做临时环境、计时、数据库事务都爱用这种写法。

### 91. raise ... from ... 是做什么的
- tags: Python 基础, 异常
- difficulty: medium
- prompt: raise NewError from e 这个 from 是什么意思？
- answer: from 用来声明「异常链」——新异常是由哪个原异常引起的， traceback 里会打出 "The above exception was the direct cause of..."，两层堆栈都保留，排查时能看到完整因果。典型场景是在底层异常上包一层业务异常往上抛，比如接口测试框架里捕获 requests.Timeout，再 raise MyApiError("请求超时") from e。不加 from 的话 Python 会隐式记成 "During handling..."，因果不清晰；`from None` 则主动切断链条、只显示新异常。一句话：转抛异常时带 from e 是好习惯，保留现场方便定位。

### 92. 自定义异常怎么写
- tags: Python 基础, 异常
- difficulty: easy
- prompt: 项目里怎么定义自己的异常？
- answer: 标准写法是继承 Exception（或更具体的父类），类体一行 docstring 就够：`class ApiTestError(Exception): """接口测试基础异常"""`。工程上通常再建一个异常层级：顶层 BaseError，下面按模块分 NetworkError、AssertionError、DataError，各自的异常类可以加 __init__ 传额外信息（比如把接口响应存进异常，方便日志排查）。两个要点：一是别继承 BaseException，那会拦不住 Ctrl+C；二是自定义异常让上层能精确捕获 `except ApiTestError`，而不是一串裸 except，这是框架代码质量的直接体现。

### 93. EAFP 和 LBYL 是什么
- tags: Python 哲学, 编码风格
- difficulty: medium
- prompt: Python 推荐先检查再执行还是先执行再兜底？
- answer: 这是两种风格：LBYL 是 Look Before You Leap（三思而后行），先 if 判断再操作；EAFP 是 Easier to Ask Forgiveness than Permission（先斩后奏、错了再兜），直接干，用 try/except 接住。Python 官方更推崇 EAFP，因为判断和操作之间可能有并发窗口（查的时候存在、用的时候没了），而 try/except 是原子的。典型例子：取字典值用 `try: d[k] except KeyError` 优于先 `if k in d`。但别走极端——高频失败的路径用异常开销不小，可读性优先。能说出「Pythonic 偏向 EAFP + 举例」就够了。

### 94. 类型标注有什么用
- tags: Python 工程化, 类型系统
- difficulty: medium
- prompt: Python 不是动态语言吗，为什么还要写类型标注？
- answer: 类型标注（typing）不改变运行时行为——解释器基本不检查它，价值全在开发期：IDE 补全和跳转更准、mypy 静态检查提前抓住传参错误、代码即文档不用猜参数是什么。写法上函数签名 `def get(url: str, timeout: float = 3.0) -> dict:`，复杂类型用 `list[str]`、`dict[str, Any]`、`Optional[int]`。测试开发场景特别贴合：pytest 参数化的预期值、fixture 返回类型标清楚，用例可读性明显提升。收尾一句：标注是渐进式的，关键接口先标，不追求一步到位。

### 95. dataclass 是什么
- tags: Python 工程化, 数据类
- difficulty: medium
- prompt: @dataclass 装饰器解决什么问题？
- answer: 解决「纯数据类模板代码太多」的问题。以前一个数据类要手写 __init__、__repr__、__eq__，字段一多就是十几行重复代码。加 @dataclass 后，只要声明类属性，这三个方法自动生成：`@dataclass class Case: name: str; priority: int`，两行搞定。常用选项：`field(default_factory=list)` 解决可变默认值、`frozen=True` 生成不可变实例、`order=True` 顺带支持比较排序。测试场景直接对口：测试用例对象、接口响应模型、配置项，都是纯数据载体，用 dataclass 又短又标准。

### 96. 怎么分析 Python 程序的性能瓶颈
- tags: Python 工程化, 性能分析
- difficulty: medium
- prompt: 脚本跑得慢，怎么定位哪里慢？
- answer: 先测量再优化，别凭感觉。粗粒度用 time.perf_counter() 给可疑段落计时；系统化用 cProfile：`python -m cProfile -s cumulative test_run.py`，输出每个函数的调用次数和累计耗时，一眼看出热点函数；单函数精调用 timeit（`timeit.timeit(fn, number=1000)`）避免一次运行的偶然性。找到热点后的常见处理：循环内重复计算提到外面、用生成器省内存、字符串拼接改 join、纯计算密集段换算法或用 numpy。面试金句：瓶颈 80% 集中在 20% 的代码，cProfile 就是找那 20% 的工具。

### 97. Python 3.10 的 match-case 是什么
- tags: Python 特性, 新版本
- difficulty: medium
- prompt: match-case 和其他语言的 switch 一样吗？
- answer: 语法像 switch，能力更强：它做的是「结构化模式匹配」。基础用法 `match status: case 200: ... case 404|500: ...` 支持多值或匹配；进阶在于能直接解构数据，`case {"code": code, "data": data}:` 一行把 dict 的字段取出来，`case [first, *rest]:` 直接解包列表，还能加守卫条件 `case Point(x, y) if x == y:`。接口测试里按响应结构分支断言时很好用。注意两点：匹配是按顺序的、要留 case _ 兜底；3.10 以下版本不支持，用之前确认环境版本。

### 98. 听说过 Python 去掉 GIL 的尝试吗
- tags: Python 底层, 并发
- difficulty: hard
- prompt: GIL 有可能被移除吗？进展如何？
- answer: 有两条线。一条是 PEP 684，Python 3.12 起支持「每子解释器一个 GIL」，把解释器级别的锁下放到子解释器级别，多解释器进程内可以真并行，但普通用户用得还少。另一条是 PEP 703，基于 Sam Gross 的 nogil 项目，Python 3.13 起官方发布了实验性的 free-threaded 构建（无 GIL 版本），牺牲一些单线程性能换多线程真并行，仍是实验特性、需要单独下载。面试这样收尾：短期内生产环境还是按「有 GIL」来设计——IO 密集用多线程或异步、CPU 密集用多进程，同时说明自己关注 free-threading 的演进，体现技术视野。

### 99. __pycache__ 和 .pyc 文件是什么
- tags: Python 底层, 执行机制
- difficulty: easy
- prompt: 目录下的 __pycache__ 是什么？能删吗？
- answer: __pycache__ 存的是模块编译后的字节码文件（.pyc）。Python 执行 .py 时会先编译成字节码，编译结果缓存到 __pycache__，下次导入如果源文件没改（比对时间戳和大小）就直接用缓存，跳过编译、导入更快。可以放心删，删了只是下次导入重新编译一遍，功能零影响。两个实践点：一是它应该进 .gitignore；二是排查「代码明明改了行为没变」的诡异问题时，可以想到时间戳异常导致旧字节码没失效，删掉 __pycache__ 重跑就恢复。

### 100. a, b = b, a 为什么能交换变量
- tags: Python 基础, 语法糖
- difficulty: easy
- prompt: Python 一行交换两个变量的原理是什么？
- answer: 原理是元组打包加解包两步：右边的 `b, a` 先被打包成元组 (b, a)，然后左边按位置解包，把第一个值给 a、第二个给 b，交换就完成了，全程不需要临时变量。这背后是 Python 的序列解包协议，`a, *rest = [1,2,3]`、函数返回多值 `return x, y` 接收端 `x, y = f()` 都是同一套机制——多值返回本质就是返回一个元组。面试收尾可以带一句：这也是 Python 区别于 C/Java 需要 temp 中转变量的标志性写法，体现「表达式也是对象」的语言设计。
