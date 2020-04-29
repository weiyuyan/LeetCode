#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/21
'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
通过次数96,282提交次数195,712
'''
# 方法一：DFS
# 我们可以将二维网格看成一个无向图，竖直或水平相邻的 11 之间有边相连。
#
# 为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 11，则以其为起始节点开始进行深度优先搜索。
# 在深度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 00。
#
# 最终岛屿的数量就是我们进行深度优先搜索的次数。

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    res += 1
                    self.dfs(row, col, grid)
        return res

    def dfs(self, r: int, c: int, grid: List[List[str]]):
        if r>=len(grid) or r<0 or c>=len(grid[0]) or c<0:
            return
        if grid[r][c] == '0':
            return
        if grid[r][c] == '1':
            grid[r][c] = '0'
        for x, y in ([r+1, c], [r-1, c], [r, c+1], [r, c-1]):
            self.dfs(x, y, grid)

        return

# 方法二：广度优先搜索
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    res += 1
                    neighbors = deque([(row, col)])
                    while neighbors:
                        row_, col_ = neighbors.popleft()
                        if grid[row_][col_] == '1':
                            grid[row_][col_] = '0'
                            for (x, y) in [(row_-1, col_), (row_+1, col_), (row_, col_-1), (row_, col_+1)]:
                                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                                    continue
                                else:
                                    neighbors.append((x, y))
        return res

# 方法三：并查集
# 使用并查集解决本问题的思想很简单：
#
# 1、如果当前是“陆地”，尝试与周围合并一下；
#
# 2、如果当前是“水域”，就把所有的“水域”合并在一起，为此，我设置了一个虚拟的结点，表示“所有的水域都和这个虚拟结点是连接的”。
#
# 注意：
#
# 1、针对上面的第 1 点：如果当前是 “陆地”，尝试与周围合并一下”，此时 “周围” 并不需要像 “深度优先遍历” 和 “广度优先遍历” 一样，
# 方向是四周。事实上，只要 “向右”、“向下” 两个方向就可以了，原因很简单，你可以在脑子里想象一个 “4 个方向” 和
# “2 个方向” 的算法执行流程（或者看我下面展示的动画），就知道 “4 个方向” 没有必要；
#
# 2、针对上面的第 2 点：由于我设置了“虚拟结点”，最后返回“岛屿个数”的时候，应该是连通分量个数 - 1，
# 不要忘记将 “虚拟结点” 代表的 “水域” 分量去掉，剩下的连通分量个数就是 “岛屿个数”。
#
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        row = len(grid)
        # 特判
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = row * col

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1


if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = solution.numIslands(grid)
    print(res)