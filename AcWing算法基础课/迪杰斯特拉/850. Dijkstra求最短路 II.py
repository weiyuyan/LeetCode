#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/23

import heapq
def dijkstra():
    dist = [float("inf") for i in range(n+1)]    # 存储每个点到节点1的最短距离
    dist[1] = 0
    heap = []   # 初始化小跟堆
    heapq.heappush(heap,(0, 1))    # heap存到是二元组，0 表示到起点1的最短距离，1表示节点编号
    while heap:
        d, t = heapq.heappop(heap)    # heap存到是二元组，d 表示节点t到起点的距离dist[t]，t表示节点编号
        st[t] = True
        # 用t更新其他点的距离
        if t not in graph: continue
        for weight,node in graph[t]:
            if dist[node]>dist[t]+weight:
                dist[node] = dist[t]+weight
                heapq.heappush(heap, (dist[node], node))    # heap存到是二元组，d 表示节点t到起点的距离dist[t]，t表示节点编号
    if dist[n]==float("inf"):
        return -1
    else:
        return dist[n]

# 输入示例
n, m = map(int, input().split())
st = [False for i in range(n+1)]
graph = {}
while m:
    x,y,z = map(int, input().split())    # 表示点x-->点y，权重是z
    if x not in graph:
        graph[x] = [(z,y)]    # 按照（权重，节点）的顺序存是因为heapq存元组时只能按照第一个元素的顺序出堆
    else:
        graph[x].append((z,y))
    m -= 1
print(dijkstra())
