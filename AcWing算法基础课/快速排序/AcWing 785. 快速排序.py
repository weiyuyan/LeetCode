#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/11
'''
给定你一个长度为n的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

输入格式
输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在1~109范围内），表示整个数列。

输出格式
输出共一行，包含 n 个整数，表示排好序的数列。

数据范围
1≤n≤100000
输入样例：
5
3 1 2 4 5
输出样例：
1 2 3 4 5
'''
# def quicksort(nums, left, right):
#     if len(nums) <=1 : return
#     i, j = left, right-1
#     flag = nums[-1]
#     for _ in range(len(nums)):
#         while(nums[i]<=flag):
#             i+=1
#         while(nums[j]>=flag):
#             j-=1
#         if i >= j: break
#         nums[i], nums[j] = nums[j], nums[i]
#
#
#     quicksort(nums, 0, i)
#     quicksort(nums, j, len(nums)-1)

def quicksort(q,l,r):
    if l>=r:
        return
    x = q[(l+r)//2]
    i,j = l-1,r+1
    while(i<j):
        while True:
            i+=1
            if q[i]>=x:
                break
        while True:
            j-=1
            if q[j] <=x:
                break
        if i < j:
            q[i],q[j]=q[j],q[i]

    quicksort(q,l,j)
    quicksort(q,j+1,r)

# def quick_sort(q, l, r):
#     if l>=r: return
#     x = q[(l+r)//2]
#     i, j = l-1, r+1
#     while(i<j):
#         while True:
#             i+=1
#             if q[i]>=x: break
#         while True:
#             j-=1
#             if q[j]<=x: break
#         if i<j:
#             q[i], q[j] = q[j], q[i]
#     quick_sort(q, l, j)
#     quick_sort(q, j+1, r)

def quick_sort(q, l, r):
    if l>=r: return
    i = l-1
    j = r+1
    x = q[(l+r)//2]
    while(i<j):
        while True:
            i+=1
            if q[i]>=x: break
        while True:
            j-=1
            if q[j]<=x: break
        if i<j:
            q[i], q[j] = q[j], q[i]
    quick_sort(q, l, j)
    quick_sort(q, j+1, r)

if __name__ == '__main__':
    n = int(input())
    alist = list(map(int, input().split()))
    quick_sort(alist, 0, n-1)
    for i in alist:
        print(i, end=' ')
