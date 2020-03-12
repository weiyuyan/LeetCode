#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
【题目】
给定两个32位整数a和b，可正、可负、可0。不能使用算术运算符，分别实现a和b的加减乘除运算。

【要求】
如果给定的a和b执行加减乘除的某些结果本来就会导致数据的溢出，那么你实现的函数不必对那些结果负责。
'''

# 位的异或运算跟求'和'的结果一致：
# 异或 1^1=0 1^0=1 0^0=0
# 求和 1+1=0 1+0=1 0+0=0

# 位的与运算跟求'进位‘的结果一致：
# 位与 1&1=1 1&0=0 0&0=0
# 进位 1+1=1 1+0=0 0+0=0

# 方法一
# 这里只适用于a,b均为正整数
def add(a, b):  # 递归
    if b==0:
        return a
    sum = a ^ b  # 异或得到两数之和
    carry = (a & b) << 1  # 与得到进位，左移后与sum相加
    return add(sum, carry)

# 方法二
# 这里只适用于a,b均为正整数
def add(a, b):  # 非递归
    # sum = 0
    # carry = 0
    while b:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a

# 方法三
# 这里适用于a,b均为整数，正负均可
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

print(add(-1, 8))