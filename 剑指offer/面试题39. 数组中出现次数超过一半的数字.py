#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/21
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 
限制：

1 <= 数组长度 <= 50000

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
'''
from typing import List
import random

# 方法一：使用Partition（随机快速排序）法

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         length = len(nums)
#         if not self.CheckInvalidArray(nums, length): return 0
#
#         middle = length >> 1
#         start = 0
#         end = length - 1
#         index = self.Partition(nums, length, start, end)
#
#         while index != middle:
#             if index > middle:
#                 end = index - 1
#                 index = self.Partition(nums, length, start, end)
#             else:
#                 start = index + 1
#                 index = self.Partition(nums, length, start, end)
#
#         result = nums[middle]
#         if not self.CheckMoreThanHalf(nums, length, result): result = 0
#         return result
#
#     def Partition(self, data: List[int], length: int, start: int,  end: int):
#         if not data or length<=0 or start<0 or end>=length: return False
#
#         index = random.randint(start, end)
#         data[index], data[end] = data[end], data[index]
#         small = start - 1
#         for index in range(start, end):
#             if data[index] < data[end]:
#                 small += 1
#                 if small != index:
#                     data[index], data[small] = data[small], data[index]
#
#         small += 1
#         data[small], data[end] = data[end], data[small]
#         return small
#
#     def CheckInvalidArray(self, numbers, length):
#         '''
#         检测是否符合规范
#         :param numbers:
#         :param length:
#         :return:
#         '''
        # return True
    #
    # def CheckMoreThanHalf(self, nums, length, number):
    #     '''
    #     检查超过一半数字的是否存在
    #     :param nums:
    #     :param length:
    #     :param number:
    #     :return:
    #     '''
        # return True
pass

# 方法二：使用哈希表
# 时间复杂度o(n)，空间复杂度o(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hash_dict = {}
#         for num in nums:
#             if num in hash_dict:
#                 hash_dict[num] += 1
#             else:
#                 hash_dict[num] = 1
#         return max(hash_dict, key=lambda x: hash_dict[x])
#

# 方法三：使用临时计数器
# 时间复杂度o(n)，空间复杂度o(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return 0
        result = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if nums[i] == result:
                times += 1
            else:
                times -= 1
            if times == 0:
                times = 1
                result = nums[i]

        return result



solution = Solution()
res = solution.majorityElement([1,1,1,2,3,3,3,3,3,3,2])
print(res)