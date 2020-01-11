#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/10
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
from typing import List
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
                if (nums[i]+nums[L]+nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L=L+1
                    R=R-1
                elif (nums[i]+nums[L]+nums[R] > 0):
                    R -= 1
                else:
                    L += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.threeSum([-1,0,1,2,-1,-4])

