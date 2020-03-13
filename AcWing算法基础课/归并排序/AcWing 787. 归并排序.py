#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/12
from typing import List
class Solution:
    def k_number(self, alist: List[int], k: int):
        # 归并排序需要用到的临时数组tmp
        self.tmp=[0]*10000000
        self.merge_sort(alist, 0, len(alist)-1)
        for num in alist:
            print(num, end=' ')

    def merge_sort(self, q, l, r):
        if l>=r: return
        mid = (l+r)//2
        self.merge_sort(q, l, mid)
        self.merge_sort(q, mid+1, r)

        k, i, j = 0, l, mid+1
        while(i<=mid and j<=r):
            if q[i]<=q[j]:
                self.tmp[k] = q[i]
                k+=1; i+=1
            else:
                self.tmp[k] = q[j]
                k+=1; j+=1
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
    def merge_sort(self, q, l, r):
        if l>=r: return
        mid = (l+r)//2
        self.merge_sort(q, l, mid)
        self.merge_sort(q, mid+1, r)

        k, i, j = 0, l, mid+1
        while(i<=mid and j<=r):
            if q[i]<=q[j]:
                self.tmp[k] = q[i]
                k+=1; i+=1
            else:
                self.tmp[k] = q[j]
                k+=1; j+=1
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
    def merge_sort(self, q, l, r):
        if l>=r: return
        mid = (l+r)//2
        self.merge_sort(q, l, mid)
        self.merge_sort(q, mid+1, r)

        k, i, j = 0, l, mid+1
        while(i<=mid and j<=r):
            if q[i]<=q[j]:
                self.tmp[k] = q[i]
                k+=1; i+=1
            else:
                self.tmp[k] = q[j]
                k+=1; j+=1
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
    nums = list(map(int, input().split(' ')))
    solution.k_number(nums, n-1)