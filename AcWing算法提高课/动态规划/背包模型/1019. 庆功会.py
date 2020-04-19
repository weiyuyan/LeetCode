#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/17
'''
为了庆贺班级在校运动会上取得全校第一名成绩，班主任决定开一场庆功会，为此拨款购买奖品犒劳运动员。

期望拨款金额能购买最大价值的奖品，可以补充他们的精力和体力。

输入格式
第一行二个数n，m，其中n代表希望购买的奖品的种数，m表示拨款金额。

接下来n行，每行3个数，v、w、s，分别表示第I种奖品的价格、价值（价格与价值是不同的概念）和能购买的最大数量（买0件到s件均可）。

输出格式
一行：一个数，表示此次购买能获得的最大的价值（注意！不是价格）。

数据范围
n≤500,m≤6000,
v≤100,w≤1000,s≤10
输入样例：
5 1000
80 20 4
40 50 9
30 50 7
40 30 6
20 20 1
输出样例：
1040
'''
# 本题同6、多重背包问题III
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