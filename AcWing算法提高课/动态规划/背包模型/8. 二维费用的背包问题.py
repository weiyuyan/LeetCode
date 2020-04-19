#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/17
'''
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。

每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V,M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。

接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N≤1000
0<V,M≤100
0<vi,mi≤100
0<wi≤1000
输入样例
4 5 6
1 2 3
2 4 4
3 4 5
4 5 6
输出样例：
8
'''
# 状态表示：dp[i][j][k] 表示所有只从前i个物品中选，总体积不超过j，总重量不超过k的选法的集合   属性：max
# 状态计算：分为两个状态：所有包含i的情况；所有不包含物品i的情况
# dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-v_i][k-wight_i]+wi)

from typing import List
class Solution:
    def bagge(self, stuffs: List[List[int]], space: int, max_weight: int):
        dp = [[[0 for _ in range(max_weight+1)] for _ in range(space+1)] for _ in range(len(stuffs)+1)]
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                for k in range(len(dp[0][0])):
                    if j >= stuffs[i-1][0] and k >= stuffs[i-1][1]:
                        v_i = stuffs[i-1][0]
                        weight_i = stuffs[i-1][1]
                        w_i = stuffs[i-1][2]
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-v_i][k-weight_i]+w_i)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[-1][-1][-1]

# 优化空间以及时间复杂度
class Solution:
    def bagge(self, stuffs: List[List[int]], space: int, max_weight: int):
        dp = [[0 for _ in range(max_weight+1)] for _ in range(space+1)]
        for i in range(len(stuffs)):
            v_i = stuffs[i][0]  # i的体积
            weight_i = stuffs[i][1] # i的重量
            w_i = stuffs[i][2]  # i的价值
            for j in range(space, v_i-1, -1):
                for k in range(max_weight, weight_i-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-v_i][k-weight_i]+w_i)

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    num, space, max_weight = list(map(int, input().split()))
    stuffs = []
    for i in range(num):
        stuffs.append(list(map(int, input().split())))
    res = solution.bagge(stuffs, space, max_weight)
    print(res)