#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
给你一个n种面值的货币系统，求组成面值为m的货币有多少种方案。

输入格式
第一行，包含两个整数n和m。

接下来n行，每行包含一个整数，表示一种货币的面值。

输出格式
共一行，包含一个整数，表示方案数。

数据范围
n≤15,m≤3000
输入样例：
3 10
1
2
5
输出样例：
10
'''
# 完全背包问题
from typing import List
class Solution:
    def money(self, money: List[int], target: int):
        dp = [[0 for _ in range(target+1)] for _ in range(len(money)+1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j >= money[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-money[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    n, target = list(map(int, input().split()))
    money = []
    for i in range(n):
        money.append(int(input()))

    res = solution.money(money, target)
    print(res)