#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/11
'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。


示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

提示：

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
'''
from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        all_sum = sum(A)
        if all_sum%3 != 0:
            return False

        tmp_sum = 0
        time = 0
        for i in range(len(A)):
            tmp_sum += A[i]
            if tmp_sum == all_sum/3:
                tmp_sum=0
                time+=1


        if all_sum==0 and time>=3: return True
        if tmp_sum==0 and time==3: return True
        return False

solution = Solution()
A = [12,-4,16,-5,9,-3,3,8,0]
res = solution.canThreePartsEqualSum(A)
print(res)