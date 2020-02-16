#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/16
'''
给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：

令 x 为你数组里所有元素的和
选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
你可以重复该过程任意次
如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。



示例 1：

输入：target = [9,3,5]
输出：true
解释：从 [1, 1, 1] 开始
[1, 1, 1], 和为 3 ，选择下标 1
[1, 3, 1], 和为 5， 选择下标 2
[1, 3, 5], 和为 9， 选择下标 0
[9, 3, 5] 完成
示例 2：

输入：target = [1,1,1,2]
输出：false
解释：不可能从 [1,1,1,1] 出发构造目标数组。
示例 3：

输入：target = [8,5]
输出：true


提示：

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
'''

'''
参考了力扣大佬“小白二号”的思路
顺着推肯定是没戏，我们考虑倒着推

按照题目意思，假设数组 [a1, a2, a3, a4,..., an]的和是 s，那么这个 s 肯定比这数组里面任一个数都要大。
不管替换成哪个数，生成出来的数组的最大值一定是 s 。

倒过来，假设数组 [b1. b2, b3, b4,..., bn] 是生成后的数组，那么最大值一定是上一轮的和。
假设这个最大值是 p ，当前数组的和是 s ，那么上一轮的数组的和是 p ，这个最大值替换成 p - (s - p)

这个题的解法就是不断的将最大值还原，直到整个数组都变成了1
'''

# from typing import List
# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#
#         while (sum(target) > len(target)):
#             tmp_sum = sum(target)
#             tmp_max = max(target)
#             pos = target.index(tmp_max)
#             target[pos] = tmp_max - (tmp_sum-tmp_max)
#             if target[pos] <= 0: return False
#
#         if sum(target) == len(target): return True
#
#         return False
'''
这。。。这就过了？？那我再优化一下下嚯嚯嚯
'''

# 优化版本
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        tmp_sum = sum(target)

        while (tmp_sum > len(target)):
            tmp_max = max(target)
            pos = target.index(tmp_max)
            # 上一个最大的值，target[pos]
            target[pos] = tmp_max - (tmp_sum-tmp_max)
            # 更新tmp_sum
            tmp_sum = tmp_sum + target[pos] - tmp_max
            if target[pos] <= 0: return False

        if sum(target) == len(target): return True

        return False

solution = Solution()
a = [9, 9, 1]
res = solution.isPossible(a)
print(res)
