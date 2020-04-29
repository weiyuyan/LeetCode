#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/23
'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000
通过次数4,324提交次数8,540
'''

# 分析：多重背包问题
# 状态表示：①集合：dp[i][j]表示只看前i种硬币，凑成j的集合  ②属性：count
# 状态计算：选第i个物品和不选第i个物品
# dp[i][j] = dp[i-1][j] + dp[i][j-v[i]]
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(5)]
        v = [1, 5, 10, 25]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j >= v[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-v[i-1]]
                    dp[i][j] %= 1000000007
                else:
                    dp[i][j] = dp[i-1][j]
                    dp[i][j] %= 1000000007
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.waysToChange(10)
    print(res)

