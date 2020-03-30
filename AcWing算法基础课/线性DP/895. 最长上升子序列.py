#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/28
'''
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。

第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000，
−10^9≤数列中的数≤10^9
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4
'''
# 状态表示（化零为整）（维数的考虑原则是从小到大）①集合：这里我们发现一维就行f[i]表示以第i个数结尾的上升子序列的集合，例如：
# 对于f[5]来说，是8，有以下几个子序列：（8）、（1，8）、（2，8）、（1，2，8）、（3，8）
# ②属性：（min、max、count）这里是集合里每一个上升子序列的长度的最大值
# 状态计算（化整为零/集合划分）
# 将集合划分成k份（从0到i-1）（n==k），表示f[i]前的第k个数
# f[i] = max(f[j]+1), j=0,1,2...,i-1

from typing import List
class Solution:
    def max_substring(self, string: List[int]):
        n = len(string)
        dp = [float('-inf') for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = 1
            for j in range(1, i):
                if string[i-1] > string[j-1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    n = int(input())
    string = list(map(int, input().split()))
    solution = Solution()
    res = solution.max_substring(string)
    print(res)
