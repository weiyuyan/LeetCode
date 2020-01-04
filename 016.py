#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/4
'''
Title: 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

'''
# 思路：首先进行排序，时间复杂度o（nlogn），之后固定一个数，设置两个指针Left和Reight
from typing import List
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        optimal_value = math.fabs(nums[0] + nums[1] + nums[2] - target)  # 先随便找三个数，默认为最优值
        n = len(nums)
        sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(n):
            left = i+1
            right = n-1
            while(left < right):
                tmp_value = nums[left] + nums[right] + nums[i] - target
                if math.fabs(tmp_value) < optimal_value:
                    optimal_value = math.fabs(tmp_value)
                    sum = nums[i] + nums[left] + nums[right]
                elif tmp_value > 0:
                    right -= 1
                else:
                    left += 1
        return sum

if __name__ == '__main__':
    solution = Solution()
    optimal_value = solution.threeSumClosest([0, 2, 1, -3], 1)
    print(optimal_value)