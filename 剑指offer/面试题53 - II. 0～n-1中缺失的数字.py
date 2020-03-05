#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/4
'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000
'''
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)-1

# 方法二：二分查找
# 如果中间元素的值和下标相等,那么下一轮查找只需查找右半边
# 如果中间元素的值和下标不相等,并且它前面一个元素和它的下标相等,这意味着这个中间的数字正好是第一个值和下标不相等的元素,它的下标就是在数组中不存在的数字
# 如果中间元素的值和下标不相等,并且他前面的一个元素和它的下标不相等,这意味着下一轮只需要查找左半边即可
class Solution(object):
    def missingNumber(self, nums):
        if not nums or len(nums) <= 0:
            return -1
        start = 0
        end = len(nums) - 1
        length = len(nums)
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] != mid:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                end = mid - 1
            else:
                start = mid + 1
            if start == length:
                return length
class Solution(object):
    def missingNumber(self, nums):
        if not nums or len(nums) <= 0: return -1
        start, end = 0, len(nums)-1
        length = len(nums)
        while start <= end:
            mid = (start+end)>>1
            if nums[mid]!=mid:
                if mid==0 or nums[mid-1]==mid-1: return mid
                end = mid-1
            else: start = mid+1
            if start==length: return length
