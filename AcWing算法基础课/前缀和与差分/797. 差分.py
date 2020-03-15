#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/14
'''
输入一个长度为n的整数序列。

接下来输入m个操作，每个操作包含三个整数l, r, c，表示将序列中[l, r]之间的每个数加上c。

请你输出进行完所有操作后的序列。

输入格式
第一行包含两个整数n和m。

第二行包含n个整数，表示整数序列。

接下来m行，每行包含三个整数l，r，c，表示一个操作。

输出格式
共一行，包含n个整数，表示最终序列。

数据范围
1≤n,m≤100000,
1≤l≤r≤n,
−1000≤c≤1000,
−1000≤整数序列中元素的值≤1000
输入样例：
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
输出样例：
3 4 5 3 4 2
'''
# 差分其实是前缀和的逆运算
# 输入的是a1, a2, a3,...,an这样一个数组
# 要构建一个b1, b2, b3,...,bn这样一个差分数组
# 只要把a数组当成b数组的前缀和就行，即a1 = b1, a2 = a1+b2, a3 = a2+b3
# 即b1 = a1, b2 = a2-a1, b3 = a3-a2...以此类推
# 这样的话，如果要在a[l,r]范围上+c，只需要
# 1、b[l]+c
# 2、b[r+1]-c即可

def insert(b, l, r, c):
    b[l] += c
    b[r+1] -= c

if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    b = [0]*(len(alist)+2)
    for i in range(1, len(alist)+1):
        insert(b, i, i, alist[i-1])

    for j in range(n):
        l, r, c = list(map(int, input().split()))
        insert(b, l, r, c)

    for k in range(1, len(b)-1):
        b[k] += b[k-1]
        print(b[k], end=' ')
