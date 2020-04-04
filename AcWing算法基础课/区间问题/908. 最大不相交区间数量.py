#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/1
'''
给定N个闭区间[ai,bi]，请你在数轴上选择若干区间，使得选中的区间之间互不相交（包括端点）。

输出可选取区间的最大数量。

输入格式
第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示可选取区间的最大数量。

数据范围
1≤N≤105,
−109≤ai≤bi≤109
输入样例：
3
-1 1
2 4
3 5
输出样例：
2
'''
from typing import List
class Solution:
    def selectDot(self, alist: List[List[int]]):
        # 按左端点从小到大排序
        alist.sort(key=lambda x: x[0])
        res = 0
        right = alist[0][1]
        for i in alist:
            if i[0] <= right:   # 如果上一个的右端点大于等于下一个的左端点，说明重叠，不行
                res += 1
                right = i[1]

            else:
                continue
        return res

if __name__ == '__main__':
    num = int(input())
    alist = []
    for i in range(num):
        alist.append(list(map(int, input().split())))

    solution = Solution()
    res = solution.selectDot(alist)
    print(res)