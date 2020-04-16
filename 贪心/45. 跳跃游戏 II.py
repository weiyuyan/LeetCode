#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/15
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

通过次数39,256提交次数116,525

'''
# 解：另一种贪心hhh
# 如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
# 11. 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。
#
# 如果从这个 起跳点 起跳叫做第 1 次 跳跃，那么从后面 3 个格子起跳 都 可以叫做第 2 次 跳跃。
#
# 所以，当一次 跳跃 结束时，从下一个格子开始，到现在 能跳到最远的距离，都 是下一次 跳跃 的 起跳点。
# 31. 对每一次 跳跃 用 for 循环来模拟。
# 32. 跳完一次之后，更新下一次 起跳点 的范围。
# 33. 在新的范围内跳，更新 能跳到最远的距离。
#
# 记录 跳跃 次数，如果跳到了终点，就得到了结果。
#
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_range = [0, 0]
        res = 0

        while jump_range[1]<len(nums)-1:

            # 形如[3,2,1,0,4]这样的数据，永远跳不出去，所以return0
            if jump_range[0] >= jump_range[1] and nums[jump_range[0]]==0: return 0
            max_jump = 0
            for i in range(jump_range[0], jump_range[1]+1):
                max_jump = max(max_jump, nums[i]+i)
            jump_range[0] = jump_range[1]
            jump_range[1] = max_jump
            res += 1

        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,0,4]
    res = solution.jump(nums)
    print(res)