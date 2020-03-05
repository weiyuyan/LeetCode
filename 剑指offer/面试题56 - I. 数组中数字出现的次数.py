#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

限制：

2 <= nums <= 10000
'''
from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        if not nums: return None
        if len(nums) == 1: return [nums[0]]
        res = 0
        for num in nums:
            res ^= num
        pos = -1
        while bin(res)[pos] != '1':
            pos -= 1

        pos_0 = []
        pos_1 = []
        for num in nums:
            if len(bin(num)) < 2-pos or bin(num)[pos] == '0': pos_0.append(num)
            else: pos_1.append(num)

        return [self.singleNumber(pos_0), self.singleNumber(pos_1)]

    # 只出现一次的数字
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

solution = Solution()
nums = [6,2,3,3]
res = solution.singleNumbers(nums)
print(res)