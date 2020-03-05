#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 
限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31
'''
from typing import List
# 状态机，炒鸡巧妙？？？
# 初始：0 0
# 1个1：1 1
# 2个1：0 1
# 3个1：0 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones
        return ones

# 方法二：统计二进制数量
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        binary = [0]*32
        res = 0
        for num in nums:
            i = 1
            while bin(num)[-i] != 'b':
                binary[i-1] += 1 if bin(num)[-i]=='1' else 0
                i += 1

        for j in range(len(binary)):
            binary[j] %= 3

        for k in range(len(binary)):
            res += binary[k] * (2**k)
        return res



solution = Solution()
nums = [-2,-2, 1, 1, -3, 1, -3, -3, -4, -2]
res = solution.singleNumber(nums)
print(res)