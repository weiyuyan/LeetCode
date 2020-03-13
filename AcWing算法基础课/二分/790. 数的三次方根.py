#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/13
'''
给定一个浮点数n，求它的三次方根。

输入格式
共一行，包含一个浮点数n。

输出格式
共一行，包含一个浮点数，表示问题的解。

注意，结果保留6位小数。

数据范围
−10000≤n≤10000
输入样例：
1000.00
输出样例：
10.000000
'''
class Solution:
    # 用二分查找法
    # 注意：如果精度是保留6位小数，那么最好算到第8位，如果是保留4位，那么最好算到第6位，以此类推。。。
    def cube_root(self, num):
        l, r = -10000.0, 10000.0
        while(r-l>1e-8):
            mid = (l + r) / 2.0
            tmp = mid**3
            if tmp < num:
                l = mid
            else:
                r = mid
        print("{:.6f}".format(mid))
        return


if __name__ == '__main__':
    solution = Solution()
    num = float(input())
    solution.cube_root(num)
