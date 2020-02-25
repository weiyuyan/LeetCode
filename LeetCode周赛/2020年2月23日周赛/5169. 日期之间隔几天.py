#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/23
'''
请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。

示例 1：

输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
示例 2：

输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15

提示：
给定的日期是 1971 年到 2100 年之间的有效日期。
'''
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        normal_year = 365
        leap_year = 366
        normal_year_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_year_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0
        date1 = date1.split('-')
        date2 = date2.split('-')
        if int(date1[0]) > int(date2[0]):
            date1, date2 = date2, date1

        for year in range(int(date1[0]), int(date2[0])):
            if (year%4 == 0 and year%100 != 0) or year%400 == 0:
                # 闰年
                res += 366
            else:
                res += 365

        for month in range(1, int(date2[1])):
            if (int(date2[0])%4 == 0 and int(date2[0])%100 != 0) or int(date2[0])%400 == 0:
                # 闰年
                res += leap_year_month[month-1]
            else:
                res += normal_year_month[month-1]

        for month in range(1, int(date1[1])):
            if (int(date1[0])%4 == 0 and int(date1[0])%100 != 0) or int(date1[0])%400 == 0:
                # 闰年
                res -= leap_year_month[month-1]
            else:
                res -= normal_year_month[month-1]

        res += (int(date2[2])-int(date1[2]))
        return abs(res)
solution = Solution()
res = solution.daysBetweenDates('2019-05-30', '2019-06-29')
print(res)