#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/17
'''
输入一个长度为n的整数数列，从小到大输出前m小的数。

输入格式
第一行包含整数n和m。

第二行包含n个整数，表示整数数列。

输出格式
共一行，包含m个整数，表示整数数列中前m小的数。

数据范围
1≤m≤n≤105，
1≤数列中元素≤109
输入样例：
5 3
4 5 1 3 2
输出样例：
1 2 3
'''
# 如何手写一个堆？
# 1、插入一个数
# 2、求集合中的最小值
# 3、删除最小值
# 4、删除任意一个元素
# 5、修改任意一个元素

# 堆是一棵完全二叉树

# 小根堆性质：每一个点都小于它的左右儿子
# 堆的存储：一种全新的存储方式：用一个一维数组存
# 根节点编号是1
# 编号x的左儿子：2x
# 编号x的右儿子：2x+1

# 函数：
# down(x)往下调整
# up(x)往上调整

# 插入一个数：heap[++x]; up(size)
# 求最小值：heap[1]
# 删除一个数：取出堆最后一个元素，放到堆顶：heap[1] = heap[size]; size--; down(1)
# 删除第k个数：heap[k] = heap[size]; size--;  down(k) or up(k)
def down(u):
    t = u
    if(u*2 <= size and heap[u*2]<heap[t]):
        t = u*2
    if(u*2+1 <= size and heap[u*2+1]<heap[t]):
        t = u*2+1
    if u!=t:
        heap[u], heap[t] = heap[t], heap[u]
        down(t)



if __name__ == '__main__':
    heap = [0]
    n, m = list(map(int, input().split()))
    heap += list(map(int, input().split()))

    size = n

    for j in range(n>>1, 0, -1):
        down(j)

    while(m):
        m-=1
        print(heap[1])
        size-=1
        down(1)

