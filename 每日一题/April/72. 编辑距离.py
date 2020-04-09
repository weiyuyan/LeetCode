#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/8
'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''
# 动态规划
# 状态表示：①集合：dp[i][j]表示从集合word1从0到i的位置 转到 word2从0到j的位置的方案的集合      ②属性：min
# 状态计算：dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1 (if word[j-1]!=word[i-1]), dp[i-1][j-1](if word[j-1]!=word[i-1]))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l_word1 = len(word1)
        l_word2 = len(word2)
        dp = [[0 for _ in range(l_word2+1)] for _ in range(l_word1+1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    res = solution.minDistance(word1, word2)
    print(res)