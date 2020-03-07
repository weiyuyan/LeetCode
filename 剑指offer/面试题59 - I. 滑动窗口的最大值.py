#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
'''
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        temp0 = float('-inf')  # 负穷大
        temp = temp0
        for i in range(len(nums)):
            temp = max(temp, nums[i])  # 窗口的最后一个值与前缀最大值比较
            if i > k - 2:  # 判断到达窗口长度
                res.append(temp)
                if temp <= nums[i - k + 1]:  # 如果即将滑出窗口的值可能是最大值，重新计算下个窗口前缀temp的值
                    temp = temp0
                    for j in range(k - 1):
                        temp = max(temp, nums[i - j])
        return res


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = deque(), list()

        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                # 如果最大值在当前滑动窗口之外，去掉它
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                # 将小于当前元素的，全部从队列中推出
                queue.pop()

            queue.append(i)  # 将当前元素加入队列
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = deque(), list()

        for i in range(len(nums)):
            if queue and queue[0] == i-k:
                # 最大值在滑动窗口之外
                queue.popleft()
            while queue and nums[queue[-1]]<nums[i]:
                # 将小于当前元素的，全部从队列中推出
                queue.pop()

            queue.append(i) # 将当前元素加入队列
            if i>=k-1:
                result.append(queue[0])
        return result

a = list()
print(a)
a = list
print(a)

