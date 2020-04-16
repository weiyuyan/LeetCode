#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
通过次数71,489提交次数173,675
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        # 先排序
        intervals.sort(key=lambda x: x[0])
        res = []
        begin = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
        res.append([begin, end])
        return res

if __name__ == '__main__':
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res = solution.merge(intervals)
    print(res)