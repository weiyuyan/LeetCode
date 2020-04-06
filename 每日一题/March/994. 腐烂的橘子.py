#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/4
'''
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2
'''
# 方法：利用队列
from typing import List
import collections

# 方法一：超棒的一个解法，广度优先算法
class Solution:
    def orangeRotting(self, grid: List[List[int]]):

        row, column = len(grid), len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(column) if grid[i][j]==2}
        fresh = {(i, j) for i in range(row) for j in range(column) if grid[i][j]==1}
        time = 0
        while fresh:
            if not rotten: return -1
            rotten = {(i+di, j+dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                      if (i+di, j+dj) in fresh}
            fresh -= rotten
            time += 1

        return time

# 方法二：广度优先搜索BFS，优先考虑使用队列
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i, j, time))

        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0<=i+di<row and 0<=j+dj<col and grid[i+di][j+dj]==1:
                    grid[i+di][j+dj] = 2
                    queue.append((i+di, j+dj, time+1))
        for row in grid:
            if 1 in row: return -1
        return time
