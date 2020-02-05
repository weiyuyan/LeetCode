#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/5
'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

'''
from typing import List
# 解法一：动态规划 时间复杂度O(n)，空间复杂度o(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max((nums[0]+nums[2]), nums[1])

        money = [nums[0], nums[1], nums[2]+nums[0]]   # 初始化money数组
        for i in range(3, len(nums)):
            money.append(max(money[i-2], money[i-3]) + nums[i])

        return max(money)
pass

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#         if len(nums) == 3:
#             return max((nums[0]+nums[2]), nums[1])
#         pre_money = nums[2]+nums[0]
#         pre_pre_money = nums[1]
#         for i in range(3, len(nums)):
#             money = max(pre_money, pre_pre_money)+nums[i]
#             pre_money = pre_pre_money
#             pre_pre_money = money
#
#         return money



solution = Solution()
res = solution.rob([2,7,9,3,1])
print(res)