#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/19
'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/

'''
# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []  # 特殊值

        self.res = []   # res纪录所有符合条件的路径（只纪录数值）
        self.target_sum = sum
        self.Preorder(root, root.val, [root.val])

        return self.res

    def Preorder(self, root: TreeNode, cur_sum: int, footprint: List[int]): # 先序遍历
        '''
        :param root: 当前子树的根节点
        :param cur_sum: 从根节点到当前子树根节点（包括根节点）的值的和
        :param footprint: 走过的路径(包括根节点)
        :return:
        '''
        if cur_sum == self.target_sum and not root.left and not root.right: # 看清题目，是从根节点到所有叶子节点！！ 叶子！！
            self.res.append(footprint[:])

        # 先序遍历开始
        if root.left:
            cur_sum += root.left.val
            footprint.append(root.left.val)
            self.Preorder(root.left, cur_sum, footprint)
            cur_sum -= root.left.val
            footprint.pop()

        if root.right:
            cur_sum += root.right.val
            footprint.append(root.right.val)
            self.Preorder(root.right, cur_sum, footprint)
            cur_sum -= root.right.val
            footprint.pop()
        return

pass
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         res = []
#         if not root: return []
#
#         def helper(root, sum, tmp):
#             if not root:
#                 return
#             if not root.left and not root.right and sum - root.val == 0:
#                 tmp += [root.val]
#                 res.append(tmp)
#                 return
#             helper(root.left, sum - root.val, tmp + [root.val])
#             helper(root.right, sum - root.val, tmp + [root.val])
#
#         helper(root, sum, [])
#         return res

solution = Solution()
root = TreeNode(1)
A = TreeNode(2)
# root = TreeNode(5)
# A = TreeNode(4)
# B = TreeNode(8)
# C = TreeNode(11)
# D = TreeNode(13)
# E = TreeNode(4)
# F = TreeNode(7)
# G = TreeNode(2)
# H = TreeNode(5)
# I = TreeNode(1)
root.left = A
# root.right = B
# A.left = C
# C.left = F
# C.right = G
# B.left = D
# B.right = E
# E.left = H
# E.right = I
res = solution.pathSum(root, 1)
print(res)
