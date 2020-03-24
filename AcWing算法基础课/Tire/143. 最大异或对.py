#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/16
'''
在给定的N个整数A1，A2……AN中选出两个进行xor（异或）运算，得到的结果最大是多少？

输入格式
第一行输入一个整数N。

第二行输入N个整数A1～AN。

输出格式
输出一个整数表示答案。

数据范围
1≤N≤105,
0≤Ai<231
输入样例：
3
1 2 3
输出样例：
3
'''
# 异或有可以叫无进位加法

# class Solution:
#     def __init__(self):
#         self.root = {}
#
#     def insert(self, num: int):
#         p = self.root
#         for bit in range(30, -1, -1):
#             s = num>>bit&1 # 看一下num的第bit位是0还是1
#             if s not in p:
#                 p[s] = {}
#             p = p[s]
#
#     def search(self, num: int):
#         tmp_res = 0
#         p = self.root
#         for bit in range(30, -1, -1):
#             s = num >> bit & 1  # 看一下num的第bit位是0还是1
#             _s = 0 if s else 1  # 与s取反
#             if _s in p:
#                 tmp_res += (1<<bit)
#                 p = p[_s]
#             else:
#                 p = p[s]
#         return tmp_res
#
# if __name__ == '__main__':
#     solution = Solution()
#     res = 0
#     n = input()
#     nums = list(map(int, input().split()))
#     for i in nums:
#         solution.insert(i)
#     for j in nums:
#         res = max(solution.search(j), res)
#     print(res)

## 别人写的，可以AC
n = int(input())
N = n+5
M = 30*N
a = [0]*N
son = [[0, 0] for i in range(M)]  ##  注意不要使用[[0, 0]] * M的形式，不知道错误原因
idx = 0


def insert(x):
    global idx
    p = 0  # 链表指针，开始指向0（头结点，空的，真正元素是下标为1开始的)
    ti = 30   # 对python语法不太了解，保险起见函数里不用i,怕与全局的i冲突
    while ti >= 0:
        if son[p][x >> ti & 1] == 0:  # 没有就创造
            idx += 1
            son[p][x >> ti & 1] = idx
        p = son[p][x >> ti & 1]
        ti -= 1


def search(x):
    p = 0  # 指针
    res = 0
    ti = 30
    while ti >= 0:
        s = x >> ti & 1
        if son[p][1 - s]:
            res += 1 << ti
            p = son[p][1 - s]
        else:
            p = son[p][s]
        ti -= 1
    return res

row = list(map(int, input().split()))
for i in range(n):
    a[i] = row[i]   # 为了使得a开的大小为N，这样保险一些
    insert(a[i])

ans = 0
for i in range(n):
    ans = max(ans, search(a[i]))
print(ans)