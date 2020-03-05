#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''
from typing import List
# 方法一：二分查找法
# 时间复杂度：o(nlogn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            tmp_target = target - nums[i]
            tmp_res = self.binarySearch(nums, i+1, len(nums)-1, tmp_target)
            if tmp_res is not 'None':
                return [nums[i], tmp_res]

    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target: return nums[mid]
            if nums[mid] < target: left = mid+1
            if nums[mid] > target: right = mid-1
        return 'None'


# 方法二：中心扩散寻找法
# 时间复杂度：o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start]+nums[end] == target: return [nums[start], nums[end]]
            if nums[start]+nums[end] < target: start+=1
            else: end-=1
        return None
solution = Solution()
nums = [16,16,18,24,30,32]; target = 48
res = solution.twoSum(nums, target)
print(res)
