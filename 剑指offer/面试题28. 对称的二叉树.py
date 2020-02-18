#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        return self.is_Symmetrical(root, root)

    def is_Symmetrical(self, root1: TreeNode, root2: TreeNode):

        # 全为空，自然返回True
        if not root1 and not root2: return True

        # 一个为空，另一个不为空，返回False
        if not root1 or not root2: return False

        # 两个节点的值不相同，返回False
        if root1.val != root2.val: return False

        # 全不为空
        # root1 按照 根-左-右 的先序遍历来， root2按照 根-右-左 的对称先序遍历来
        return self.is_Symmetrical(root1.left, root2.right) and self.is_Symmetrical(root1.right, root2.left)
