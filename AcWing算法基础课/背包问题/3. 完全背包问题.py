#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/27
'''
有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。

第 i 种物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。

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
10
'''
# 首先，对于完全背包问题，把01背包问题反过来就行
from typing import List
class Solution:

    def bag(self, bags: List[List[int]], v: int):
        n = len(bags)
        v = v
        dp = [0 for i in range(v+1)]
        # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求

        for i in range(n):
            for j in range(v+1):
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

# 一、状态表示：①集合（化零为整）f(i, j)，所有从前i个物品中选出总体积不超过j的方案的集合  ②属性（min max count）max
# 二、状态计算（化整为零）分成0,1,2,3,4,...,k表示选择了0个，1个，2个...k个第i个物品的集合
# 对于为0的状态，由于不选第i个，所有相当于f(i-1, j)
# 对于为k的状态，表示要选k个i元素，所以在之前的i-1方案中，总体积不能超过j-k(vi)
# 故对于为k的状态，表示为f(i-1, j-k(vi))+k(wi)
# 以此类推
# f(i, j) = max(f(i-1, j), f(i-1, j-1(vi))+1(wi), f(i-1, j-2(vi))+2(wi),...,f(i-1, j-k(vi))+k(wi))
# 优化：如果把j换成j-vi，f(i, j-vi) = max(f(i-1, j-1(vi)), f(i-1, j-2(vi))+1(wi), f(i-1, j-3(vi))+2(wi),...,f(i-1, j-(k+1)(vi))+k(wi))
# 所以f(i, j) = max(f(i-1, j), f(i, j-1)+wi)

# 综合一下，对比0-1背包和完全背包：
# 0-1背包     f[i][j] = max(f[i-1][j], f[i-1][j-v]+w)
# 完全背包    f[i][j] = max(f[i-1][j], f[i][j-v]+w)

# 朴素做法
n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])
dp = [0 for i in range(v+1)]
for i in range(n):
    for j in range(v,-1,-1): # 从后往前
        k = j//goods[i][0]
        dp[j] = max([dp[j- x* goods[i][0]] + x * goods[i][1] for x in range(k+1)])


print(dp[-1])


# 一维动态规划（优化）
n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])
dp = [0 for i in range(v+1)]
for i in range(n):
    for j in range(v+1): # 从前往后
        if j >= goods[i][0]:
            dp[j] = max(dp[j], dp[j-goods[i][0]]+goods[i][1])


print(dp[-1])
