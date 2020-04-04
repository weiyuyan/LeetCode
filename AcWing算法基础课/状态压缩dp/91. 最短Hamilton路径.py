#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/31
'''
给定一张 n 个点的带权无向图，点从 0~n-1 标号，求起点 0 到终点 n-1 的最短Hamilton路径。
 Hamilton路径的定义是从 0 到 n-1 不重不漏地经过每个点恰好一次。

输入格式
第一行输入整数n。

接下来n行每行n个整数，其中第i行第j个整数表示点i到j的距离（记为a[i,j]）。

对于任意的x,y,z，数据保证 a[x,x]=0，a[x,y]=a[y,x] 并且 a[x,y]+a[y,z]>=a[x,z]。

输出格式
输出一个整数，表示最短Hamilton路径的长度。

数据范围
1≤n≤20
0≤a[i,j]≤107
输入样例：
5
0 2 4 5 1
2 0 6 5 3
4 6 0 8 3
5 5 8 0 5
1 3 3 5 0
输出样例：
18
'''
# 状态表示：①集合f[i][j]：所有从0开始走到j，走过的所有点是i的所有路径的集合，这里i表示状态，是一个二进制数，
# 如：i = (101001)表示第一个点走过了，第二、三个点没走过、第4个点走过了、第五个点没走、第六个点走过了
# ②属性：min
# 状态计算：倒数第二个点是哪个（倒数第2个点是0是第1类，倒数第2个点是1是第2类,...,倒数第二个点是k的话是第k+1类...）
# 如果前一个点是k的话，f[i][j] = f[i-{j}][k] + a[k][j]
# 综上，f[i][j] = min(f[i-{j}][k] + a[k][j]) for k in range(1, j-1)
n = int(input().strip())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[float('inf') for i in range(n)] for j in range(1<<n)]
dp[1][0] = 0    # 从第0号点到第0号点，因为只走了第0个点，所以是0000001，故为1，代价为0
for i in range(1<<n):   # 遍历在从第0号点到第j号点时，可能经过的所有节点组成的路径
    for j in range(n):  # 遍历所有路径可能结尾的点[0~n-1]
        if (i>>j)&1:    # 如果路径i以j号点结尾
            for k in range(n):  # 遍历以第j号点结尾的路径i的倒数第二个点的编号k
                if (i-(1<<j))>>k & 1:   # 如果路径i删除节点j后，倒数第二个节点为k，则执行状态转移方程
                    dp[i][j] = min(dp[i][j], dp[i-(1<<j)][k] + a[k][j])
# print(dp[(1<<n)-1][n-1])
print(dp[-1][-1])
