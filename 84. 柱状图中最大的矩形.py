#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/4
'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。


以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。


图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

'''
from typing import List
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         all_max = 0
#         for i in range(len(heights)):
#             tmp_high = heights[i]   # 当前最优柱状矩形的高
#             tmp_max = heights[i]    # 当前最优柱状矩形的面积
#             j = i+1
#             while(j<len(heights) and ((heights[j]>=tmp_high) or (heights[j]-(j-i)*(tmp_high-heights[j]))>=0) ): # 可以继续往后走
#                 # tmp_max += tmp_high if heights[j]>=tmp_high else heights[j]-(j-i)*(tmp_high-heights[j])  # 如果新柱高度>=tmp_hith，面积增加tmp_high，否则，增加0
#                 tmp_high = min(tmp_high, heights[j])
#                 tmp_max = (j-i+1) * tmp_high
#                 j += 1
#
#             if tmp_max > all_max:
#                 all_max = tmp_max
#         return all_max

pass

# 暴力法，无法通过，时间复杂度O(n^3)，空间复杂度O(1)
# 这个超时了
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxmun = 0
#         for i in range(len(heights)):
#             for j in range(i, len(heights)):
#                 s = (j-i+1) * min(heights[i: j+1])
#                 maxmun = max(maxmun, s)
#         return maxmun

pass
# 中心扩展法，时间复杂度O(n^2)，空间复杂度O(1)
# class Solution:
#     def largestRectangleArea(self, heights: [int]) -> int:
#         sum = 0
#         for i in range(len(heights)):
#             s = heights[i]
#             left = right = 1
#             while(left or right):
#                 if (i-left>=0 and heights[i-left]>=heights[i] and left):
#                     left += 1
#                     s += heights[i]
#                 else:
#                     left = 0
#                 if (i+right<len(heights) and heights[i+right]>=heights[i] and right):
#                     right += 1
#                     s += heights[i]
#                 else:
#                     right = 0
#             sum = max(sum, s)
#         return sum

pass
# 中心扩展法，时间复杂度O(n^2)，空间复杂度O(1) (别人写的，比我简洁些)
# 然鹅还是超时了！！！
# class Solution:
#     def largestRectangleArea(self, heights: [int]) -> int:
#         maxmun = 0
#
#         for i in range(len(heights)):
#             left, right = i, i
#             while left > 0 and heights[left - 1] >= heights[i]:
#                 left -= 1
#             while right < len(heights) - 1 and heights[right + 1] >= heights[i]:
#                 right += 1
#
#             s = (right - left + 1) * heights[i]
#             maxmun = max(maxmun, s)
#
#         return maxmun

pass

# 网友的解法，用到了单调栈，妈的
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, heights[tmp]*(i-stack[-1]-1))
            stack.append(i)
        return res

solution = Solution()
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
res = solution.largestRectangleArea(a_list)
print(res)