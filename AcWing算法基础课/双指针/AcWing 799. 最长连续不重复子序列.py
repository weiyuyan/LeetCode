#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/14
'''
给定一个长度为n的整数序列，请找出最长的不包含重复数字的连续区间，输出它的长度。

输入格式
第一行包含整数n。

第二行包含n个整数（均在0~100000范围内），表示整数序列。

输出格式
共一行，包含一个整数，表示最长的不包含重复数字的连续子序列的长度。

数据范围
1≤n≤100000
输入样例：
5
1 2 2 3 5
输出样例：
3
'''
if __name__ == '__main__':
    n = int(input())
    alist = list(map(int, input().split()))
    adict = {}
    j = 0
    res = 0
    for i in range(len(alist)):
        if alist[i] in adict and adict[alist[i]]>=j:
            res = max(res, i-j)
            j = adict[alist[i]]+1
            adict[alist[i]] = i
        else:
            adict[alist[i]] = i
    print(res)

