#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

提示：

节点总数 <= 10000
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法：递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = self.back_track(root)
        return res

    def back_track(self, root):
        if not root.left and not root.right: return 1
        if not root.left and root.right: return 1+self.back_track(root.right)
        if not root.right and root.left: return 1+self.back_track(root.left)
        if root.left and root.right: return 1+max(self.back_track(root.left), self.back_track(root.right))

solution = Solution()
