#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
【题目】
给定两个32位整数a和b，可正、可负、可0。不能使用算术运算符，分别实现a和b的加减乘除运算。

【要求】
如果给定的a和b执行加减乘除的某些结果本来就会导致数据的溢出，那么你实现的函数不必对那些结果负责。
'''
# 减法其实是用加法来实现的。在ALU中，当我求a-b，其实是求[a-b]补。因为有[a-b]补=[a]补 - [b]补= [a]补+[-b]补。
# 所以我就要先求出-b。求一个数的负的操作是将其连符号位一起取反然后加1。
#    于是有办法做减法了：先把减数求负，然后做加法。

# 这里a,b均为整数
def add(a, b):
    if b == 0:
        return a
    # a, b互为相反数
    if a == -b:
        return 0
    flag = False
    # 异号数之和大于0，转换加数符号
    if a < 0 and b > 0:
        if -a < b:
            flag = True
            a = -a
            b = -b
    if a > 0 and b < 0:
        if a > -b:
            flag = True
            a = -a
            b = -b
    while b != 0:
        res = a ^ b
        b = (a & b) << 1
        a = res
    if flag is True:
        res = -res
    return res

def sub(a, b):
    return add(a, -b)

print(sub(3, -2))
# print(-1>>31)