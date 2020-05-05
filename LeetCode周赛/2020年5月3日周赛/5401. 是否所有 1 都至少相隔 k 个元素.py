#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/5/3
'''
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。



示例 1：



输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。
示例 2：



输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。
示例 3：

输入：nums = [1,1,1,1,1], k = 0
输出：true
示例 4：

输入：nums = [0,1,0,1], k = 1
输出：true


提示：

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] 的值为 0 或 1
'''
from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        tmp_pos = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp_pos = i
                break

        for i in range(tmp_pos+1, len(nums)):
            if nums[i] == 1:
                if i-tmp_pos-1 >= k:
                    tmp_pos = i
                    continue
                else:
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,1]
    k = 1
    res = solution.kLengthApart(nums, k)
    print(res)
