#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/3
'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

'''
from typing import List
# 方案一： 动态规划+存储数组
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        sum_matrix = [[0] if matrix[i]==0 else [1] for i in range(len(matrix))]
        # 按行计算，如果有连着的1就累加，如果遇到0就置零
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    sum_matrix[i].append(sum_matrix[i][j-1])
                if matrix[i][j] == 0:
                    sum_matrix[i].append(0)

        # 数组建立完毕，开始计算，要竖着计算
        max_num = 0
        # for j in range(len(sum_matrix[0])):
        #     for i in range

        # P.S. 要解决这个问题，得先熟悉第LeetCode84题：柱状图中最大的矩形

