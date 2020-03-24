#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/22
'''
给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：

1 表示连接左单元格和右单元格的街道。
2 表示连接上单元格和下单元格的街道。
3 表示连接左单元格和下单元格的街道。
4 表示连接右单元格和下单元格的街道。
5 表示连接左单元格和上单元格的街道。
6 表示连接右单元格和上单元格的街道。


你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。

注意：你 不能 变更街道。

如果网格中存在有效的路径，则返回 true，否则返回 false 。



示例 1：



输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
示例 2：



输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
示例 3：

输入：grid = [[1,1,2]]
输出：false
解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
示例 4：

输入：grid = [[1,1,1,1,1,1,3]]
输出：true
示例 5：

输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
输出：true


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
'''
from typing import List
# class Solution:
#     def hasValidPath(self, grid: List[List[int]]) -> bool:
#         if len(grid)==1 and len(grid[0])==1: return True
#
#         self.flag = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
#         tmp_grid = [[0]*(len(grid[0])+2)]
#         for row in grid:
#             tmp_grid.append([0]+row+[0])
#         tmp_grid.append([0]*(len(grid[0])+2))
#
#         self.back_track(tmp_grid, 1, 1)
#         if self.flag[-2][-2] == 1:
#             return True
#         else:
#             return False
#
#     def back_track(self, tmp_grid, i, j):
#         if self.flag[i][j]==1 or i>=len(tmp_grid) or j>=len(tmp_grid[0]):
#             return
#
#         if tmp_grid[i][j] == 1:
#             if tmp_grid[i][j + 1] == 3 or tmp_grid[i][j + 1] == 5 or tmp_grid[i][j + 1] == 1:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j+1)
#
#             if tmp_grid[i][j - 1] == 4 or tmp_grid[i][j - 1] == 6 or tmp_grid[i][j - 1] == 1:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j-1)
#             else:
#                 return False
#
#         elif tmp_grid[i][j] == 2:
#             if tmp_grid[i + 1][j] == 5 or tmp_grid[i + 1][j] == 6 or tmp_grid[i + 1][j] == 2:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i+1, j)
#
#             if tmp_grid[i - 1][j] == 3 or tmp_grid[i - 1][j] == 4 or tmp_grid[i - 1][j] == 2:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i-1, j)
#
#             else:
#                 return False
#
#
#         elif tmp_grid[i][j] == 3:
#             if tmp_grid[i][j - 1] == 1 or tmp_grid[i][j - 1] == 4 or tmp_grid[i][j - 1] == 6:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j-1)
#
#             if tmp_grid[i + 1][j] == 2 or tmp_grid[i + 1][j] == 5 or tmp_grid[i + 1][j] == 6:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i + 1, j)
#
#             else:
#                 return False
#
#
#
#         elif tmp_grid[i][j] == 4:
#             if tmp_grid[i][j + 1] == 1 or tmp_grid[i][j + 1] == 3 or tmp_grid[i][j + 1] == 5:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j+1)
#
#             if tmp_grid[i + 1][j] == 2 or tmp_grid[i + 1][j] == 5 or tmp_grid[i + 1][j] == 6:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i + 1, j)
#
#             else:
#                 return False
#
#
#         elif tmp_grid[i][j] == 5:
#             if tmp_grid[i - 1][j] == 2 or tmp_grid[i - 1][j] == 3 or tmp_grid[i - 1][j] == 4:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i - 1, j)
#
#             if tmp_grid[i][j - 1] == 1 or tmp_grid[i][j - 1] == 4 or tmp_grid[i][j - 1] == 6:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j-1)
#
#             else:
#                 return False
#
#
#         elif tmp_grid[i][j] == 6:
#             if tmp_grid[i - 1][j] == 2 or tmp_grid[i - 1][j] == 3 or tmp_grid[i - 1][j] == 4:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i - 1, j)
#
#             if tmp_grid[i][j + 1] == 1 or tmp_grid[i][j + 1] == 3 or tmp_grid[i][j + 1] == 5:
#                 self.flag[i][j] = 1
#                 self.back_track(tmp_grid, i, j+1)
#
#             else:
#                 return False
#
#         return False

import collections


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0, 0)])
        occupied = {(0, 0)}

        while q:
            x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return True
            z = grid[x][y]

            # // (1, 3, 5)
            # 的水平入口方向向右，所以grid[x][y - 1]
            # 的水平出口方向向右，即(1, 4, 6)
            if z in (1, 3, 5) and y > 0 and grid[x][y - 1] in (1, 4, 6) and (x, y - 1) not in occupied:
                q.append((x, y - 1))
                occupied.add((x, y - 1))

            # (1, 4, 6)的水平出口方向向右，所以grid[x][y+1]的水平入口方向向右，即(1, 3, 5)
            if z in (1, 4, 6) and y < n - 1 and grid[x][y + 1] in (1, 3, 5) and (x, y + 1) not in occupied:
                q.append((x, y + 1))
                occupied.add((x, y + 1))

            # (2, 5, 6)的竖直入口方向向下，所以grid[x-1][y]的竖直出口方向向下，即(2, 3, 4)
            if z in (2, 5, 6) and x > 0 and grid[x - 1][y] in (2, 3, 4) and (x - 1, y) not in occupied:
                q.append((x - 1, y))
                occupied.add((x - 1, y))

            # (2, 3, 4)的竖直出口方向向下，所以grid[x+1][y]的竖直入口方向向下，即(2, 5, 6)
            if z in (2, 3, 4) and x < m - 1 and grid[x + 1][y] in (2, 5, 6) and (x + 1, y) not in occupied:
                q.append((x + 1, y))
                occupied.add((x + 1, y))
        return False

solution = Solution()
grid = [[1]]
res = solution.hasValidPath(grid)
print(res)
