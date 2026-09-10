# python-testdev-drill state

version: 2

last_active_module: Python基础手写代码题
last_active_mode: brush
last_batch_size: 1
answer_visibility: visible_in_brush_mode

## Module: Python基础手写代码题

module_name: Python基础手写代码题
completed_through: 15
next_question: 16
asked_questions:
  - 1. reverse_string
  - 2. count_characters
  - 3. dedup_list
  - 4. merge_sorted_lists
  - 5. sort_dict_by_value
  - 6. binary_search
  - 7. bubble_sort
  - 8. quick_sort
  - 9. fibonacci
  - 10. two_sum
  - 11. valid_parentheses
  - 12. longest_substring_without_repeat
  - 13. retry_decorator
  - 14. singleton
  - 15. context_manager
mistakes:
  - dedup_list | 逻辑正确，最后一行未调用函数直接打印原列表 | 2026-09-09 | 错1次 | 复习:2026-09-10
  - merge_sorted_lists | append写成整个列表、j+=2、extend未切片、缺return；重做后全对 | 2026-09-09 | 错1次 | 复习:2026-09-10
  - sort_dict_by_value | sorted的key=关键字遗漏、缺dict()转换 | 2026-09-09 | 错1次 | 复习:2026-09-10
  - binary_search | 首答mid漏括号、else误写left；重做后全对 | 2026-09-09 | 错1次 | 复习:2026-09-10
  - two_sum | set/dict用混：应存值→下标映射；targe拼写错；存补数方向反。口诀"查补数、存自己" | 2026-09-09 | 错1次 | 复习:2026-09-10
  - 12. longest_substring_without_repeat | 只扫描到第一次重复就break，等于只求了从下标0开始的前缀无重复长度；pwwkew 应返回3实际返回2。正确思路是滑动窗口：重复时收缩左边界继续扫，而不是整体停止 | 2026-09-10 | 错1次 | 复习:2026-09-11
  - 13. retry_decorator | 直接看答案：带参数装饰器（三层结构）不熟练 | 2026-09-10 | 错1次 | 复习:2026-09-11
  - 14. singleton | 直接看答案：单例模式写法待巩固 | 2026-09-10 | 错1次 | 复习:2026-09-11
  - 15. context_manager | 直接看答案：__enter__/__exit__ 自定义上下文管理器待巩固 | 2026-09-10 | 错1次 | 复习:2026-09-11
answer_given_questions:
history_questions:
  - 12. longest_substring_without_repeat
  - 13. retry_decorator
  - 14. singleton
  - 15. context_manager
favorite_questions:
custom_questions:
current_mode: brush
current_batch_size: 1
last_round_questions:
last_round_results:

## Module: Python高阶编程

module_name: Python高阶编程
completed_through: 34
next_question: 35
asked_questions:
  - 1. decorator_essence
  - 2. closure_essence
  - 3. iterator_vs_generator
  - 4. context_manager
  - 5. mutable_default_param
  - 6. shallow_vs_deep_copy
  - 7. new_vs_init
  - 8. super_and_mro
  - 9. property_usage
  - 10. slots_usage
  - 11. dunder_methods
  - 12. str_vs_repr
  - 13. len_dunder
  - 14. getitem_dunder
  - 15. setitem_dunder
  - 16. call_dunder
  - 17. iter_next_dunder
  - 18. generator_vs_iterator
  - 19. yield_vs_return
  - 20. closure_keeps_outer_scope
  - 21. nonlocal_vs_global
  - 22. decorator_essence_review
  - 23. iterable_vs_iterator
  - 24. for_loop_iterator_protocol
  - 25. lazy_iteration
  - 26. generator_function_vs_normal_function
  - 27. why_generator_save_memory
  - 28. when_prefer_generator
  - 29. gil_what_is_it
  - 30. why_gil_less_affects_io
  - 31. cpu_bound_why_multiprocessing
  - 32. thread_process_coroutine_how_to_choose
  - 33. why_coroutine_good_for_high_concurrency_io
  - 34. coroutine_vs_thread_core_difference
