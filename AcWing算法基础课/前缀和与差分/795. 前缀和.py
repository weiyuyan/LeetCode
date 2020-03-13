#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
输入一个长度为n的整数序列。

接下来再输入m个询问，每个询问输入一对l, r。

对于每个询问，输出原序列中从第l个数到第r个数的和。

输入格式
第一行包含两个整数n和m。

第二行包含n个整数，表示整数数列。

接下来m行，每行包含两个整数l和r，表示一个询问的区间范围。

输出格式
共m行，每行输出一个询问的结果。

数据范围
1≤l≤r≤n,
1≤n,m≤100000,
−1000≤数列中元素的值≤1000
输入样例：
5 3
2 1 3 6 4
1 2
1 3
2 4
输出样例：
3
6
10
'''
# 前缀和的话，更好的处理方式是下标从1开始计数，下标0可以设为0，这样的话将来减起来的话方便，不需要额外判断边界
# Si = a1+a2+..+ai
# S0 = 0
# 求sum(a[l]~a[r])：只需S[r]-S[l-1]
class Solution:
    def __init__(self, alist):
        self.alist = alist
        self.s = [0]
        for i in range(len(self.alist)):
            self.s.append(self.s[i]+self.alist[i])

    def prefixSum(self, l, r):
        return self.s[r] - self.s[l-1]

if __name__ == '__main__':
    res = []
    n, m = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    solution = Solution(alist)
    for i in range(m):
        l, r = list(map(int, input().split()))
        res.append(solution.prefixSum(l, r))
    for j in res:
        print(j)