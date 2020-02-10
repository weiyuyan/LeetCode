#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/10
'''
你的赛车起始停留在位置 0，速度为 +1，正行驶在一个无限长的数轴上。（车也可以向负数方向行驶。）

你的车会根据一系列由 A（加速）和 R（倒车）组成的指令进行自动驾驶 。

当车得到指令 "A" 时, 将会做出以下操作： position += speed, speed *= 2。

当车得到指令 "R" 时, 将会做出以下操作：如果当前速度是正数，则将车速调整为 speed = -1 ；否则将车速调整为 speed = 1。  (当前所处位置不变。)

例如，当得到一系列指令 "AAR" 后, 你的车将会走过位置 0->1->3->3，并且速度变化为 1->2->4->-1。

现在给定一个目标位置，请给出能够到达目标位置的最短指令列表的长度。

示例 1:
输入:
target = 3
输出: 2
解释:
最短指令列表为 "AA"
位置变化为 0->1->3
示例 2:
输入:
target = 6
输出: 5
解释:
最短指令列表为 "AAARA"
位置变化为 0->1->3->7->7->6
说明:

1 <= target（目标位置） <= 10000。
'''
# import functools
# @functools.lru_cache(None)
# def fun():
#     pass

# 太难了，立即推放弃考研
import heapq
class Solution(object):
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]

solution = Solution()
res = solution.racecar(6)

print(res)