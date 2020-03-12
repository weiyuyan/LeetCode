#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
【题目】
给定两个32位整数a和b，可正、可负、可0。不能使用算术运算符，分别实现a和b的加减乘除运算。

【要求】
如果给定的a和b执行加减乘除的某些结果本来就会导致数据的溢出，那么你实现的函数不必对那些结果负责。
'''
# 除法是乘法的逆运算
# 先转换为正数相除，再根据符号位判断结果的正负
# 负数的范围比正数的范围多1，因此转换为正数(abs)，存在溢出问题，java需要考虑整型溢出问题，python无需考虑。
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

def multi(a, b):
    sign_a = 0  # a的符号位
    sign_b = 0  # b的符号位
    # 提取符号位
    if a < 0:
        sign_a = 1
        a = -a
    if b < 0:
        sign_b = 1
        b = -b
    res = 0
    while b != 0:
        if b & 1 == 1:
            res = add(res, a)
        a = a << 1
        b = b >> 1
    if sign_a ^ sign_b == 1:
        res = -res
    return res

def div(a, b):
    # 除数为0
    if b == 0:
        raise ZeroDivisionError("除0错误")
    sign_a = 0  # a的符号位
    sign_b = 0  # b的符号位
    # 提取符号位
    if a < 0:
        sign_a = 1
        a = -a
    if b < 0:
        sign_b = 1
        b = -b
    res = 0
    fac = 1 << 31
    for i in range(0, 32):
        if a >= multi(b, fac):
            res = add(res, fac)
            a = sub(a, multi(b, fac))
        fac = fac >> 1
    if sign_a ^ sign_b == 1:
        res = -res
    return res

print(div(6, 9))