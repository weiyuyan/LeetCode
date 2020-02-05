#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/5
'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''

# 时间复杂度：O(n)+O(n) = O(n)
# 空间复杂度：O(n)+O(n) = O(n)
from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return max(nums, default=0)
#         def _rob(_nums: List[int]) -> int:
#             if len(_nums) == 0:
#                 return 0
#             if len(_nums) == 1:
#                 return _nums[0]
#             if len(_nums) == 2:
#                 return max(_nums[0], _nums[1])
#             if len(_nums) == 3:
#                 return max((_nums[0] + _nums[2]), _nums[1])
#             money = [_nums[0], _nums[1], _nums[2]+_nums[0]]   # 初始化money数组
#             for i in range(3, len(_nums)): # 不打劫最后一家
#                 money.append(max(money[i-2], money[i-3]) + _nums[i])
#             return max(money)
#
#         return max(_rob(nums[1:]), _rob(nums[:-1]) )
pass

# 大神的答案，思路一样，但是更简洁。。。emmm，简洁得多
# class Solution:
#     def rob(self, nums: [int]) -> int:
#         def my_rob(nums):
#             cur, pre = 0, 0
#             for num in nums:
#                 cur, pre = max(pre + num, cur), cur
#             return cur
#         return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre+num, cur), cur
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

solution = Solution()
a_list = []
res = solution.rob(a_list)
print(res)