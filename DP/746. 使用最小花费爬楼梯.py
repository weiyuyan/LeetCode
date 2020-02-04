#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/2
'''
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

'''

# 这道题可以看做70题的变形，解决方案也类似
# 方案一
from typing import List
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         num_stairs = len(cost)
#         store = [-1 for _ in range(num_stairs)]
#         # store[0] = cost[0]
#         store[0] = cost[0]
#         store[1] = cost[0] if num_stairs<2 else cost[1]
#         cost.append(0)  # cost[n]
#
#         for i in range(2, num_stairs):
#             if i == num_stairs-1:
#                 store[i] = min((store[i - 1] + 0), (store[i - 2] + cost[i]))
#             else:
#                 store[i] = min((store[i-1]+cost[i]), (store[i-2]+ cost[i]))
#
#         return store[num_stairs-1]

# 方案二 空间复杂度优化为o(1)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
solution = Solution()
res = solution.minCostClimbingStairs([10, 15, 20])
print(res)