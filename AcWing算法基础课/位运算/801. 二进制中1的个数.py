#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/14
'''
给定一个长度为n的数列，请你求出数列中每个数的二进制表示中1的个数。

输入格式
第一行包含整数n。

第二行包含n个整数，表示整个数列。

输出格式
共一行，包含n个整数，其中的第 i 个数表示数列中的第 i 个数的二进制表示中1的个数。

数据范围
1≤n≤100000,
0≤数列中元素的值≤109
输入样例：
5
1 2 3 4 5
输出样例：
1 1 2 1 2
'''
if __name__ == '__main__':
    n = int(input())
    alist = list(map(int, input().split()))
    for i in alist:
        print(bin(i).count('1'), end=' ')

    # 看n的第k位数字是多少：(n>>k)&1
    # x&-x，可以得到x最后一个'1'是多少
    # why?
    # -x = ~x+1
    # 假设x = b10010000，那么
    # ~x = b01101111，那么
    # ~x+1 = b01110000
    # x&(~x+1) = 00010000 = 10000，也就是x最后一个1所在的位置
    # def lowbit(x):
    #    return x & -x
    # res = 0
    # while(x):
    #    x -= lowbit(x); res+=1