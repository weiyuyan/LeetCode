#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/14
'''
假定有一个无限长的数轴，数轴上每个坐标上的数都是0。

现在，我们首先进行 n 次操作，每次操作将某一位置x上的数加c。

接下来，进行 m 次询问，每个询问包含两个整数l和r，你需要求出在区间[l, r]之间的所有数的和。

输入格式
第一行包含两个整数n和m。

接下来 n 行，每行包含两个整数x和c。

再接下里 m 行，每行包含两个整数l和r。

输出格式
共m行，每行输出一个询问中所求的区间内数字和。

数据范围
−109≤x≤109,
1≤n,m≤105,
−109≤l≤r≤109,
−10000≤c≤10000
输入样例：
3 3
1 2
3 6
7 5
1 3
4 6
7 8
输出样例：
8
0
5
'''
def find(x):
    """二分查找模板，从索引数组alls中找到大于等于x的最小的索引"""
    l = 0
    r = len(alls)-1
    while l<r:
        mid = l+r>>1
        if alls[mid]>=x: r = mid    # ！！！if条件忘记了=号
        else: l = mid+1
    return l+1    # 因为要计算前缀和，所以加1保证索引从1开始

if __name__=="__main__":
    n, m = map(int, input().split())
    N = 300010
    a = [0]*N    # 用于存储离散化后的索引和对应值，其中索引对应离散化后的索引，值对应离散化前索引的取值
    s = [0]*N    # 存a数组的前缀和数组

    add = []    # 存储插入操作的二元组
    query = []    # 存储查询操作的二元组

    alls = []    # 存储离散化前输入的所有索引，n+2*m

    for i in range(n):
        x, c = map(int, input().split())
        add.append((x, c))
        alls.append(x)

    for i in range(m):
        l, r = map(int, input().split())
        query.append((l, r))
        alls.append(l)
        alls.append(r)

    alls = list(set(sorted(alls)))    # 将alls数组排序并去重


    # 1. 处理插入
    for x, c in add:
        x2 = find(x)
        a[x2]+=c

    # 2. 处理前缀和
    for i in range(1, len(alls)+1):
        s[i] = s[i-1]+a[i]

    # 3. 处理查询
    for l, r in query:
        l2 = find(l)
        r2 = find(r)
        res = s[r2]-s[l2-1]
        print(res)