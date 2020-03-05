#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法：对于二叉排序树，使用中序遍历
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        if not root: return None
        target = self.inOrder(root, k)
        return target.val

    def inOrder(self, root: TreeNode, k: int):
        # if times == self.k: return root.val
        # if not root.left and not root.right: return
        # self.inOrder(root.left, times+1)
        # self.inOrder(root.right, times+1)
        target = TreeNode(-1)
        if root.left:
            target = self.inOrder(root.left, k)
        if not target:
            if k==1: target=root
            k-=1
        if not target and root.right:
            target = self.inOrder(root.right, k)
        return target