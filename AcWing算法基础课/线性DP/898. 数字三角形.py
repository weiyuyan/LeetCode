#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/28
'''
给定一个如下图所示的数字三角形，从顶部出发，在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，
一直走到底层，要求找出一条路径，使路径上的数字的和最大。

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
输入格式
第一行包含整数n，表示数字三角形的层数。

接下来n行，每行包含若干整数，其中第 i 行表示数字三角形第 i 层包含的整数。

输出格式
输出一个整数，表示最大的路径数字和。

数据范围
1≤n≤500,
−10000≤三角形中的整数≤10000
输入样例：
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
输出样例：
30
'''

# 状态表示：①集合f[i][j]：表示所有从起点走到(i, j)，第i行第j列 的路径  ②属性（min max count）这里取max，即所有路径的最大值
# 状态计算：化整为零，将f[i][j]分成两类：从左上方来的和从右上方来的
# 即：f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j]
# 注：如果涉及到有i-1这样下标的情况，一般i是从1开始，这样不会出现数组越界的情况
# DP问题的时间复杂度，一般是状态数量*状态转移数量，本题里状态数量是n^2 = 250000，状态转移数量为1，所以时间复杂度o(n^2)
from typing import List
class Solution:
    def triangle(self, a_triangle: List[List[int]], n: int):
        dp = [[-20000 for _ in range(n+1)] for _ in range(n+1)]
        dp[1][1] = a_triangle[1][1]
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a_triangle[i][j]

        return max(dp[-1])

if __name__ == '__main__':
    n = int(input())
    triangle = [[0]]
    for i in range(n):
        triangle.append([0]+list(map(int, input().split())))
    # 这里为了对标dp数组，将边界进行了扩充，第一行增加了0，每一列也增加了0
    solution = Solution()
    res = solution.triangle(triangle, n)
    print(res)
