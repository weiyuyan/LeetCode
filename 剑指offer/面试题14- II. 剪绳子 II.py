#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/13
'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n 都是整数，n>1 并且 m≥1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''
# 思路：n < 5，用[1, 1, 2, 4]
#       n >= 5: res *= 3, n-= 3
class Solution:
    def cuttingRope(self, n: int) -> int:
        a = [0, 1, 1, 2, 4]
        if n < 0:  return False
        if n <= 4:  return a[n]
        res = 1
        while(n>=5):
            n -= 3
            res *= 3
        res *= n
        return res % (pow(10, 9)+7)

solution = Solution()
res = solution.cuttingRope(-120)
print(res)