#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/13
'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m≥1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        self.result = [0, 1, 1]    # 存放最短长度
        if n<= 0:   return 0
        if n<= 2:   return self.result[n]
        self.dfs(n)
        return self.result[-1] % (pow(10, 9)+7)

    def dfs(self, n: int):
        if n < len(self.result):
            return self.result[n]
        res = 0
        for i in range(1, n):
            tmp_res = max(self.dfs(i), i) * max(self.dfs(n-i), n-i)
            res = max(res, tmp_res)
        self.result.append(res)
        return res

solution = Solution()
res = solution.cuttingRope(121)
print(res)