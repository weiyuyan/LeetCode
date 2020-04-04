#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/1
'''
给定N个闭区间[ai,bi]，请你将这些区间分成若干组，使得每组内部的区间两两之间（包括端点）没有交集，并使得组数尽可能小。

输出最小组数。

输入格式
第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示最小组数。

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
# 一般来说，贪心问题最好能严格证明其正确性
from typing import List

class Solution:
    def _selectGroup(self, alist: List[List[int]]):
        # 按左端点从小到大排序
        # 从前往后处理每一个区间
        # 对于每个区间，判断能否将其放到现有的组中去（即当前区间的左端点是否小于等于该组的右端点，如果是，则不能放进去）
        # 如果不存在这样的组，则开一个新组，然后再将其放进去
        right_point = []
        alist.sort(key=lambda x: x[0])
        right = alist[0][1]
        right_point.append(right)

        for i in range(1, len(alist)):
            new = True
            for j in range(len(right_point)):
                if alist[i][0] <= right_point[j]:
                    continue
                else:
                    right_point[j] = alist[i][1]
                    new = False # 不需要添加新组
                    break
            if new:  #需要新开一个区间了
                right_point.append(alist[i][1])

        return len(right_point)

## 注意：本方法会超时
# 改进：

    def selectGroup(self, alist: List[List[int]]):
        # 按左端点从小到大排序
        # 从前往后处理每一个区间
        # 对于每个区间，判断能否将其放到现有的组中去（即当前区间的左端点是否小于等于该组的右端点，如果是，则不能放进去）
        # 如果不存在这样的组，则开一个新组，然后再将其放进去
        right_point = []
        alist.sort(key=lambda x: x[0])
        right = alist[0][1]
        right_point.append(right)

        for i in range(1, len(alist)):
            new = True
            for j in range(len(right_point)):
                if alist[i][0] <= min(right_point):
                    continue
                else:
                    right_point[j] = alist[i][1]
                    new = False # 不需要添加新组
                    break
            if new:  #需要新开一个区间了
                right_point.append(alist[i][1])

        return len(right_point)
if __name__ == '__main__':
    num = int(input())
    alist = []
    for i in range(num):
        alist.append(list(map(int, input().split())))

    solution = Solution()
    res = solution._selectGroup(alist)
    print(res)