#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        return (a^b) + ((a&b)<<1)

# 先前的方法还是用到了加法
# 方法二：
# 需要处理一下py的无限长整型.
class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a&b
            sum = a^b
            a = sum
            b = ((carry<<1) & 0xFFFFFFFF)
        return a if a<0x80000000 else ~(a^0xFFFFFFFF)


solution = Solution()
res = solution.add(-2, 1)

# print(res)
print((4294967295^0XFFFFFFFF) & 0XFFFFFFFF)