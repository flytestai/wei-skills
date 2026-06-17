# Python编程基础理论面试题

### 2. 深拷贝和浅拷贝的区别
- tags: copy, data-types
- difficulty: easy
- prompt: 解释 Python 中深拷贝和浅拷贝的区别，并举例说明。
- answer: 浅拷贝只复制最外层对象，内部可变子对象仍共享；深拷贝会递归复制内部对象，彼此独立。可用 `copy.copy` 和 `copy.deepcopy` 区分。

### 3. 装饰器是什么
- tags: decorator, closure
- difficulty: easy
- prompt: 什么是装饰器？它解决什么问题？
- answer: 装饰器本质上是接收函数并返回新函数的高阶函数，常用于在不改原函数代码的前提下添加日志、鉴权、缓存等横切逻辑。

### 4. 生成器和迭代器的区别
- tags: generator, iterator
- difficulty: easy
- prompt: 解释生成器和迭代器的区别与联系。
- answer: 迭代器实现 `__iter__`/`__next__` 协议；生成器是创建迭代器的一种更便捷方式，通常由带 `yield` 的函数生成。

### 5. GIL 是什么
- tags: gil, concurrency
- difficulty: medium
- prompt: Python 的 GIL 是什么？它对多线程有什么影响？
- answer: GIL 是 CPython 的全局解释器锁，同一时刻只允许一个线程执行 Python 字节码。CPU 密集型任务受限明显，I/O 密集型任务仍可从多线程获益。

### 6. 协程和线程区别
- tags: coroutine, concurrency
- difficulty: medium
- prompt: 协程和线程有什么区别？
- answer: 线程由操作系统调度，开销较大；协程在用户态协作切换，开销更小，更适合大量 I/O 等待场景。
