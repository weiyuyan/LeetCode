#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/9
'''
有 n 个人排队到 1 个水龙头处打水，第 i 个人装满水桶所需的时间是 ti，请问如何安排他们的打水顺序才能使所有人的等待时间之和最小？

输入格式
第一行包含整数 n。

第二行包含 n 个整数，其中第 i 个整数表示第 i 个人装满水桶所花费的时间 ti。

输出格式
输出一个整数，表示最小的等待时间之和。

数据范围
1≤n≤105,
1≤ti≤104
输入样例：
7
3 6 1 4 2 5 7
输出样例：
56
'''

if __name__ == '__main__':
    people = int(input())
    res = 0
    water = list(map(int, input().split()))
    water.sort()
    for i in range(1, people):
        res += (people-i)*water[i-1]

    print(res)