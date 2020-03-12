#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：

任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。

示例 1：

输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。
示例 2：

输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。
示例 3：

输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。
示例 4：

输入：root = [2,1,3]
输出：6
示例 5：

输入：root = [5,4,8,3,null,6,3]
输出：7

提示：

每棵树最多有 40000 个节点。
每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 二叉树的搜索，采用中序遍历
    def maxSumBST(self, root: TreeNode) -> int:
        self.val_max = 0
        self.res = []
        self.inOrder(root.left, [], 0)
        self.inOrder(root.right, [], 0)
        return self.val_max

    def inOrder(self, root: TreeNode, a_list, tmp_val):
        a_list.append(root)
        tmp_val += root.val
        if root.left and root.val>root.left.val:
            self.inOrder(root.left, a_list, tmp_val)

        if root.right and root.val<root.right.val:
            self.inOrder(root.right, a_list, tmp_val)

        if tmp_val > self.val_max:
            self.val_max = tmp_val
        return tmp_val



a = TreeNode(1)
a.left = TreeNode(4)
a.right = TreeNode(3)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)

a.right.left = TreeNode(2)
a.right.right= TreeNode(5)
a.right.right.left = TreeNode(4)
a.right.right.right = TreeNode(6)
solution = Solution()
res = solution.maxSumBST(a)
print(res)
