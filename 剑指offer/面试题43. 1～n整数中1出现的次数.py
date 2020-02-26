#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/25
'''
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6
 
限制：

1 <= n < 2^31
'''
# 第一个方法超时了，观察数据规律，可以想出另一个方法
# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         result = 0
#         for i in range(n+1):
#             result += str(i).count('1')
#         return result
pass

# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         result = 0
#         # 将n变成str形式
#         str_n = str(n)
#         while str_n:
#             if len(str_n) == 1: result += 1; break
#             uppest = str_n[0]
#             result += 10 ** (len(str_n) - 1) * (int(uppest) - 1)
#             result += int(str_n[1:]) + 1
#             str_n = '9' * (len(str_n)-1)
#         return result

pass

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 1  # 个位开始
        while n // i != 0:
            high = n//(i*10) # 高位数
            current = (n//i) % 10  # 第i位数
            low = n - (n//i) * i  # 低位数
            if current == 0:
                res += high * i
            elif current == 1:
                res += high * i + low + 1
            else:
                res += (high+1) * i
            i *= 10
        return res


solution = Solution()
res = solution.countDigitOne(9999999)
print(res)