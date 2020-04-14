#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/14
'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
通过次数19,956提交次数24,785
'''
# 方案一：借用存储空间
# 我们发现，原来的a[i][j]，在旋转后会变成a[j][n-i-1]
# 时间复杂度：o(n^2)
# 空间复杂度：o(n^2)
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new

# 方法二：先水平翻转，再主对角线翻转
# 水平翻转：matrix[row][col] = matrix[n-row-1][col]
# 主对角线翻转：matrix[row][col] = matrix[col][row]
# 合起来就是：matrix[row][col] = matrix[col][n-row-1]
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 先水平翻转
        for row in range(len(matrix)//2):
            for col in range(len(matrix[0])):
                matrix[row][col], matrix[n-row-1][col] = matrix[n-row-1][col], matrix[row][col]

        # 再主对角线翻转
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = solution.rotate(matrix)
    print(res)