mistakes:
answer_given_questions:
history_questions:
  - decorator_essence
  - closure_essence
  - iterator_vs_generator
  - context_manager
  - mutable_default_param
  - shallow_vs_deep_copy
  - new_vs_init
  - super_and_mro
  - property_usage
  - slots_usage
  - dunder_methods
  - str_vs_repr
  - len_dunder
  - getitem_dunder
  - setitem_dunder
  - call_dunder
  - iter_next_dunder
  - generator_vs_iterator
  - yield_vs_return
  - closure_keeps_outer_scope
  - nonlocal_vs_global
  - decorator_essence_review
  - iterable_vs_iterator
  - for_loop_iterator_protocol
  - lazy_iteration
  - generator_function_vs_normal_function
  - why_generator_save_memory
  - when_prefer_generator
  - gil_what_is_it
  - why_gil_less_affects_io
  - cpu_bound_why_multiprocessing
  - thread_process_coroutine_how_to_choose
  - why_coroutine_good_for_high_concurrency_io
  - coroutine_vs_thread_core_difference
favorite_questions:
  - super_and_mro
custom_questions:
current_mode: brush
current_batch_size: 1
last_round_questions:
  - 34. coroutine_vs_thread_core_difference
last_round_results:
  - paused_after_brush_progress_saved

## Module: 自动化测试题

module_name: 自动化测试题
completed_through: 10
next_question: 11
asked_questions:
  - 1. api_testcase_design_dimensions
  - 2. api_assertion_layers
  - 3. which_api_should_be_automated_first
  - 4. why_ui_automation_flaky
  - 5. how_to_reduce_ui_flaky
  - 6. ui_vs_api_automation_layering
  - 7. app_automation_vs_web_ui_difference
  - 8. app_automation_common_difficulties
  - 9. api_automation_framework_design
  - 10. why_app_automation_keeps_only_core_cases
mistakes:
answer_given_questions:
history_questions:
  - api_testcase_design_dimensions
  - api_assertion_layers
  - which_api_should_be_automated_first
  - why_ui_automation_flaky
  - how_to_reduce_ui_flaky
  - ui_vs_api_automation_layering
  - app_automation_vs_web_ui_difference
  - app_automation_common_difficulties
  - api_automation_framework_design
  - why_app_automation_keeps_only_core_cases
favorite_questions:
custom_questions:
current_mode: brush
current_batch_size: 1
last_round_questions:
  - 10. why_app_automation_keeps_only_core_cases
last_round_results:
  - paused_after_brush_progress_saved

## Module: 性能测试面试题

module_name: 性能测试面试题
completed_through: 21
next_question: 22
asked_questions:
  - 1. 什么是性能测试，性能测试的目的是什么
  - 2. 性能测试和功能测试有什么区别
  - 3. 性能测试的主要类型有哪些
  - 4. 什么是 TPS 和 QPS，它们有什么区别
  - 5. 什么是响应时间，90% 响应时间是什么意思
  - 6. 什么是并发用户数，它和线程数是一个概念吗
  - 7. 什么是性能瓶颈，常见瓶颈有哪些
  - 8. 什么是思考时间，为什么要设置思考时间
  - 9. 什么是吞吐量，它和 TPS 有什么关系
  - 10. 什么是性能拐点，如何找到性能拐点
  - 11. 什么是容量规划，如何做容量规划
  - 12. 什么是性能基线，为什么要建立性能基线
  - 13. 什么是混合场景压测，和单接口压测有什么区别
  - 14. 性能测试报告应该包含哪些内容
  - 15. 什么是长尾请求，它有什么影响
  - 16. 什么是全链路压测，和普通压测有什么区别
  - 17. 性能测试中如何准备测试数据
  - 18. 什么是预热，为什么需要预热
  - 19. 性能测试通常什么时候做
  - 20. 性能测试和压力测试是一回事吗
  - 21. 性能测试中主要监控哪些指标
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: brush
current_batch_size: 1
last_round_questions:
  - 21. 性能测试中主要监控哪些指标
last_round_results:
  - question_issued_in_brush_mode
  - question_issued_in_brush_mode

## Module: 中间件面试题

module_name: 中间件面试题
completed_through: 0
next_question: 1
asked_questions:
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: module
current_batch_size: 1
last_round_questions:
last_round_results:

## Module: 数据库面试题

module_name: 数据库面试题
completed_through: 0
next_question: 1
asked_questions:
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: module
current_batch_size: 1
last_round_questions:
last_round_results:

## Module: Linux面试题

module_name: Linux面试题
completed_through: 0
next_question: 1
asked_questions:
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: module
current_batch_size: 1
last_round_questions:
last_round_results:

## Module: Pytest框架

