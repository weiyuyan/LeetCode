#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/11
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # 如果小于四个数，那就别整了
        if n < 4:
            return []

        nums.sort()
        # 如果前四个和就大于target，那就凉凉，别整了
        if sum(nums[:4]) > target:
            return []

        result = []
        for one in range(n-2):
            for two in range(one+1, n-1):
                Left = two+1
                Right = n-1
                while(Left != Right):
                    sum_num = nums[one] + nums[two] + nums[Left] + nums[Right]
                    if sum_num == target and [nums[one], nums[two], nums[Left], nums[Right]] not in result:
                        result.append([nums[one], nums[two], nums[Left], nums[Right]])
                    if sum_num <= target:
                        Left += 1
                    else:
                        Right -= 1
        return result

if __name__ == '__main__':
    solution = Solution()
    res = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(res)
