#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/23
'''
给你一个整数 num，请你找出同时满足下面全部要求的两个整数：

两数乘积等于  num + 1 或 num + 2
以绝对差进行度量，两数大小最接近
你可以按任意顺序返回这两个整数。

示例 1：

输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。
示例 2：

输入：num = 123
输出：[5,25]
示例 3：

输入：num = 999
输出：[40,25]


提示：

1 <= num <= 10^9
'''
from typing import List
import math
# class Solution:
#     def closestDivisors(self, num: int) -> List[int]:
#         res1 = self.findNearestFactor(num+1)
#         if res1[0]-res1[1] == 0: return res1
#
#         res2 = self.findNearestFactor(num+2)
#
#         res_1 = abs(res1[0]-res1[1])
#         res_2 = abs(res2[0]-res2[1])
#         return res1 if res_1<=res_2 else res2
#
#     def findNearestFactor(self, num: int) -> List[int]:
#         # 找到差最小的因数
#         def crack(integer):
#             start = int(math.sqrt(integer))
#             # factor = integer / start
#             # while not is_integer(factor):
#             #     start += 1
#             #     factor = integer / start
#             # return [int(factor), start]
#
#             factor = integer // start
#             while not is_ok(start, factor, integer):
#                 start += 1
#                 factor = integer // start
#             return [int(factor), start]
#
#
#
#         def is_integer(number):
#             if int(number) == number:
#                 return True
#             else:
#                 return False
#         def is_ok(a, b, target):
#             return True if a*b == target else False
#
#         return crack(num)


# 很神奇，从sqrt(num)位置算到num和从1算到sqrt(num)花费的时间差太多了，我也暂时没整明白，
# 可能在python里除以小数和除以大数计算量是不一样的
# 2020年2月23日17:18:54 他妈的我懂了！和除数、被除数没关系，因为从sqrt(x) 到 x 的数字比 1 到 x 的数字多得多
# 比如900，sqrt(900) == 30，从1到30运算比从30到900运算数量少得多！！！
# 好神奇！今天才意识到
import time

class Solution1:
    def closestDivisors(self, num: int) -> List[int]:
        low1, high1 = self.cloestFactor(num + 1)
        low2, high2 = self.cloestFactor(num + 2)
        return [low1, high1] if abs(low1-high1) < abs(low2-high2) else [low2, high2]

    def cloestFactor(self, num):
        sqrt = int(num ** 0.5)
        high = sqrt
        while high > 1:
            if num % high == 0:
                low = num // high
                return [low, high]
            high += 1
        return [1, num]

class Solution2:
    def closestDivisors(self, num: int) -> List[int]:
        low1, high1 = self.cloestFactor(num + 1)
        low2, high2 = self.cloestFactor(num + 2)
        return [low1, high1] if abs(low1-high1) < abs(low2-high2) else [low2, high2]

    def cloestFactor(self, num):
        sqrt = int(num ** 0.5)
        high = sqrt
        while high > 1:
            if num % high == 0:
                low = num // high
                return [low, high]
            high -= 1
        return [1, num]

solution = Solution1()
a1 = time.time()
# res = solution.closestDivisors(688427155)
a2 = time.time()

solution = Solution2()
b1 = time.time()
res = solution.closestDivisors(6884271555)
b2 = time.time()
print(a1-a2)
print(b1-b2)