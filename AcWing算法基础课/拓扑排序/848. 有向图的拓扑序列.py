#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/22
'''
给定一个n个点m条边的有向图，点的编号是1到n，图中可能存在重边和自环。

请输出任意一个该有向图的拓扑序列，如果拓扑序列不存在，则输出-1。

若一个由图中所有点构成的序列A满足：对于图中的每条边(x, y)，x在A中都出现在y之前，则称A是该图的一个拓扑序列。

输入格式
第一行包含两个整数n和m

接下来m行，每行包含两个整数x和y，表示存在一条从点x到点y的有向边(x, y)。

输出格式
共一行，如果存在拓扑序列，则输出拓扑序列。

否则输出-1。

数据范围
1≤n,m≤105
输入样例：
3 3
1 2
2 3
1 3
输出样例：
1 2 3
'''
'''
拓扑序列
对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，
使得图中任意一对顶点u和v，若边<u,v>∈E(G)，则u在线性序列中出现在v之前。 
通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。
'''

# 有向图才有拓扑序列
# 有向无环图一定存在一个拓扑序列，所以有向无环图也称为拓扑图
# 如果存在环的话，一定不存在拓扑序列
# 一个有向无环图一定能找到一个入度为0的点
# 因为所有入度为0的点都可以排在当前序列的最前面，所以要先找到入度为0的点