#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/1
'''
给定N个闭区间[ai,bi]，请你在数轴上选择尽量少的点，使得每个区间内至少包含一个选出的点。

输出选择的点的最小数量。

位于区间端点上的点也算作区间内。

输入格式
第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示所需的点的最小数量。

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
# 首先，对于区间问题，我们一般都会先排个序
# 一、将每个区间安装右端点按从小到大排序
# 二、从前往后依次枚举每个区间，如果当前区间中已经包含点，则直接pass，否则，选择当前区间的右端点
# 每次选点的话，尽量选择最右边的区间，即尽可能多地覆盖其他区间
# 贪心是一个比较短视的策略，每次决策只选择当前一小块的局部最优解，最后变成全局最优解
from typing import List
class Solution:
    def selectDot(self, alist: List[List[int]]):
        # 按右端点从小到大排序
        alist.sort(key=lambda x: x[1])
        res = 1
        right = alist[0][1]
        for i in alist:
            if right >= i[0] and right <= i[1]:
                continue
            else:
                res += 1
                right = i[1]
        return res

if __name__ == '__main__':
    num = int(input())
    alist = []
    for i in range(num):
        alist.append(list(map(int, input().split())))

    solution = Solution()
    res = solution.selectDot(alist)
    print(res)

