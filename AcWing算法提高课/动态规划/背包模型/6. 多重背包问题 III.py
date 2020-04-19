#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V (0<N≤1000, 0<V≤20000)，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N≤1000
0<V≤20000
0<vi,wi,si≤20000
提示
本题考查多重背包的单调队列优化方法。

输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
'''
# 多重背包问题：物品有有限个
# 状态表示：①集合：dp[i][j]表示所有只从前i个物品中找，且总体积不超过j的选法的集合 ②属性：max
# 状态计算：第i个物品选多少个，0,1,2，... ,si个
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-vi]+w, dp[i-1][j-2vi]+2w, ..., dp[i-1][j-s*vi]+s*w)
# 优化：dp[i][j-v] = max(dp[i-1][j-v], dp[i-1][j-2vi]+w, dp[i-1][j-3vi]+2w, ... , dp[i-1][j-s*vi]+(s-1)*w, dp[i-1][j-(s+1)*vi]+s*w)

# 又超时了，化简的写法没做出来
from typing import List
class Solution:
    def bagge(self, stuffs: List[List[int]], space: int):
        dp = [[0 for _ in range(space+1)] for _ in range(len(stuffs)+1)]
        dp[0][0] = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j >= stuffs[i-1][0]*stuffs[i-1][2]:
                    v = stuffs[i-1][0]
                    w = stuffs[i-1][1]
                    num = stuffs[i-1][2]
                    # 即空间完全能放得下
                    for k in range(num+1):
                        dp[i][j] = max(dp[i][j], dp[i-1][j-k*v]+k*w)

                elif j >= stuffs[i-1][0]:
                    # 空间不能完全放得下
                    # 但至少能放一个
                    v = stuffs[i - 1][0]
                    w = stuffs[i - 1][1]
                    dp[i][j] = max(dp[i-1][j], dp[i][j-v]+w)
                else:
                    # 一个都放不下
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    num, space = list(map(int, input().split()))
    stuffs = []
    for i in range(num):
        stuffs.append(list(map(int, input().split())))
    res = solution.bagge(stuffs, space)
    print(res)