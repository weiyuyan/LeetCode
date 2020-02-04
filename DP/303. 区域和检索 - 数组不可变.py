#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/3
'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

'''

from typing import List
# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         if not nums:
#             return
#         self.all_sum = [0, 0]
#         self.nums = nums
#         self.all_sum[1] = self.nums[0]
#         for i in range(1, len(nums)):
#             self.all_sum.append(self.all_sum[-1]+self.nums[i])
#
#         pass
#     def sumRange(self, i: int, j: int) -> int:
#
#         return self.all_sum[j+1] - self.all_sum[i]
class NumArray:

    def __init__(self, nums: List[int]):
        if(not nums):
            return
        n=len(nums)
        self.dp=[0]*(n+1)
        self.dp[1]=nums[0]
        for i in range(2,n+1):
            self.dp[i]=nums[i-1]+self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

solution = NumArray([])
res = solution.sumRange(0, 2)
print(res)