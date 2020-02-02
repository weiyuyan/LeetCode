#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/2
'''
给你一个整数数组 arr。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。
返回 至少 能删除数组中的一半整数的整数集合的最小大小。

示例 1：

输入：arr = [3,3,3,3,5,5,5,2,2,7]
输出：2
解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
示例 2：

输入：arr = [7,7,7,7,7,7]
输出：1
解释：我们只能选择集合 {7}，结果数组为空。
示例 3：

输入：arr = [1,9]
输出：1
示例 4：

输入：arr = [1000,1000,3,7]
输出：1
示例 5：

输入：arr = [1,2,3,4,5,6,7,8,9,10]
输出：5


提示：

1 <= arr.length <= 10^5
arr.length 为偶数
1 <= arr[i] <= 10^5
'''
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # 先排序
        arr.sort()
        # 再建立一个记录各元素数量的数组
        num_array = [1]
        # 设置一个flag，用来标记num_array的当前位置
        flag = 0

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                num_array[-1] += 1
            else:   # 新的数字
                num_array.append(1)

        num_array.sort(reverse=True)
        sum = 0
        for i in range(len(num_array)):
            sum += num_array[i]
            if sum >= len(arr) / 2:
                return i+1


if __name__ == '__main__':
    solution = Solution()
    res = solution.minSetSize([1,2,3,4,5,6,7,8,9,10])
    print(res)