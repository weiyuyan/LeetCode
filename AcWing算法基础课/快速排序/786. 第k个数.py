#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/11
'''
给定一个长度为n的整数数列，以及一个整数k，请用快速选择算法求出数列的第k小的数是多少。

输入格式
第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在1~109范围内），表示整数数列。

输出格式
输出一个整数，表示数列的第k小数。

数据范围
1≤n≤100000,
1≤k≤n
输入样例：
5 3
2 4 1 5 3
输出样例：
3
'''
# 暴力算法：不管三七二十一先快排，然后求第k个数
from typing import List
class Solution:
    def k_number(self, alist: List[int], k: int):
        self.quick_sort(alist, 0, len(alist)-1)
        print(alist[k-1])


    def quick_sort(self, q, l, r):
        if l>=r: return
        x = q[(l+r)//2]
        i, j = l-1, r+1
        while(i<j):
            while True:
                i+=1
                if q[i]>=x: break
            while True:
                j-=1
                if q[j]<=x: break
            if i<j:
                q[i], q[j] = q[j], q[i]
        self.quick_sort(q, l, j)
        self.quick_sort(q, j+1, r)

# 快速选择算法

class Solution2:
    def k_number(self, alist: List[int], k: int):
        self.k = k
        self.quick_sort(alist, 0, len(alist)-1)
        print(alist[k-1])


    def quick_sort(self, q, l, r):
        if l>=r: return
        x = q[(l+r)//2]
        i, j = l-1, r+1
        while(i<j):
            while True:
                i+=1
                if q[i]>=x: break
            while True:
                j-=1
                if q[j]<=x: break
            if i<j:
                q[i], q[j] = q[j], q[i]

        if j-l+1>=self.k:
            self.quick_sort(q, l, j)
        else:
            self.k -= (j-l+1)
            self.quick_sort(q, j+1, r)

if __name__ == '__main__':
    solution = Solution2()
    nums, k = map(int, input().split())
    alist = list(map(int, input().split()))
    solution.k_number(alist, k)

