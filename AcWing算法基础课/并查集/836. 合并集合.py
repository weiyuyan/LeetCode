#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/16
'''
一共有n个数，编号是1~n，最开始每个数各自在一个集合中。

现在要进行m个操作，操作共有两种：

“M a b”，将编号为a和b的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
“Q a b”，询问编号为a和b的两个数是否在同一个集合中；
输入格式
第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“M a b”或“Q a b”中的一种。

输出格式
对于每个询问指令”Q a b”，都要输出一个结果，如果a和b在同一集合内，则输出“Yes”，否则输出“No”。

每个结果占一行。

数据范围
1≤n,m≤105
输入样例：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
输出样例：
Yes
No
Yes
'''
# 并查集
# ①将两个集合合并
# ②询问两个元素是否在一个集合中
# 基本原理：每个集合用一棵树来表示，树根的编号就是整个集合的编号
# 每个节点存储他的父节点，p[x]表示x的父节点

# 问题一：如何判断树根？
# 解：p[x] == x

# 问题二：如何求集合编号？
# 解：while(p[x] != x): x = p[x]

# 问题三：如何合并两个集合？
# 解：设px是x的集合编号，py是y的集合编号，只需要p[x] = y 或者 p[y] = x

# 优化：路径压缩

def find(x: int):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))  # n个数，m个操作
    p = [0]+[i for i in range(1, n+1)]
    for j in range(m):  # 接下来m个操作
        option, a, b = input().split()
        a = int(a); b = int(b)
        if option == 'M':
            p[find(a)] = find(b)
        else:
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')


