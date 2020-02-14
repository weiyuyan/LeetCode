#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/14
'''
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

说明：

用返回一个整数列表来代替打印
n 为正整数
'''
from typing import List
class Solution:
    # def printNumbers(self, n: int) -> List[int]:
    #     tmp_res = ['0']    # 这里放的是字符串类型的结果
    #     res = []    # 这里放的是数值类型的结果
    #     # if n == 1:  return [int(_) for _ in tmp_res]
    #     if n <= 0:  return []
    #
    #     def dfs(tmp_res, depth):
    #         if depth == 0:    return
    #         next_tmp_res = []
    #         for i in tmp_res:
    #             for j in range(10):
    #                 next_tmp_res.append(i+str(j))
    #         print(next_tmp_res)
    #         dfs(next_tmp_res, depth-1)
    #
    #     dfs(tmp_res, 2)

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]


solution = Solution()
res = solution.printNumbers(1)
# print(res)