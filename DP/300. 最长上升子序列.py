#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/10
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

'''
from typing import List
# 思考：可以用最优栈来解决
# 我庄严宣誓我没干好事（我是傻逼）
# 此法不通
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         stack = []
#         stack.append(nums[0])
#         for i in range(len(nums)):
#             if stack[-1] >= nums[i]:
#                 stack[-1] = nums[i]
#             else:
#                 stack.append(nums[i])
#         return stack

# class Solution:
    # 这不是递归，加这个没用
    # import functools
    # # @functools.lru_cache(None)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     dp = [1 for _ in range(len(nums))]
    #     for i in range(1, len(nums)):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i<j:
                m = (i+j) // 2
                if tails[m] < num: i=m+1
                else:   j=m
            tails[i] = num
            if j == res:    res += 1
        return res


solution = Solution()
res = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
print(res)