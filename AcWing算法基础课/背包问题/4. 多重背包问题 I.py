#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/27
'''
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<vi,wi,si≤100
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
'''
# 一、状态表示：①集合（化零为整）f[i][j]：所有只从前i个物品中选，且总体积不超过j的选法  ②属性（min max count）max
# 二、状态计算：化整为零）分成0,1,2,3,4,...,s[i]表示选择了0个，1个，2个...s[i]个第i个物品的集合（因为最多只有s[i]个）
# 和完全背包相类似
# f[i][j] = max(f[i-1][j-vi*k] for k in range(s[i]+1))

# 暴力解法
from typing import List
class Solution:
    def bag(self, goods: List[List[int]], v: int):
        n = len(goods)
        v = v
        dp = [[0 for i in range(v+1)]for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, v+1):
                # 体积：
                vi = goods[i - 1][0]
                # 价值：
                wi = goods[i - 1][1]
                # 数量
                si = goods[i - 1][2]
                for k in range(si+1):
                    if k*vi>j:
                        break
                    dp[i][j] = max(dp[i][j], dp[i-1][j-k*vi] + wi*k)

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    n, v = map(int, input().split())
    bags = []
    for i in range(n):
        bags.append([int(i) for i in input().split()])
    res = solution.bag(bags, v)

    print(res)