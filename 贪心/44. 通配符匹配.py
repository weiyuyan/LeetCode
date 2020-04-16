#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/15
'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false
通过次数26,092提交次数95,370
'''
# 尝试动态规划
# 状态表示：①集合：dp[i][j]表示s[1~i]与p[1~j]匹配  ②属性
# 状态转移：
# 1.如果p[j]是正常字符：dp[i][j] = s[i]==p[j] && dp[i+1][j+1]
# 2.如果p[j]是 '?'：dp[i][j] = dp[i+1][j+1]
# 3.如果p[j]是 '*'，此时有两种情况：
# ① 若p的第 j 个字符匹配空串, f[i][j] = f[i][j - 1]
# ② 若p的第 j 个字符匹配s的第 i 个字符, f[i][j] = f[i - 1][j]

# 初始化：
# dp[0][i] = dp[0][i - 1] && p[i] == '*'

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        # 初始化

        dp[0][0] = True
        for j in range(1, len(dp[0])):
            dp[0][j] = dp[0][j-1] and p[j-1]=='*'

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    s = "adceb"
    p = "*a*b"
    res = solution.isMatch(s, p)
    print(res)
