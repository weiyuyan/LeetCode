#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/9
'''
在一个果园里，达达已经将所有的果子打了下来，而且按果子的不同种类分成了不同的堆。

达达决定把所有的果子合成一堆。

每一次合并，达达可以把两堆果子合并到一起，消耗的体力等于两堆果子的重量之和。

可以看出，所有的果子经过n-1次合并之后，就只剩下一堆了。

达达在合并果子时总共消耗的体力等于每次合并所耗体力之和。

因为还要花大力气把这些果子搬回家，所以达达在合并果子时要尽可能地节省体力。

假定每个果子重量都为1，并且已知果子的种类数和每种果子的数目，你的任务是设计出合并的次序方案，使达达耗费的体力最少，并输出这个最小的体力耗费值。

例如有3种果子，数目依次为1，2，9。

可以先将1、2堆合并，新堆数目为3，耗费体力为3。

接着，将新堆与原先的第三堆合并，又得到新的堆，数目为12，耗费体力为12。

所以达达总共耗费体力=3+12=15。

可以证明15为最小的体力耗费值。

输入格式
输入包括两行，第一行是一个整数n，表示果子的种类数。

第二行包含n个整数，用空格分隔，第i个整数ai是第i种果子的数目。

输出格式
输出包括一行，这一行只包含一个整数，也就是最小的体力耗费值。

输入数据保证这个值小于231。

数据范围
1≤n≤10000,
1≤ai≤20000
输入样例：
3
1 2 9
输出样例：
15
'''
# 这是一个经典的哈夫曼树问题
# 权值最小额两个点在树中一定深度最深，同时可以互为兄弟
# 问题：刚开始的时候是合理的，在n堆果子中，然而，n堆果子在合并一次后的n-1堆，此时的哈夫曼树还是最优解吗

# 所以，正确的策略是，每次在剩余根堆中找出两个最小的，组成堆
# 方法一：优先队列
from queue import PriorityQueue
from typing import List
class Solution:
    def apple(self, apples: List[int]):
        q = PriorityQueue()
        res = 0
        for i in apples:
            q.put(i)

        while q.qsize() > 1:
            a = q.get()
            b = q.get()
            sum = a+b
            res += sum
            q.put(sum)

        return res

# 方法二：单调栈
class Solution:
    def apple(self, apples: List[int]):
        stack = []
        res = 0
        apples.sort(reverse=True)
        for i in apples:
            stack.append(i)

        while len(stack)>1:
            a = stack.pop()
            b = stack.pop()
            sum = a+b
            res += sum

            # 接着再把sum推进去
            tmp = []
            while stack and sum>stack[-1]:
                a = stack.pop()
                tmp.append(a)

            # 推进去
            stack.append(sum)
            # tmp中的元素也推进去
            for i in range(len(tmp)-1, -1, -1):
                stack.append(tmp[i])
        return res


if __name__ == '__main__':
    num = int(input())
    apples = list(map(int, input().split()))
    solution = Solution()
    res = solution.apple(apples)
    print(res)

