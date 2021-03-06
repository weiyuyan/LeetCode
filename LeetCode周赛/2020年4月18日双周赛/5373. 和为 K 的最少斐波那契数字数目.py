#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/18
'''
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

示例 1：

输入：k = 7
输出：2
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
示例 2：

输入：k = 10
输出：2
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
示例 3：

输入：k = 19
输出：3
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。

提示：

1 <= k <= 10^9
'''

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        self.Fibo = [1, 1]
        while(self.Fibo[-1] < 1e10):
            self.Fibo.append(self.Fibo[-1]+self.Fibo[-2])
            self.res = 0

        self.search(k)
        return self.res

    def search(self, k: int):
        for i in range(1, len(self.Fibo)):
            if k == self.Fibo[i]:
                self.res += 1
                return
            elif k > self.Fibo[i]:
                continue
            else:   # k < self.Fibo[i]
                self.res += 1
                self.search(k-self.Fibo[i-1])
                return


if __name__ == '__main__':
    solution = Solution()
    res = solution.findMinFibonacciNumbers(19)
    print(res)
