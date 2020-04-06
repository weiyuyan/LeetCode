#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/4
'''
给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。

换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。

示例 1：

输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形有公共点 (1,0)
示例 2：

输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true
示例 3：



输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
输出：true
示例 4：

输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false


提示：

1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2
'''


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 思考：对于每个正方形，只需要考虑四条边上的每个点距离圆心是否大于等于半径radius
        # 考虑到有存在于矩形内部的圆
        # 如果圆心在矩形内部，那么也符合条件
        if x_center >= x1 and x_center <= x2 and y_center >= y1 and y_center <= y2:
            return True

        radius_2 = radius*radius
        # 左边的边 (x1, y1) → (x1, y2)
        x1_2 = (x1-x_center)*(x1-x_center)
        for i in range(y1, y2+1):
            if x1_2 + (i-y_center)*(i-y_center) <= radius_2:
                return True

        # 右边的边 (x2, y1) → (x2, y2)
        x2_2 = (x2-x_center)*(x2-x_center)
        for i in range(y1, y2+1):
            if x2_2 + (i-y_center)*(i-y_center) <= radius_2:
                return True

        # 上边的边
        y2_2 = (y2-y_center)*(y2-y_center)
        for i in range(x1, x2+1):
            if y2_2 + (i-x_center)*(i-x_center) <= radius_2:
                return True

        # 下边的边
        y1_2 = (y1-y_center)*(y1-y_center)
        for i in range(x1, x2 + 1):
            if y1_2 + (i-x_center)*(i-x_center) <= radius_2:
                return True

        return False

if __name__ == '__main__':
    solution = Solution()
    radius = 1
    x_center = 1
    y_center = 1
    x1 = -3
    y1 = -3
    x2 = 3
    y2 = 3
    res = solution.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)
    print(res)