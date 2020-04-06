#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.quick_sort(self.nums, 0, len(self.nums)-1)
        return nums

    def quick_sort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        select = nums[(right+left)//2]
        i, j = left-1, right+1
        while(i<j):
            while True:
                i+=1
                if nums[i] >= select:
                    break
            while True:
                j-=1
                if nums[j] <= select:
                    break
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
        self.quick_sort(nums, left, j)
        self.quick_sort(nums, j+1, right)

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1]
    nums = solution.sortArray(nums)
    print(nums)


