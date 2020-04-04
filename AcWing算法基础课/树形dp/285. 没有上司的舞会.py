#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/31
'''
Ural大学有N名职员，编号为1~N。

他们的关系就像一棵以校长为根的树，父节点就是子节点的直接上司。

每个职员有一个快乐指数，用整数 Hi 给出，其中 1≤i≤N。

现在要召开一场周年庆宴会，不过，没有职员愿意和直接上司一起参会。

在满足这个条件的前提下，主办方希望邀请一部分职员参会，使得所有参会职员的快乐指数总和最大，求这个最大值。

输入格式
第一行一个整数N。

接下来N行，第 i 行表示 i 号职员的快乐指数Hi。

接下来N-1行，每行输入一对整数L, K,表示K是L的直接上司。

输出格式
输出最大的快乐指数。

数据范围
1≤N≤6000,
−128≤Hi≤127
输入样例：
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
输出样例：
5
'''
# 树形dp最经典的问题

# 要求：在邀请的那些人里，不存在某一个人是另一个人的直接上司
# 树形dp问题
# 状态表示：①集合：f[u][0]：所有从以u为根的子树中选择，并且不选u这个点的方案
# f[u][1]：所有从以u为根的子树中选择，并且选u这个点的方案
# ②属性：
# 状态计算：假设u是一个父节点，它的子节点是s1, s2, s3,..., sn，那么
# f[u][0] = ∑ max(f[si][0], f[si][1])
# f[u][1] = ∑ f[si][0]
# 时间复杂度：首先一共有2n个状态（0或1），每个状态在计算的时候需要枚举它所有的儿子（也就是树的边的数量：n-1）

class Node:
    def __init__(self, happy: int):
        self.happy = happy
        self.son = []
        self.father = None

class Solution:

    def noBossParty(self, N: int, root: Node):
        self.dp = [[0, 0] for _ in range(N+1)]
        pass
    def dfs(self, root: int):
        child = a_dict[root].son
        self.dp[root][1] =
if __name__ == '__main__':
    N = int(input())
    happy = []
    # 设置一个字典，存放Node和它们的信息
    # {key: Node编号（从1开始）, value: class Node}
    a_dict = {}
    for i in range(N):
        node_happy = int(input())
        # 将happy值存入node
        happy.append(node_happy)
        a_dict[i+1] = Node(node_happy)

    # 有N-1条边，所以接下来输入N-1次
    for j in range(N-1):
        son, father = list(map(int, input().split()))   # son和father是Node节点编号
        # 互相更新son、father信息
        a_dict[son].father = a_dict[father]
        a_dict[father].son.append(a_dict[son])

    # 找到树的根节点
    # 拿node1开刀
    root = a_dict[1]
    while(root.father):
        root = root.father

    solution = Solution()
    res = solution.noBossParty(N, root)

