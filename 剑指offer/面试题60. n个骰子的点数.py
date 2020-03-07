#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/6
'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
'''
from typing import List
# 递归方法
# 超时了，不可取
class Solution:
    def twoSum(self, n: int) -> List[float]:
        self.n = n
        res = []
        for i in range(n, n*6+1):
            res.append(self.back_track(0, i, 1))
        return res

    def back_track(self, depth: int, res: int, prob: float):
        if depth == self.n and res == 0: return prob
        if depth > self.n or res < 0: return 0
        return self.back_track(depth+1, res-1, prob*1/6) + self.back_track(depth+1, res-2, prob*1/6)\
        + self.back_track(depth+1, res-3, prob*1/6) + self.back_track(depth+1, res-4, prob*1/6)\
        + self.back_track(depth+1, res-5, prob*1/6) + self.back_track(depth+1, res-6, prob*1/6)


class Solution:
    def twoSum(self, n: int) -> List[float]:
        res = []
        # 要求每一个出现的点数出现的总数，开辟一个二维数组dp dp[n][j]表示n个骰子投掷后，总数为j的出现次数
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        # (1) 初始状态
        for j in range(1, 7):  # 初始化第一行
            dp[1][j] = 1
        for i in range(2, n + 1):  # 每1行
            for j in range(i, 6 * i + 1):  # 每一列，要计算的每一列的数量是不一样的，为6i,即i枚骰子，有5i种结果，需要填充的数量为5i
                for z in range(1, 7):  # 是转移方程dp[i][j]=dp[i-1][j-1]+dp[i-1][j-2]+...+dp[i-1][j-6]
                    if j - z >= 1 and dp[i - 1][j - z] > 0:
                        dp[i][j] += dp[i - 1][j - z]
        for i in range(6 * n + 1):
            if dp[n][i] / 6 ** n > 0:
                res.append(dp[n][i] / (6 ** n))
        return res

class Solution:
    def twoSum(self, n):
        res = []
        dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]
        for j in range(1, 7):
            dp[1][j] = 1
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for z in range(1, 7):
                    if j-z >= 1 and dp[i-1][j-z]>0:
                        dp[i][j] += dp[i-1][j-z]
        for i in range(6*n+1):
            if dp[n][i] / (6**n) > 0:
                res.append(dp[n][i] / (6**n))
        return res


solution = Solution()
res = solution.twoSum(2)
print(res)