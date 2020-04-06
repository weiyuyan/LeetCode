#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/3
'''
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''
from typing import List
# 第一种方法：直接拼接到A的尾部然后使用sort()方法排序
# class Solution:
#     def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
#         """
#         Do not return anything, modify A in-place instead.
#         """
#         A[m:] = B
#         A.sort()
pass
# 第二种方法，使用额外数组空间
# class Solution:
#     def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
#         """
#         Do not return anything, modify A in-place instead.
#         """
#         if not A or not B: return
#         sorted = []
#         pa=pb=0
#         while pa<=m and pb<=n:
#             if pa==m: sorted[pa+pb:]=B[pb:]; break
#             if pb==n: sorted[pa+pb:]=A[pa:m]; break
#             if A[pa]<=B[pb]: sorted.append(A[pa]); pa+=1
#             else: sorted.append(B[pb]); pb+=1
#         A[:] = sorted
pass
# 第三种方法，利用A后面的额外空间，从大到小倒序排列
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        tail= m+n-1
        pa, pb = m-1, n-1
        while pa>=0 or pb>=0:
            if pa==-1:
                A[tail]=B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1






A = [1,2,3,0,0,0]; m = 3
B = [2,5,6];       n = 3
# A = [2, 0]; m = 1
# B = [1];       n = 1
solution = Solution()
solution.merge(A, m, B, n)
print(A)