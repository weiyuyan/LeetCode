#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/8
'''
我们有两个长度相等且不为空的整型数组 A 和 B 。

我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。

在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。

给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。

示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
注意:

A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。
'''
from typing import List
class Solution(object):
    # def minSwap(self, A, B):
    #     n1, s1 = 0, 1
    #     for i in range(1, len(A)):
    #         n2 = s2 = float("inf")
    #         if A[i-1] < A[i] and B[i-1] < B[i]:
    #             n2 = min(n2, n1)
    #             s2 = min(s2, s1 + 1)
    #         if A[i-1] < B[i] and B[i-1] < A[i]:
    #             n2 = min(n2, s1)
    #             s2 = min(s2, n1 + 1)
    #
    #         n1, s1 = n2, s2
    #
    #     return min(n1, s1)

    def minSwap(self, A, B):
        n1, s1 =  0, 1
        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1+1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1+1)
            n1, s1 = n2, s2

        return min(n1, s1)
