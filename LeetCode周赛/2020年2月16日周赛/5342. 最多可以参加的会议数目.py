#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/16
'''
给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。

你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。

请你返回你可以参加的 最大 会议数目。



示例 1：



输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。
示例 2：

输入：events= [[1,2],[2,3],[3,4],[1,2]]
输出：4
示例 3：

输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
输出：4
示例 4：

输入：events = [[1,100000]]
输出：1
示例 5：

输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
输出：7


提示：

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
'''

from typing import List

'''
这是一道典型的扫描算法题。由于每个时间点最多参加一个会议，我们可以从1开始遍历所有时间。
对于每一个时间点，所有在当前时间及之前时间开始，并且在当前时间还未结束的会议都是可参加的。
显然，在所有可参加的会议中，选择结束时间最早的会议是最优的，因为其他会议还有更多的机会可以去参加。
# 思路不错，但是超时了
'''
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if len(events) == 1: return 1

        Days = []   # 参赛的日期

        # 对数组进行复合排序，先对第二列从小到大排序，在此基础上对第一列进行从小到大排序
        # 时间复杂度o(nlogn)
        events.sort(key=lambda x: (x[1], x[0])) # 这一句和下边5句一个功能，可见。。。（论憨批能有多憨
        # events.sort(key=lambda x: x[1])
        # for i in range(len(events)-1):
        #     if events[i][1] == events[i+1][1]:
        #         if events[i][0] > events[i+1][0]:
        #             events[i], events[i+1] = events[i+1], events[i]

        for i in events:
            for j in range(i[0], i[1]+1):
                if j not in Days:
                    Days.append(j)
                    break

        return len(Days)



'''
新的解法，爷把Days从List类型换成set就通过了。。。
草他妈的
为啥！！！
'''
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        # 对数组进行复合排序，先对第二列从小到大排序，在此基础上对第一列进行从小到大排序
        # 时间复杂度o(nlogn)
        events.sort(key=lambda x: (x[1], x[0]))

        # 这里把Days设置成set，然后就不超时了，很迷
        Days = set()
        for i in events:
            for j in range(i[0], i[1]+1):
                if j not in Days:
                    Days.add(j)
                    break

        return len(Days)


solution = Solution()
events = [[1, 2]]
res = solution.maxEvents(events)
print(res)
