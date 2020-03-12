#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 
提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
'''
# 构造前缀树
class Solution:
    def constructArr(self, A):
        if not A:
            return []
        prefix = [1]*len(A)
        prefix[0]=1
        for i in range(1,len(A)):
            prefix[i] = prefix[i-1]*A[i-1]
        cur_suffix = 1
        for i in range(len(A)-1,-1,-1):
            prefix[i] = prefix[i] * cur_suffix
            cur_suffix *= A[i]
        return prefix

# 方法二
from typing import List
class Solution:
    # 将数组分为两部分数组C和D
    # C[i] = A[0]*A[1]*...*A[i-1]
    # D[i] = A[i+1]*A[i+2]*...*A[n-1]
    # C[i]可以用自上到下的方法算出来，即C[i] = C[i-1]*A[i-1]
    # D[i]可以用自下到上的方法算出来，即D[i] = D[i+1]*A[i+1]
    def constructArr(self, a: List[int]) -> List[int]:
        C, D = [1]*len(a), [1]*len(a)
        res = []
        for i in range(1, len(a)):
            C[i] = C[i-1]*a[i-1]

        for j in range(len(a)-2, -1, -1):
            D[j] = D[j+1]*a[j+1]

        for k in range(len(a)):
            res.append(C[k]*D[k])

        return res

solution = Solution()
array = [1, 2]
res = solution.constructArr(array)
print(res)