#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/15
'''
公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的
速度和效率。请你返回由最多 k 个工程师组成的最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。

团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

示例 1：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
输出：60
解释：
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
示例 2：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
输出：68
解释：
此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
示例 3：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
输出：72
 

提示：

1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n
'''
# 基本思想：以每个人作为最低效率时，前k个最大速度的最大团队表现值
#
# 首先按每个人的效率降序排序，O(nlogn)；
# 将每个人的速度依次插入小根堆中，add_sum记录速度和
# 当插入第k+1个数时，add_sum记录前k大速度和当前堆中最小值，add_sum减去最小值，仍为前k个最大速度之和；
# 速度和乘以最低效率即为当前最大团队表现值；
# 又k<n，因此最终时间复杂度O(nlogn)
from typing import List
from queue import PriorityQueue
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        items = [(speed[i], efficiency[i]) for i in range(n)]
        items.sort(key=lambda item:item[1], reverse=True)
        add_sum = 0
        pq = PriorityQueue()
        res = 0
        for i in range(n):
            pq.put(items[i][0])
            add_sum += items[i][0]
            if pq.qsize() > k:
                add_sum -= pq.get()
            val = add_sum * items[i][1]
            if val > res:
                res = val
        return res % (10 ** 9 + 7)