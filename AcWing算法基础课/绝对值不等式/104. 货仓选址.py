#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/9
'''
在一条数轴上有 N 家商店，它们的坐标分别为 A1~AN。

现在需要在数轴上建立一家货仓，每天清晨，从货仓到每家商店都要运送一车商品。

为了提高效率，求把货仓建在何处，可以使得货仓到每家商店的距离之和最小。

输入格式
第一行输入整数N。

第二行N个整数A1~AN。

输出格式
输出一个整数，表示距离之和的最小值。

数据范围
1≤N≤100000
输入样例：
4
6 2 9 1
输出样例：
12
'''
# 很经典的问题
# 首先，如果我们把商店的地址设为x1, x2, x3,..., xn，把仓库的地址设为x，那么
# f(x)表示仓库到商店的距离和
# f(x) = abs(x-x1)+abs(x-x2)+abs(x-x3)+...+abs(x-xn)
# 首先公布一下答案：中位数！
# 如果是奇数个，那么把仓库放到中间那个商店即可
# 如果是偶数个，那么把仓库放到中间两个商店之间任一位置均可
# 证明：abs(x-x1)+abs(x-x2)+abs(x-x3)+...+abs(x-xn)
# = 【abs(x-x1)+abs(x-xn)】+【abs(x-x2)+abs(x-xn-1)】+...+
# 由于【abs(x-x1)+abs(x-xn)】最小值为xn-x1，所以：
# 原式 >= (xn-x1)+(xn-1-x2)+...+
# 取等号（=）的充要条件：x处在(x1, xn)之间，x处在(x2, xn-1)之间，x处在。。。(xn-k, xn-k+1)之间，其中，k是中间的数
# 即，x是中位数就可

if __name__ == '__main__':
    num = int(input())
    dist = list(map(int, input().split()))
    dist.sort()
    mid = len(dist) // 2
    mid_val = dist[mid]
    res = 0
    for i in range(len(dist)):
        res += abs(dist[i]-mid_val)
    print(res)

