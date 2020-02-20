#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/20
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。


特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
还需要返回链表中的第一个节点的指针。

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。
'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def treeToDoublyList(self, root: Node) -> Node:
#         res = self.inOrder(root)
#         print(res)
#     # 中序遍历
#     def inOrder(self, root: Node):
#         if not root.left and not root.right: return [root, root]
#         if root.left and root.right:
#             lsides = self.inOrder(root.left)
#             rsides = self.inOrder(root.right)
#             lsides[1].right = root
#             root.left = lsides[1].right
#             rsides[0].left = root
#             root.right = rsides[0].left
#             return [lsides[0], rsides[1]]
#
#         if root.left:
#             lsides = self.inOrder(root.left)
#             lsides[1].right = root
#             root.left = lsides[1].right
#             return [lsides[0], root]
#
#         if root.right
#             rsides = self.inOrder(root.right)
#             rsides[0].left = root
#             root.right = rsides[0].left
#             return [root, rsides[1]]


class Solution(object):
    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.res = []
        self.pre_order(root)
        for i, node in enumerate(self.res[:-1]):
            node.right = self.res[i + 1]
            self.res[i + 1].left = node

        self.res[-1].right = self.res[0]
        self.res[0].left = self.res[-1]
        return self.res[0]

    def pre_order(self, root):
        if not root:
            return
        self.pre_order(root.left)
        self.res.append(root)
        self.pre_order(root.right)

solution = Solution()
solution.treeToDoublyList()