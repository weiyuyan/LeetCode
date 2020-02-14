#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/13
'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''

# 分析：这道题用宽度优先搜索遍历BFS
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 先设定一个visited数组，用来纪录是否访问过所有元素
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.all = 0
        self.m = m
        self.n = n
        a = self.bfs(0, 0, k)
        return self.all

    # bfs
    def bfs(self, m, n, k):
        if m >= self.m or m < 0 or n >= self.n or n < 0:  return  # 如果越界了，返回
        if self.visited[m][n]:  return  # 如果遍历过，返回
        self.visited[m][n] = True   # 如果没有遍历过，标记为True
        res = self.judge(m, n)  # 判断是否可行，得到横纵坐标加和
        if res > k: return  # 如果超过k，返回
        self.all += 1   # 总数+1
        # m的上下左右，n的上下左右
        dm = [-1, 1, 0, 0]
        dn = [0, 0, -1, 1]
        for i in range(4):
            self.bfs(m+dm[i], n+dn[i], k)   # 上下左右走
        return True

    # 一个判断函数，用来判断是否超界
    def judge(self, m, n):
        res = 0
        while m:
            res += m % 10
            m //= 10
        while n:
            res += n % 10
            n //= 10
        return res

solution = Solution()
m, n, k = 1, 5, 6
res = solution.movingCount(m, n, k)
print(res)