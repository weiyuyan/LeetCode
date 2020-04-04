#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/1
'''
给定一个R行C列的矩阵，表示一个矩形网格滑雪场。

矩阵中第 i 行第 j 列的点表示滑雪场的第 i 行第 j 列区域的高度。

一个人从滑雪场中的某个区域内出发，每次可以向上下左右任意一个方向滑动一个单位距离。

当然，一个人能够滑动到某相邻区域的前提是该区域的高度低于自己目前所在区域的高度。

下面给出一个矩阵作为例子：

 1  2  3  4 5

16 17 18 19 6

15 24 25 20 7

14 23 22 21 8

13 12 11 10 9
在给定矩阵中，一条可行的滑行轨迹为24-17-2-1。

在给定矩阵中，最长的滑行轨迹为25-24-23-…-3-2-1，沿途共经过25个区域。

现在给定你一个二维矩阵表示滑雪场各区域的高度，请你找出在该滑雪场中能够完成的最长滑雪轨迹，并输出其长度(可经过最大区域数)。

输入格式
第一行包含两个整数R和C。

接下来R行，每行包含C个整数，表示完整的二维矩阵。

输出格式
输出一个整数，表示可完成的最长滑雪长度。

数据范围
1≤R,C≤300,
0≤矩阵中整数≤10000
输入样例：
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
输出样例：
25
'''
# 状态表示：①集合：f[i][j]所有从[i][j]开始滑的路径的集合    ②属性：max
# 状态计算：按照第一步往哪个方向滑，分成4类：向上、向下、向左、向右
# f[i][j]的最大值 == max(f[i][j]向上，f[i][j]向下，f[i][j]向左，f[i][j]向右)（前提是a[i][j]得大于它们）

# from typing import List
# class Solution:
#     def iceSkating(self, R: int, C:int, a:List[List[int]]):
#         dp = [[1 for _ in range(C+2)] for _ in range(R+2)]
#         for i in range(1, R+1):
#             for j in range(1, C+1):
#                 if a[i][j] > a[i][j+1]:
#                     dp[i][j] = max(dp[i][j], dp[i][j+1]+1)
#                 if a[i][j] > a[i][j-1]:
#                     dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
#                 if a[i][j] > a[i+1][j]:
#                     dp[i][j] = max(dp[i][j], dp[i+1][j]+1)
#                 if a[i][j] > a[i-1][j]:
#                     dp[i][j] = max(dp[i][j], dp[i-1][j]+1)
#         res = dp[1][1]
#         for i in range(1, R+1):
#             for j in range(1, C+1):
#                 if res<dp[i][j]:
#                     res=dp[i][j]
#         return res
#
# if __name__ == '__main__':
#     R, C = list(map(int, input().split()))
#     a = [[100000 for _ in range(C+2)] for _ in range(R+2)]
#     for r in range(1, R+1):
#         a[r] = [100000] + list(map(int, input().split())) + [100000]
#     solution = Solution()
#     res = solution.iceSkating(R, C, a)
#     print(res)
#

r,c = map(int, input().split())

arr = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(1, r+1):
    in_li = list(map(int, input().split()))
    for j in range(1, c+1):
        arr[i][j] = in_li[j-1]

# 2. 初始化dp数组
dp = [[-1 for i in range(c+1)] for j in range(r+1)]


# 3.递归搜索
dx = [-1,0,1,0]    # ！！！技巧：遍历方格的上下左右四个方向的技巧，新建两个这样的数组
dy = [0,1,0,-1]

def dfs(i, j):
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j] = 1
    for d in range(4):
        a = i+dx[d]
        b = j+dy[d]
        if a>=1 and a<=r and b>=1 and b<=c and arr[a][b]<arr[i][j]:
            dp[i][j] = max(dp[i][j], dfs(a,b)+1)
    return dp[i][j]

# def dfs(i,j):
#     if  dp[i][j]!=-1:
#         return dp[i][j]
#     dp[i][j] = 1    # 初始化dp[i][j]等于1，表示路劲只包含[i,j]元素，长度为1
#     for d in range(4):
#         a = i+dx[d]
#         b = j+dy[d]
#         if a>=1 and a<=r and b>=1 and b<=c and arr[a][b]<arr[i][j]:    # !出错，最后要比较arr数组中移动一个位置前后的高度大小
#             dp[i][j] = max(dp[i][j], dfs(a,b)+1)
#     return dp[i][j]
res = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        res = max(res, dfs(i, j))
print(res)
# res = 0
# for i in range(1, r+1):
#     for j in range(1, c+1):
#         res = max(res, dfs(i,j))
# print(res)