module_name: Pytest框架
completed_through: 20
next_question: 21
asked_questions:
  - 1. fixture_basic
  - 2. fixture_vs_setup
  - 3. conftest_role
  - 4. fixture_scope
  - 5. fixture_autouse
  - 6. parametrize_basic
  - 7. skip_xfail
  - 8. mark_usage
  - 9. pytest_ini
  - 10. collection_rules
  - 11. fixture_dependency
  - 12. yield_fixture_cleanup
  - 13. plugin_ecosystem
  - 14. hook_basic
  - 15. fixture_best_practice
  - 16. conftest_role_advanced
  - 17. fixture_override_resolution
  - 18. pytest_generate_tests
  - 19. pytest_allure_integration
  - 20. pytest_xdist_precautions
mistakes:
answer_given_questions:
history_questions:
  - fixture_basic
  - fixture_vs_setup
  - conftest_role
  - fixture_scope
  - fixture_autouse
  - parametrize_basic
  - skip_xfail
  - mark_usage
  - pytest_ini
  - collection_rules
  - fixture_dependency
  - yield_fixture_cleanup
  - plugin_ecosystem
  - hook_basic
  - fixture_best_practice
  - conftest_role_advanced
  - fixture_override_resolution
  - pytest_generate_tests
  - pytest_allure_integration
  - pytest_xdist_precautions
favorite_questions:
  - pytest_ini
  - hook_basic
custom_questions:
current_mode: brush
current_batch_size: 1
last_round_questions:
  - 20. pytest_xdist_precautions
last_round_results:
  - paused_after_brush_progress_saved

## Module: 测试开发面试题

module_name: 测试开发面试题
completed_through: 0
next_question: 1
asked_questions:
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: module
current_batch_size: 1
last_round_questions:
last_round_results:

## Module: Python编程基础理论面试题

module_name: Python编程基础理论面试题
completed_through: 20
next_question: 21
asked_questions:
  - 1. *args 和 **kwargs 的区别
  - 2. 深拷贝和浅拷贝的区别
  - 3. 装饰器是什么
  - 4. 生成器和迭代器的区别
  - 5. GIL 是什么
  - 6. 协程和线程区别
  - 7. Python 的垃圾回收机制是怎样的
  - 8. 什么是闭包
  - 9. try / except / else / finally 分别有什么作用
  - 10. __new__ 和 __init__ 有什么区别，它们分别在什么时候执行
  - 11. with 语句和上下文管理器的原理
  - 12. lambda 表达式的适用场景和限制
  - 13. 列表推导式和生成器表达式有什么区别
  - 14. 可变类型默认参数的问题与规避方式
  - 15. @classmethod 和 @staticmethod 的区别与使用场景
  - 16. __str__ 和 __repr__ 的区别与使用场景
  - 17. set 和 list 的区别与适用场景
  - 18. read()、readline()、readlines() 的区别
  - 19. sorted() 和 list.sort() 的区别
  - 20. global 和 nonlocal 的区别
mistakes:
answer_given_questions:
history_questions:
  - 1. *args 和 **kwargs 的区别
  - 2. 深拷贝和浅拷贝的区别
  - 3. 装饰器是什么
  - 4. 生成器和迭代器的区别
  - 5. GIL 是什么
  - 6. 协程和线程区别
  - 7. Python 的垃圾回收机制是怎样的
  - 8. 什么是闭包
  - 9. try / except / else / finally 分别有什么作用
  - 10. __new__ 和 __init__ 有什么区别，它们分别在什么时候执行
  - 11. with 语句和上下文管理器的原理
  - 12. lambda 表达式的适用场景和限制
  - 13. 列表推导式和生成器表达式有什么区别
  - 14. 可变类型默认参数的问题与规避方式
  - 15. @classmethod 和 @staticmethod 的区别与使用场景
  - 16. __str__ 和 __repr__ 的区别与使用场景
  - 17. set 和 list 的区别与适用场景
  - 18. read()、readline()、readlines() 的区别
  - 19. sorted() 和 list.sort() 的区别
  - 20. global 和 nonlocal 的区别
favorite_questions:
custom_questions:
current_mode: brush
current_batch_size: 5
last_round_questions:
  - 16. __str__ 和 __repr__ 的区别与使用场景
  - 17. set 和 list 的区别与适用场景
  - 18. read()、readline()、readlines() 的区别
  - 19. sorted() 和 list.sort() 的区别
  - 20. global 和 nonlocal 的区别
last_round_results:
  - question_issued_in_brush_mode

## Module: 测试工程化与CI/CD

module_name: 测试工程化与CI/CD
completed_through: 0
next_question: 1
asked_questions:
mistakes:
answer_given_questions:
history_questions:
favorite_questions:
custom_questions:
current_mode: module
current_batch_size: 1
last_round_questions:
last_round_results:
