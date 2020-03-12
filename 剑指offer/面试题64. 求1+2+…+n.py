#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/6
'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

限制：

1 <= n <= 10000
'''
# 方法一：（递归+短路+叠加）
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n+self.sumNums(n-1))

# 方法二：定义乘法运算
class Solution:
    def sumNums(self, n: int) -> int:
        return self.multi(n, n+1) >> 1
    def multi(self, a, b):
        return b and ((b & 1 and a) + self.multi(a<<1, b>>1))

solution = Solution()
res = solution.sumNums(3)
print(res)
