#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
给定两个正整数，计算它们的和。

输入格式
共两行，每行包含一个整数。

输出格式
共一行，包含所求的和。

数据范围
1≤整数长度≤100000
输入样例：
12
23
输出样例：
35
'''
class Solution:
    def add(self, m, n):
        print(m+n)

if __name__ == '__main__':
    solution = Solution()
    a = int(input())
    b = int(input())
    solution.add(a, b)