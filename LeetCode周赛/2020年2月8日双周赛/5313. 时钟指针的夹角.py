#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/8
'''
给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。
'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_extra = minutes/60 * (360/12)
        hour_real = hour_extra + hour/12 * 360
        minutes_real = minutes/60 * 360
        res = min(abs(hour_real-minutes_real), 360-abs(hour_real-minutes_real))
        return res

solution = Solution()
res = solution.angleClock(4, 50)
print(res)