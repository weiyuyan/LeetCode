#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
输入一个n行m列的整数矩阵，再输入q个询问，每个询问包含四个整数x1, y1, x2, y2，表示一个子矩阵的左上角坐标和右下角坐标。

对于每个询问输出子矩阵中所有数的和。

输入格式
第一行包含三个整数n，m，q。

接下来n行，每行包含m个整数，表示整数矩阵。

接下来q行，每行包含四个整数x1, y1, x2, y2，表示一组询问。

输出格式
共q行，每行输出一个询问的结果。

数据范围
1≤n,m≤1000,
1≤q≤200000,
1≤x1≤x2≤n,
1≤y1≤y2≤m,
−1000≤矩阵内元素的值≤1000
输入样例：
3 4 3
1 7 2 4
3 6 2 8
2 1 2 3
1 1 2 2
2 1 3 4
1 3 3 4
输出样例：
17
27
21
'''
# 这是二维前缀和
# 子矩阵的s[i][j]如何求？
# s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

class Solution:
    def __init__(self, alist):
        self.s = [[0 for _ in range(len(alist[0])+1)] for _ in range(len(alist)+1)]
        # print(self.s)
        self.alist = alist

    def prefix_matrix(self):
        for i in range(1, len(self.s)):
            for j in range(1,  len(self.s[0])):
                self.s[i][j] = self.s[i][j-1] + self.s[i-1][j] - self.s[i-1][j-1] + self.alist[i-1][j-1]
        # print(self.s)

    def prefix_Sum(self, x1, y1, x2, y2):
        return self.s[x2][y2] + self.s[x1-1][y1-1] - self.s[x2][y1-1] - self.s[x1-1][y2]


if __name__ == '__main__':
    res = []
    matrix = []
    # a, b分别是矩阵的行与列, c是接下来的c组询问
    a, b, c = list(map(int, input().split()))
    for i in range(a):
        matrix.append(list(map(int, input().split())))

    solution = Solution(matrix)
    solution.prefix_matrix()

    for i in range(c):
        x1, y1, x2, y2 = list(map(int, input().split()))
        res.append(solution.prefix_Sum(x1, y1, x2, y2))
    for j in res:
        print(j)