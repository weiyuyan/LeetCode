#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/15
'''
给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

如果有多种构造方法，请你返回任意一种。



示例：



输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。


提示：

树节点的数目在 1 到 10^4 之间。
树节点的值互不相同，且在 1 到 10^5 之间。
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 将二叉搜索树变成序列
        self.alist = []
        self.getList(root)

        # 将序列变成二叉平衡树
        ans = self.getBalanceTree(0, len(self.alist)-1)
        return ans


    def getList(self, root: TreeNode):
        # 将二叉搜索树变成序列
        if not root: return
        self.getList(root.left)
        self.alist.append(root.val)
        self.getList(root.right)

    def getBalanceTree(self, l, r):
        if l==r:
            return TreeNode(self.alist[l])
        elif l+1==r:
            tmp = TreeNode(self.alist[l])
            tmp.right = TreeNode(self.alist[r])
            return tmp

        mid = (l+r)//2
        ans = TreeNode(self.alist[mid])
        ans.left = self.getBalanceTree(l, mid-1)
        ans.right = self.getBalanceTree(mid+1, r)
        return ans