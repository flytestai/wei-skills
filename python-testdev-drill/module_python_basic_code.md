# Python基础手写代码题

## easy

### 11. merge_two_sorted_lists
- tags: list, two-pointers
- prompt: 给定两个递增有序列表，返回合并后的递增列表。
- answer: 使用双指针依次比较两个列表当前元素，较小者加入结果，最后拼接剩余部分；时间复杂度 O(n+m)。

### 12. move_zeroes
- tags: list, two-pointers
- prompt: 将列表中的 0 移动到末尾，同时保持非 0 元素相对顺序不变。
- answer: 用快慢指针把非 0 元素依次前移，最后把剩余位置补 0；时间复杂度 O(n)。

### 13. valid_parentheses
- tags: stack, string
- prompt: 判断只包含 `()[]{}` 的字符串是否为有效括号串。
- answer: 用栈保存左括号，遇到右括号时检查栈顶是否匹配；最终栈空则有效。

### 14. two_sum
- tags: hash, list
- prompt: 在整数列表中找出和为目标值的两个元素下标。
- answer: 用哈希表记录已见元素和下标，遍历时检查 `target-num` 是否已存在；时间复杂度 O(n)。

### 15. dedup_sorted_array
- tags: list, two-pointers
- prompt: 删除有序列表中的重复元素，返回去重后的新长度。
- answer: 双指针，慢指针指向已处理末尾，快指针遍历，遇到新值就前移覆盖；时间复杂度 O(n)。

## medium

### 16. group_anagrams
- tags: string, dict, hash
- prompt: 将字符串列表中的变位词分组。
- answer: 以排序后的字符串或字符计数作为 key，用字典聚合原字符串列表。

### 17. top_k_frequent
- tags: dict, heap, sorting
- prompt: 返回列表中出现频率最高的前 k 个元素。
- answer: 先统计频率，再按频率排序或用堆取前 k 个。

### 18. longest_substring_without_repeat
- tags: string, sliding-window, hash
- prompt: 求不含重复字符的最长子串长度。
- answer: 滑动窗口 + 哈希表记录字符最近位置，动态收缩左边界。

### 19. merge_intervals
- tags: sorting, list
- prompt: 合并重叠区间。
- answer: 先按起点排序，再线性扫描，当前区间与结果末尾有重叠就合并，否则直接追加。

### 20. daily_temperatures
- tags: stack, list
- prompt: 对每天温度，求距离下一个更高温度还要等多少天。
- answer: 用单调栈保存未找到更高温的下标，当前温度更高时回填答案。
