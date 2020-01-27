#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/27
'''
给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。

数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。

请找出数组中任意一个重复的数字。

注意：如果某些数字不在 0∼n−1 的范围内，或数组中不包含重复数字，则返回 -1；

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
'''
# 方法一：先排序，后查找
# class Solution(object):
#     def duplicateInArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype int
#         """
#         res = -1
#         nums.sort()
#         len_nums = len(nums)
#         if len_nums < 2:
#             return res
#         if nums[0] < 0 or nums[-1] > len_nums-1:
#             return -1
#         for i in range(len_nums-1):
#             if nums[i] == nums[i+1]:
#                 return nums[i]
#         return -1

# 方法二：哈希表
# class Solution(object):
#     def duplicateInArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype int
#         """
#         res = -1
#         len_nums = len(nums)
#         hash_dict = {}
#         for i in range(len_nums):
#             if nums[i]>len_nums or nums[i]<0:
#                 return -1
#             if nums[i] in hash_dict.keys():
#                 res =  nums[i]
#             else:
#                 hash_dict[nums[i]] = i
#         return res

# 方法三：数组重排列
class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        res = -1
        flag = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i]<0 or nums[i]>=len_nums:
                return -1
            if nums[flag]<0 or nums[flag]>=len_nums:
                return -1
            if nums[flag] != flag:
                # 调换数组中元素顺序
                tmp = nums[nums[flag]]
                if tmp == nums[flag]:
                    res = tmp
                nums[nums[flag]] = nums[flag]
                nums[flag] = tmp
            else:
                flag += 1
        return res


solution = Solution()
res = solution.duplicateInArray([3, 1, -10, 1, 1, 4, 3, 10, 1, 1])
print(res)


