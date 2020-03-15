#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/15
'''
给定一个长度为N的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出-1。

输入格式
第一行包含整数N，表示数列长度。

第二行包含N个整数，表示整数数列。

输出格式
共一行，包含N个整数，其中第i个数表示第i个数的左边第一个比它小的数，如果不存在则输出-1。

数据范围
1≤N≤105
1≤数列中元素≤109
输入样例：
5
3 4 2 7 5
输出样例：
-1 3 -1 2 2
'''
N = int(input())
sequence = list(map(int, input().split()))

ans = []
stack = [-1]
for i in range(N):
    if sequence[i] > stack[-1]:
        ans.append(stack[-1])
        stack.append(sequence[i])
    else:
        while sequence[i]<=stack[-1] and len(stack)>0:
            del stack[-1]
        ans.append(stack[-1])
        stack.append(sequence[i])

print(' '.join(list(map(str, ans))))