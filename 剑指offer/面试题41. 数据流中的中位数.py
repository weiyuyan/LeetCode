#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/21
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 

限制：

最多会对 addNum、findMedia进行 50000 次调用。
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = []
        self.MaxHeap = []
        self.MinHeap = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)


    def findMedian(self) -> float:
        # 建立一个大根堆（最大堆）和一个小根堆（最小堆）
        # 大根堆的堆顶存放所有节点中的最大值
        # 小根堆的堆顶存放所有节点中的最小值
        # 两个堆中数据的数目之差不能超过1
        # 要保证大根堆中所有的元素都要小于小根堆中的元素，也就是大根堆的堆顶元素小于小根堆的堆顶元素
        MaxHeap = []
        MinHeap = []

import heapq
class MedianFinder:

    def __init__(self):
        self.s, self.l = [], []

    def addNum(self, num: int) -> None:
        if len(self.s) == len(self.l):
            heapq.heappush(self.s, -heapq.heappushpop(self.l, num))
        else:
            heapq.heappush(self.l, -heapq.heappushpop(self.s, -num))

    def findMedian(self) -> float:
        return len(self.s) == len(self.l) and (self.l[0] - self.s[0]) / 2 or -self.s[0]

class MedianFinder:
    def __init__(self):
        self.s, self.l = [], []

    def addNum(self, num: int) -> None:
        if len(self.s) == len(self.l):
            heapq.heappush(self.s, -heapq.heappushpop(self.l, num))
        else:
            heapq.heappush(self.l, heapq.heappushpop(self.s, -num))
    def findMedian(self) -> float:
        return len(self.s) == len(self.l) and (self.l[0] - self.s[0]) / 2 or -self.s[0]
