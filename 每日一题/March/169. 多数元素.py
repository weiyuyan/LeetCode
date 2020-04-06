#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
from typing import List
class Solution:
    # 哈希表
    # 时间复杂度：o(n)
    # 空间复杂度: o(n)
    def majorityElement(self, nums: List[int]) -> int:
        a_dict = {}
        for i in nums:
            if i in a_dict:
                a_dict[i]+=1
                if a_dict[i] > len(nums) // 2:
                    return i
            else:
                a_dict[i]=1

    # 哈希表简化版
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 排序法
    # 时间复杂度：o(nlogn)
    # 空间复杂度: o(n)，如果采用堆排序，o(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # 投票法（这个真的灵性）
    # 这个时间复杂度和空间复杂度为o(n)和o(1)，超级棒
    def majorityElement(self, nums: List[int]) -> int:
        candidate= None
        count = 0
        for i in nums:
           if count == 0:
               candidate = i
           count += 1 if candidate==i else -1
        return candidate

solution = Solution()
nums = [2,2,1,1,1,2,2]
res = solution.majorityElement(nums)
print(res)