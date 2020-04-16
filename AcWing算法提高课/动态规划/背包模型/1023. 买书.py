#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
小明手里有n元钱全部用来买书，书的价格为10元，20元，50元，100元。

问小明有多少种买书方案？（每种书可购买多本）

输入格式
一个整数 n，代表总共钱数。

输出格式
一个整数，代表选择方案种数。

数据范围
0≤n≤1000
输入样例1：
20
输出样例1：
2
输入样例2：
15
输出样例2：
0
输入样例3：
0
输出样例3：
1
'''
# 完全背包问题
# 状态表示：①集合：所有只从前i个物品中选，且总体积恰好是j的方案的集合  ②属性：count
# 状态计算：将状态分为k个，依次表示选0个i物品；选1个i物品。。。选k个i物品
# dp[i][j] = dp[i-1][j] + dp[i-1][j-v[i]] + dp[i-1][j-2v[i]] +...+ dp[i-1][j-k*v[i]]
# 简化：
# 将j 换成 j-v[i]，得到dp[i][j-v[i]] = dp[i][j-v[i]] + dp[i][j-2v[i]] +...+ dp[i-1][j-k*v[i]]，与上边的式子相抵消
# 所以dp[i][j] = dp[i-1][j] + dp[i][j-v[i]]


# 普通版
class Solution:
    def buy_books(self, money: int):
        books = [10, 20, 50, 100]
        dp = [[0 for _ in range(money+1)] for _ in range(len(books)+1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(money+1):
                if j >= books[i-1]:
                    for k in range(j//books[i-1] + 1):
                        dp[i][j] += dp[i-1][j-k*books[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# 优化版
class Solution:
    def buy_books(self, money: int):
        books = [10, 20, 50, 100]
        dp = [[0 for _ in range(money+1)] for _ in range(len(books)+1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(money+1):
                if j >= books[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j - books[i - 1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    money = int(input())
    res = solution.buy_books(money)
    print(res)