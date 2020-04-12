#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/12
'''
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。

给你网格图的行数 n 。

请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。

示例 1：

输入：n = 1
输出：12
解释：总共有 12 种可行的方法：

示例 2：

输入：n = 2
输出：54
示例 3：

输入：n = 3
输出：246
示例 4：

输入：n = 7
输出：106494
示例 5：

输入：n = 5000
输出：30228214


提示：

n == grid.length
grid[i].length == 3
1 <= n <= 5000
'''
# 这一题，假设每一层有两种状态：ABA型和ABC型，记为dp[i][0]和dp[i][1]；属性：count
# 状态计算：对于dp[i][0]，下一层有4个备选：2种ABA和2种ABC型
# 对于dp[i][1]，下一层有5个备选：3种ABA和2种ABC
# ∴ dp[i][0] = dp[i-1][0]*3 + dp[i-1][1]*2
#    dp[i][1] = dp[i-1][0]*2 + dp[i-1][1]*2
# 初始化：对于dp[1]来说，一共12种情况，其中6中ABC型6种ABA型
class Solution:
    def numOfWays(self, n: int) -> int:
        dp =[[0, 0] for _ in range(n+1)]
        dp[1][0] = 6
        dp[1][1] = 6
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0]*3 + dp[i-1][1]*2) % 1000000007
            dp[i][1] = (dp[i-1][0]*2 + dp[i-1][1]*2) % 1000000007
        return (dp[-1][0] + dp[-1][1]) % 1000000007

if __name__ == '__main__':
    solution = Solution()
    n = 500
    res = solution.numOfWays(n)
    print(res)
    # a = 1e1
    # print(a)