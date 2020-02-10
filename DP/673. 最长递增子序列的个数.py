#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/10
'''
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
'''
from typing import List
class Solution(object):
    def findNumberOfLIS(self, nums):
        # N = len(nums)
        # if N <= 1: return N
        # lengths = [0] * N #lengths[i] = longest ending in nums[i]
        # counts = [1] * N #count[i] = number of longest ending in nums[i]
        #
        # for j, num in enumerate(nums):
        #     for i in range(j):
        #         if nums[i] < nums[j]:
        #             if lengths[i] >= lengths[j]:
        #                 lengths[j] = 1 + lengths[i]
        #                 counts[j] = counts[i]
        #             elif lengths[i] + 1 == lengths[j]:
        #                 counts[j] += counts[i]
        #
        # longest = max(lengths)
        # return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
        N = len(nums)
        if N <= 1:  return N
        lengths = [0] * N
        counts = [1] * N
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1+lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i]==longest)

solution = Solution()
res = solution.findNumberOfLIS([1,2,3,8,7])
print(res)