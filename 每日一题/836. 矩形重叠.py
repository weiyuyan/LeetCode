#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/3
'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

示例 1：

输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
示例 2：

输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false

提示：

两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。
x 轴默认指向右，y 轴默认指向上。
你可以仅考虑矩形是正放的情况。
'''
'''
思路

我们尝试分析在什么情况下，矩形 rec1 和 rec2 没有重叠。

想象一下，如果我们在平面中放置一个固定的矩形 rec2，那么矩形 rec1 必须要出现在 rec2 的「四周」，也就是说，矩形 rec1 需要满足以下四种情况中的至少一种：

矩形 rec1 在矩形 rec2 的左侧；

矩形 rec1 在矩形 rec2 的右侧；

矩形 rec1 在矩形 rec2 的上方；

矩形 rec1 在矩形 rec2 的下方。

何为「左侧」？如果矩形 rec1 在矩形 rec2 的左侧，那就表示我们可以找到一条竖直的线（可以与矩形的边重合），
使得矩形 rec1 和 rec2 被分在这条竖线的两侧。对于「右侧」、「上方」以及「下方」，它们的定义与「左侧」是类似的。

算法

我们将上述的四种情况翻译成代码。具体地，我们用 (rec[0], rec[1]) 表示矩形的左下角，(rec[2], rec[3]) 表示矩形的右上角，
与题目描述一致。对于「左侧」，即矩形 rec1 在 x 轴上的最大值不能大于矩形 rec2 在 x 轴上最小值。对于「右侧」、「上方」以及「下方」同理。因此我们可以翻译成如下的代码：

左侧：rec1[2] <= rec2[0]；

右侧：rec1[0] >= rec2[2]；

上方：rec1[1] >= rec2[3]；

下方：rec1[3] <= rec2[1]。
'''
from typing import List
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

