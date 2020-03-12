#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''
# 注意：这里已经不再是二叉搜索树了

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 利用辅助内存
        self.FLAG = False
        self.Path = []
        self.findPath(root, p, [])
        p_path = self.Path

        self.FLAG = False
        self.Path = []
        self.findPath(root, q, [])
        q_path = self.Path

        res = p_path[0]
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                res = p_path[i]
            else:
                break
        return res

    def findPath(self, root: TreeNode, node: TreeNode, cur_path: List[TreeNode]):
        if self.FLAG: return    # 如果FLAG为True，那么不找了
        if not root: return

        cur_path.append(root)

        if root.val == node.val:
            self.FLAG = True    # 找到了，FLAG设为True
            self.Path = cur_path[:]
            return

        self.findPath(root.left, node, cur_path)
        self.findPath(root.right, node, cur_path)
        cur_path.pop()
        return


a = TreeNode(3)
a.left = TreeNode(5)
a.right = TreeNode(1)
a.left.left = TreeNode(6)
a.left.right = TreeNode(2)
a.right.left = TreeNode(0)
a.right.right = TreeNode(8)

a.left.right.left = TreeNode(7)
a.left.right.right = TreeNode(4)

b = a.left
c = a.left.right.right
solution = Solution()
res = solution.lowestCommonAncestor(a, b, c)
print(res.val)