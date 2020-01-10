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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            tmp_result = self.twoSum(nums[i:], -nums[i])
            result.append(tmp_result)
            result = list(filter(None, result))
        print(result)

if __name__ == '__main__':
    solution = Solution()
    solution.threeSum([-1,0,1,2,-1,-4])
    ## 未完待续