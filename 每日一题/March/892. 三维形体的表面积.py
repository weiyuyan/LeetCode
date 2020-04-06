#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。

示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],[3,4]]
输出：34
示例 3：

输入：[[1,0],[0,2]]
输出：16
示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46

提示：

1 <= N <= 50
0 <= grid[i][j] <= 50
'''
from typing import List
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        new_grid = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        for i in range(1, len(new_grid)):
            for j in range(1, len(new_grid[0])):
                new_grid[i][j] = grid[i-1][j-1]


        for i in range(1, len(new_grid)):
            for j in range(1, len(new_grid[0])):
                if new_grid[i][j] != 0:
                    res += (new_grid[i][j]-1)*4
                    res += 6

                    res -= min(new_grid[i][j], new_grid[i-1][j])*2
                    res -= min(new_grid[i][j], new_grid[i][j-1])*2

        return res

if __name__ == '__main__':
    solution = Solution()
    grid = [[2,2,2],[2,1,2],[2,2,2]]
    res = solution.surfaceArea(grid)
    print(res)