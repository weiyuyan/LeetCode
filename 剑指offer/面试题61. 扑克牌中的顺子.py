#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/6
'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True

示例 2:

输入: [0,0,1,2,5]
输出: True

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
'''
from typing import List
# class Solution:
#     def isStraight(self, nums: List[int]) -> bool:
#         if len(set(nums)) < 5: return False
#         max = max(nums)
#         min = min(nums)
#         if min != 0:
#             if max - min == 4: return True
#             else: return False
#
#
#         if min == 0:    # 大小王
#             if nums.count(0) > 2: return False
#             if max - min <= 4: return True

# 排序后处理
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        gost=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==0:
                gost+=1
                continue
            if nums[i+1]==nums[i]:
                return False
            if (nums[i+1]-nums[i])!=1:
                gost-=(nums[i+1]-nums[i]-1)
        return gost>=0

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        gost = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==0:
                gost+=1
                continue
            if nums[i+1]==nums[i]: return False
            if (nums[i+1]-nums[i-1]) != 1:
                gost -= (nums[i+1]-nums[i]-1)
        return gost >= 0

solution = Solution()
nums = [4,7,5,9,2]
res = solution.isStraight(nums)
print(res)










