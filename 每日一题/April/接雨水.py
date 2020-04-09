#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/8
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
通过次数87,247提交次数172,928

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    # 一：暴力法
    # 对于每一根柱子i，依次找他的左边和右边的最高值max_left、max_right，res += min(max_left, max_right) - height[i]
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) <= 2: return 0
        for i in range(1, len(height)):
            max_left, max_right = 0, 0
            for left in range(i):
                max_left = max(height[left], max_left)
            for right in range(i + 1, len(height)):
                max_right = max(height[right], max_right)

            res += (min(max_left, max_right) - height[i]) if (height[i] < min(max_left, max_right)) else 0

        return res

    # 二：动态规划
    # 上一个方法超时了，所以使用动态规划
    # 在暴力方法中，我们仅仅为了找到最大值每次都要向左和向右扫描一次。
    # 但是我们可以提前存储这个值。因此，可以通过动态编程解决。
    # 状态表示：dp[i][0]表示第i个数左边的最大值 dp[i][1]表示第i个数右边的最大值
    # 状态计算：dp[i][0] = max(dp[i-1][0], height[i]), dp[i][1] = max(dp[i+1], height[i])
    # 时间复杂度：o(n)
    # 空间复杂度：o(n)
    def trap(self, height: List[int]) -> int:
        res = 0
        dp = [[0, 0] for _ in range(len(height)+2)]
        for i in range(1, len(dp)-1):
            dp[i][0] = max(dp[i-1][0], height[i-1])
        for j in range(len(dp)-2, 0, -1):
            dp[j][1] = max(dp[j+1][1], height[j-1])

        dp.pop(0)
        dp.pop()
        res = 0
        if len(height) <= 2: return 0
        for i in range(1, len(height)):
            max_left, max_right = dp[i][0], dp[i][1]
            res += (min(max_left, max_right) - height[i]) if (height[i] < min(max_left, max_right)) else 0
        return res


    # 三：双指针法：
    # 和方法 2 相比，我们不从左和从右分开计算，我们想办法一次完成遍历。
    # 从动态编程方法的示意图中我们注意到，只要 right_max[i]>left_max[i] （元素 0 到元素 6），
    # 积水高度将由 left_max 决定，类似地 left_max[i]>right_max[i]（元素 8 到元素 11）。
    # 所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）。
    # 当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）。
    # 我们必须在遍历时维护 left_max 和 right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成。
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        while(left<right):
            if height[left]<height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max-height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max-height[right]
                right -= 1

        return res
    # 四：单调栈
    # 产生凹陷的地方才能存储雨水，那么高度一定是先减后增，所以思路就是维护一个高度递减的 stack
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length<3: return 0
        res, idx = 0, 0
        stack = [0]
        for idx in range(1, length):
            if height[idx]>height[stack[-1]]:
                while stack and height[idx]>height[stack[-1]]:
                    top = stack.pop()
                    if stack:
                        h = min(height[stack[-1]], height[idx]) - height[top]
                        dist = idx - stack[-1] - 1
                        res += h*dist
            stack.append(idx)
        return res


if __name__ == '__main__':
    solution = Solution()
    height = [2,1,0,2]
    res = solution.trap(height)
    print(res)