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
        res = []
        if not nums or n<4:
            return []
        nums.sort()
        for i in range(n):
            tmp_res = self.threeSum(nums[i:], target=nums[i])
            for j in tmp_res:
                j.append(nums[i])
                res.append(j)
        return res

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if not nums or n<3:
            return []
        nums.sort()
        for i in range(n):
            if (nums[i]>0):
                return res
            if (i>0 and nums[i]==nums[i-1]):    # 避免重复数字组合出现
                continue
            L = i+1
            R = n-1
            while(L<R):
                if (nums[i]+nums[L]+nums[R] == target):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L=L+1
                    R=R-1
                elif (nums[i]+nums[L]+nums[R] > target):
                    R -= 1
                else:
                    L += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(res)
