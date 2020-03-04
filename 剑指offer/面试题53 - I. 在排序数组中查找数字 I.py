#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/4
'''
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000
'''
from typing import List
# 方法一：对于排序数组，可以用二分法查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        if len(nums)==1 and nums[0]!=target: return 0
        if len(nums) == 1 and nums[0] == target: return 1
        if not nums: return 0
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = (left+right) >> 1
            if nums[mid]<target:
                left = mid
            if nums[mid]>target:
                right = mid
            if nums[mid]==target: break
        if nums[mid]==target:
            while mid-1>=0 and nums[mid-1]==target:
                mid-=1
        while nums[mid]==target and mid!=len(nums)-1:
            mid+=1
            res+=1
        return res

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        count, end = 0,len(nums)-1
        if nums[left] == target:
            while left <= end and nums[left] == target :
                left += 1
                count += 1
            return count
        elif nums[right] == target:
            while right <= end and nums[right] == target:
                right += 1
                count += 1
            return count
        else: return 0

solution = Solution()
nums = [1]
target = 0
res = solution.search(nums, target)
print(res)
