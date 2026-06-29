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
