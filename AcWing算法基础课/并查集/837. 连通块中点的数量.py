#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/16
'''
给定一个包含n个点（编号为1~n）的无向图，初始时图中没有边。

现在要进行m个操作，操作共有三种：

“C a b”，在点a和点b之间连一条边，a和b可能相等；
“Q1 a b”，询问点a和点b是否在同一个连通块中，a和b可能相等；
“Q2 a”，询问点a所在连通块中点的数量；
输入格式
第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“C a b”，“Q1 a b”或“Q2 a”中的一种。

输出格式
对于每个询问指令”Q1 a b”，如果a和b在同一个连通块中，则输出“Yes”，否则输出“No”。

对于每个询问指令“Q2 a”，输出一个整数表示点a所在连通块中点的数量

每个结果占一行。

数据范围
1≤n,m≤10^5
输入样例：
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
输出样例：
Yes
2
3
'''
# 思路：用集合维护一个连通块
# 前两个操作和上一个操作是一样一样的，多了第三个操作
# 多了一个操作：统计一个集合块中点的数量
# 方法：多加一个size数组，用来统计集合中点的数量
# size的话，我们只需要维护根节点的size数就行
def find(x: int):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))  # n个数，m个操作
    p = [0]+[i for i in range(1, n+1)]
    size = [0]+[1]*n
    for j in range(m):  # 接下来m个操作

        option_a_b = input().split()
        if len(option_a_b) == 3:
            option, a, b = option_a_b
            a = int(a); b = int(b)
        else:
            option, a = option_a_b
            a = int(a)

        if option == 'C':
            if find(a) == find(b):
                continue
            size[find(b)] += size[find(a)]
            p[find(a)] = find(b)

        elif option == 'Q1':
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')

        else:
            print(size[find(a)])
