#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/27
'''
有 N 组物品和一个容量是 V 的背包。

每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是 vij，价值是 wij，其中 i 是组号，j 是组内编号。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。

输出最大价值。

输入格式
第一行有两个整数 N，V，用空格隔开，分别表示物品组数和背包容量。

接下来有 N 组数据：

每组数据第一行有一个整数 Si，表示第 i 个物品组的物品数量；
每组数据接下来有 Si 行，每行有两个整数 vij,wij，用空格隔开，分别表示第 i 个物品组的第 j 个物品的体积和价值；
输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<Si≤100
0<vij,wij≤100
输入样例
3 5
2
1 2
2 4
1
3 4
1
4 5
输出样例：
8
'''
# 一、状态表示（集合）（化零为整）①集合：f[i][j]表示只从前i组物品中选，且总体积不大于j的所有选法  ②属性：max
# 二、状态计算：（完全背包问题：第i个物品选几个）（分组背包问题：第i组物品选哪个）本题：第i组物品选哪个（或者不选）
# 有以下几种情况：不选、只选第一个、只选第二个。。。只选第n个
# f[i][j] = max(f[i-1][j], f[i-1][j-v[i,1]]+w[i,1], ... , f[i-1][j-v[i,k]]+w[i,k])
# 这里v[i,k]表示第i组物品中的第k的物品的体积，w[i,k]表示第i组物品中的第k的物品的价值
from typing import List
class Solution:
    def bag(self, n: int, m: int, s: List[int], v: List[List[int]], w: List[List[int]]):
        # n存放组的个数，m存放背包总容量
        # s存放第i组的元素个数
        # v存放第i组第j个元素的体积，w存放第i组第j个元素的价值
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                for k in range(s[i]):
                    if j>=v[i][k]:
                        dp[j] = max(dp[j], dp[j - v[i][k]] + w[i][k])
        return dp[-1][-1]

# 由于只用到了第i-1列，所以可以仿照0-1背包问题的套路逆向枚举体积
    def bag(self, n: int, m: int, s: List[int], v: List[List[int]], w: List[List[int]]):
        # n存放组的个数，m存放背包总容量
        # s存放第i组的元素个数
        # v存放第i组第j个元素的体积，w存放第i组第j个元素的价值
        dp = [0 for _ in range(m+1)]

        for i in range(1, n+1):
            for j in range(m, -1, -1):
                # dp[i][j] = dp[i-1][j]
                for k in range(s[i]):
                    if j>=v[i][k]:
                        # dp[i][j] = max(dp[i][j], dp[i-1][j-v[i][k]]+w[i][k])
                        dp[j] = max(dp[j], dp[j - v[i][k]] + w[i][k])
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    n, m = map(int, input().split())    # n存放组的个数，m存放背包总容量
    s = [0 for _ in range(n+1)]
    v = [[0 for _ in range(n + 1)] for _ in range(n + 1)]   # v存放第i组第j个元素的体积
    w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]   # w存放第i组第j个元素的价值
    for i in range(1, n+1):
        s[i] = int(input())  # s存放第i组的元素个数
        for j in range(s[i]):
            v[i][j], w[i][j] = list(map(int, input().split()))

    res = solution.bag(n, m, s, v, w)

    print(res)