#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/21
'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 1000
0 <= arr[i] <= 1000
通过次数1,639提交次数2,726
'''
from typing import List
import random
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k<=0 or k>len(arr): return []
        start = 0
        end = len(arr)-1
        index = self.Partition(arr, len(arr), start, end)
        while index != k-1:
            if index > k-1:
                end = index-1
                index = self.Partition(arr, len(arr), start, end)
            else:
                start = index+1
                index = self.Partition(arr, len(arr), start, end)
        return arr[:k]

    def Partition(self, data: List[int], length: int, start: int,  end: int):
        if not data or length<=0 or start<0 or end>=length: return False

        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]
        small = start - 1
        for index in range(start, end):
            if data[index] < data[end]:
                small += 1
                if small != index:
                    data[index], data[small] = data[small], data[index]
        small += 1
        data[small], data[end] = data[end], data[small]
        return small