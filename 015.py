#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/4

'''
Title: 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

# 固定一个值，找另外二个值它们和等于 0，
# 如何找另外两个值，用的是双指针！
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        #print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    tmp = [nums[i],nums[left],nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)