#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/14
'''
给定 n 个区间 [li,ri]，要求合并所有有交集的区间。

注意如果在端点处相交，也算有交集。

输出合并完成后的区间个数。

例如：[1,3]和[2,6]可以合并为一个区间[1,6]。

输入格式
第一行包含整数n。

接下来n行，每行包含两个整数 l 和 r。

输出格式
共一行，包含一个整数，表示合并区间完成后的区间个数。

数据范围
1≤n≤100000,
−10^9 ≤ li ≤ ri ≤ 10^9
输入样例：
5
1 2
2 4
5 6
7 8
7 9
输出样例：
3
'''
# 方法：按照左端点进行排序，更新start和end
# 用一个数组存放区间的左端点，一个数组存放区间的右端点

def merge(alist):
    if not alist: return 0
    res = 1
    left, right = alist[0][0], alist[0][1]
    for i in alist:
        if i[0] > right:
            left = i[0]
            right = i[1]
            res += 1
        else:   # i[0]<=right
            if i[1]>right:
                right = i[1]
    return res


if __name__ == '__main__':
    n = int(input())
    left_right = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        left_right.append([a, b])
    left_right.sort(key=lambda x: x[0])
    res = merge(left_right)
    print(res)


