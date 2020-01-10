#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/10
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''
# 哈希表法
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target-num) is not None:
                return [i, hashmap.get(target-num)]
            hashmap[num] = i
if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)