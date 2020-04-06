#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/29
'''
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。

 

示例 1：



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：



输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
 

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1
通过次数13,359提交次数30,701
'''
# 思考：用动态规划的方法解
# 状态表示（化零为整）①集合f[i][j]表示第i行第j列上元素（只能是海洋）到四周最近陆地的曼哈顿距离 ②属性：min
# 状态计算（化整为零）
# 如果f[i][j]是陆地：f[i][j] = 0，else：f[i][j] = min(f[i-1][j], f[i][j-1], f[i+1][j], f[i][j+1])+1
# 但这样还是有点问题，因为你是从上到下，从左到右遍历的，你不知道下面和右面元素的状况，所以得分开，遍历两次
# 从左上遍历：如果f[i][j]是陆地：f[i][j] = 0，else：f[i][j] = min(f[i-1][j], f[i][j-1])+1
# 从右下遍历：如果f[i][j]是陆地：f[i][j] = 0，else：f[i][j] = min(f[i+1][j], f[i][j+1])+1
from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf') for _ in range(n+2)] for _ in range(n+2)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                a = grid[i-1][j-1]
                dp[i][j] = 0 if a==1 else min(dp[i-1][j], dp[i][j-1])+1

        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                a = grid[i-1][j-1]
                dp[i][j] = 0 if a == 1 else min(dp[i+1][j], dp[i][j+1], dp[i][j-1], dp[i-1][j]) + 1

        print(dp)
        res = 0
        for i in range(n+1):
            for j in range(n+1):
               if dp[i][j] != float('inf') and dp[i][j] > res:
                   res = dp[i][j]

        return res if res!=0 else -1

if __name__ == '__main__':
    solution = Solution()
    arr = [[1,0,0,0,0,1,0,0,0,1],
           [1,1,0,1,1,1,0,1,1,0],
           [0,1,1,0,1,0,0,1,0,0],
           [1,0,1,0,1,0,0,0,0,0],
           [0,1,0,0,0,1,1,0,1,1],
           [0,0,1,0,0,1,0,1,0,1],
           [0,0,0,1,1,1,1,0,0,1],
           [0,1,0,0,1,0,0,1,0,0],
           [0,0,0,0,0,1,1,1,0,0],
           [1,1,0,1,1,1,1,1,0,0]]

    arr = [[1,0,0],[0,0,0],[0,0,0]]
    res = solution.maxDistance(arr)
    print(res)