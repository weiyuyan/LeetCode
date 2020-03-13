#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/12
'''
给定一个长度为n的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。

输入格式
第一行包含整数n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

输出格式
输出一个整数，表示逆序对的个数。

数据范围
1≤n≤100000
输入样例：
6
2 3 4 5 6 1
输出样例：
5
'''
# 这里需要使用归并排序来做
class Solution:
    def nixushu(self, n, nums):
        self.res = 0
        self.tmp = [0]*1000000
        self.new_merge_sort(nums, 0, n-1)
        return self.res


    def new_merge_sort(self, q, l, r):
        if l>=r: return
        mid = (l+r)//2
        self.new_merge_sort(q, l, mid)
        self.new_merge_sort(q, mid+1, r)

        k, i, j = 0, l, mid+1
        while(i<=mid and j<=r):
            if q[i]<=q[j]:
                # self.res这里不需要做任何处理
                self.tmp[k] = q[i]
                k+=1; i+=1
            else:
                # self.res这里需要加上mid-i+1
                self.tmp[k] = q[j]
                k+=1; j+=1
                self.res +=mid-i+1
        while(i<=mid):
            self.tmp[k] = q[i]
            k+=1; i+=1
        while(j<=r):
            self.tmp[k] = q[j]
            k+=1; j+=1

        j = 0
        for i in range(l, r+1):
            q[i] = self.tmp[j]
            j+=1

if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    res = solution.nixushu(n, nums)
    print(res)