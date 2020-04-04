#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/2
'''
给定N个闭区间[ai,bi]以及一个线段区间[s,t]，请你选择尽量少的区间，将指定线段区间完全覆盖。

输出最少区间数，如果无法完全覆盖则输出-1。

输入格式
第一行包含两个整数s和t，表示给定线段区间的两个端点。

第二行包含整数N，表示给定区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示所需最少区间数。

如果无解，则输出-1。

数据范围
1≤N≤105,
−109≤ai≤bi≤109,
−109≤s≤t≤109
输入样例：
1 5
3
-1 3
2 4
3 5
输出样例：
2
'''
from typing import List
class Solution:
    def calculate(self, area: List[List[int]], s: int, t: int):
        area.sort(key=lambda x: (x[0], x[1]))
        tmp_start = area[0][0]
        tmp_end = area[0][1]
        if tmp_start> s: return -1
        res = 1

        new_aera = [area[0]]   # 要使新的area里所有组的第0项不同
        for j in range(1, len(area)):
            if area[j][0] > area[j-1][1]+1: # 说明中间有空档
                return -1

            if area[j][0] == area[j-1][0]:
                continue
            else:
                new_aera.append(area[j])

        for i in range(1, len(new_aera)):
            if tmp_end >= t:
                return res
            if new_aera[i][0] < tmp_end:
                continue
            elif new_aera[i][0] > tmp_end+1:
                tmp_end = new_aera[i-1][1]
                res += 1
            else:
                tmp_end = new_aera[i][1]
                res += 1
        if tmp_end < t:
            if new_aera[i][1] >= t:
                res += 1
                return res
            else:
                return -1
        return res


if __name__ == '__main__':
    s, t = list(map(int, input().split()))
    N = int(input())
    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))

    solution = Solution()
    res = solution.calculate(area, s, t)
    print(res)
