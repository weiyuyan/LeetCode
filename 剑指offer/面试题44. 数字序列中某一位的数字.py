#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/25
'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 
限制：

0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
'''
# class Solution:
#     def findNthDigit(self, n: int) -> int:
#         if n<0: return False
#         if n==0: return 0
#
#         digits = 1
#         while digits:
#             num = self.countOfIntegers(digits)
#             if n-num <= 0:
#                 break
#             n = n-num
#             digits += 1
#
#         if n==0:
#
#         a, b = divmod(n, digits-1)
#         if b==0:
#             res = int(str(10**n + a)[-1])
#         else:
#             res = int(str(10**n + a+1)[b-1])
#         return res
#
#     def countOfIntegers(self, digits: int) -> int:
#         if digits == 1: return 10
#         else:
#             return len(str(digits)) * 9
pass


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 首先判断target是几位数，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
        if idx == 0:
            idx = digits
        number = 1
        for i in range(1, digits):
            number *= 10
        if idx == digits:
            number += n // digits - 1
        else:
            number += n // digits
        # 找到target中对应的数字
        for i in range(idx, digits):
            number //= 10
        return number % 10

solution = Solution()
res = solution.findNthDigit(10)
print(res)