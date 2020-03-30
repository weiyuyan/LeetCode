#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/26
'''
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
8
'''
# 暴力做法：二维动态规划
# f[i][j]：表示只看前i个物品，总体积是j的情况下，总价值最大是多少
# result = max(f[n][0~v])
# 这个问题首先有2^n种方案（每个物品有选与不选两种状态）

from typing import List
class Solution:
    def bag(self, bags: List[List[int]], v: int):
        n = len(bags)
        v = v
        dp = [[0 for i in range(v+1)] for j in range(n+1)]
        # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求

        for i in range(1, n+1):
            for j in range(1, v+1):
                dp[i][j] = dp[i-1][j]

                if j>=bags[i-1][0]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-bags[i-1][0]]+bags[i-1][1])

        return dp[-1][-1]


# 优化：一维dp
    def bag(self, bags: List[List[int]], v: int):
        n = len(bags)
        v = v
        dp = [0 for i in range(v+1)]
        # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求

        for i in range(n):
            for j in range(v, -1, -1):
                if j>=bags[i][0]:
                    dp[j] = max(dp[j], dp[j-bags[i][0]]+bags[i][1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    n, v = map(int, input().split())
    bags = []
    for i in range(n):
        bags.append([int(i) for i in input().split()])
    res = solution.bag(bags, v)

    print(res)