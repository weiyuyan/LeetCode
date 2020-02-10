#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/28
'''
输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树。

注意:

二叉树中每个节点的值都互不相同；
输入的前序遍历和中序遍历一定合法；
样例
给定：
前序遍历是：[3, 9, 20, 15, 7]
中序遍历是：[9, 3, 15, 20, 7]

返回：[3, 9, 20, null, null, 15, 7, null, null, null, null]
返回的二叉树如下所示：
    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 我们先根据前序遍历的第一个数字创建根节点，接下来在中序遍历序列中找到根节点的位置
    # 这句就能确定左右子树节点的位置
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
