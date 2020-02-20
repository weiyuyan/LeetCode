#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/19

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000
'''
from typing import List

'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return True  # postorder为空的话返回False
        begin = 0
        end = len(postorder)-1
        res = self.back_track(begin, end, postorder)
        return res
    def back_track(self, begin: int, end: int, postorder: List[int]) -> bool:
        if begin >= end: return True    # 遍历到最后一位了，返回True
        if not self.judge(begin, end, postorder): return False  # 如果不合法，返回False

        root = postorder[end]   # 当前树/子树的根节点是root
        for i in range(begin, end):
            if postorder[i] > root: break   # 找到比当前root值大的数字，这个是右子树的开头

        # 现在，begin——i-1是左子树，i——end是右子树
        return self.back_track(begin, i, postorder) and self.back_track(i+1, end-1, postorder)


    def judge(self, begin: int, end: int, postorder: List[int]) -> bool:
        if begin>end: return False

        # 如果子树从begin开始就大于root(postorder[end])的话，后面如果还有小于等于root的情况就算False。
        # 如[5, 2, -17, -11]就不合规矩
        # 如果后面全是大于root的话，就符合规矩，返回True
        if postorder[begin] > postorder[end]:
            if min(postorder[begin: end]) <= postorder[end]: return False
            else: return True

        # 另一种情况，从begin开始是小于等于root的，但是在出现了第一个大于root值之后，仍然出现了小于等于root的情况
        # 那就不合规矩，返回False，否则的话就符合规矩，返回True
        flag = 0
        for i in range(begin, end):
            if postorder[i] > postorder[end]: flag = 1
            if flag and postorder[i] <= postorder[end]: return False # 不合规矩，返回False

        return True
'''


# 这个写法更好
class Solution(object):
    def verifyPostorder(self, sequence):
        if not sequence: return True
        return self.helper(sequence)

    def helper(self, sequence):
        if len(sequence) <= 1: return True
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        return self.helper(sequence[:i]) and self.helper(sequence[i:-1])





if __name__ == '__main__':
    a_list = [5, 2, -17, -11, 25, 76, 62, 98, 92, 61]

    # solution = Solution()
    # res = solution.verifyPostorder(a_list)
