#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/12
'''
Palmia国有一条横贯东西的大河，河有笔直的南北两岸，岸上各有位置各不相同的N个城市。

北岸的每个城市有且仅有一个友好城市在南岸，而且不同城市的友好城市不相同。

每对友好城市都向政府申请在河上开辟一条直线航道连接两个城市，但是由于河上雾太大，政府决定避免任意两条航道交叉，以避免事故。

编程帮助政府做出一些批准和拒绝申请的决定，使得在保证任意两条航线不相交的情况下，被批准的申请尽量多。

输入格式
第1行，一个整数N，表示城市数。

第2行到第n+1行，每行两个整数，中间用1个空格隔开，分别表示南岸和北岸的一对友好城市的坐标。

输出格式
仅一行，输出一个整数，表示政府所能批准的最多申请数。

数据范围
1≤N≤5000,
0≤xi≤10000
输入样例：
7
22 4
2 6
10 3
15 12
9 8
17 17
4 2
输出样例：
4
'''
# 思考：北岸的城市和南岸的城市是一对自变量与因变量的关系
# 因此，我们把北岸城市位置做一个排序，然后按照相应南岸城市的位置做一个最长上升子序列

from typing import List
class Solution:
    def friendly_city(self, cities: List[tuple]):
        res = 0
        cities.sort(key=lambda x: x[0])
        south = []
        for i in cities:
            south.append(i[1])

        dp = [1 for _ in range(len(south))]
        for i in range(1, len(dp)):
            for j in range(i):
                if south[i]>south[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        res = max(dp)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = int(input())
    cities = []
    for i in range(nums):
        north, south = list(map(int, input().split()))
        cities.append((north, south))
    res = solution.friendly_city(cities)
    print(res)