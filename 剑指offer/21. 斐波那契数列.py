#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/11
'''
输入一个整数 n ，求斐波那契数列的第 n 项。

假定从0开始，第0项为0。(n<=39)

样例
输入整数 n=5

返回 5
'''


class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0, 1, 1]
        if n <= 2:
            return res[n]
        for i in range(3, n+1):
            res.append(res[i-1]+res[i-2])

        return res[-1]
solution = Solution()
res = solution.Fibonacci(0)
print(res)