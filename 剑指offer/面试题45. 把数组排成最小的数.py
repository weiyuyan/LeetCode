#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/26
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 
提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
'''
from typing import List
# 方法一
'''
class cmpSmaller(str):
    def __lt__(self, y):
        return self + y < y + self  # 字符串拼接比较(两两比较)
    # 按由小到大来排列

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        res=sorted(map(str, nums),key=cmpSmaller)
        smallest = ''.join(res)
        return smallest
'''
pass
# 方法二
import functools
class Solution:
    def compare(self, s1: str, s2: str) -> int:
        return 1 if s1+s2 > s2+s1 else -1

    def minNumber(self, numbers):
        if not numbers: return ''
        if len(numbers) == 1: return str(numbers[0])
        str_numbers = [str(n) for n in numbers]
        return ''.join(sorted(str_numbers, key=functools.cmp_to_key(self.compare)))

solution = Solution()
a = [3,30,34,5,9]
res = solution.minNumber(a)
print(res)
