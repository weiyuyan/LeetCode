#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/19
'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        assist_list = []
        res = []
        if root:    # 如果非空
            assist_list.append(root)
        while assist_list:
            tmp_node = assist_list.pop(0)
            res.append(tmp_node.val)
            assist_list.append(tmp_node.left) if tmp_node.left else None
            assist_list.append(tmp_node.right) if tmp_node.right else None

        return res

solution = Solution()
root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

res = solution.levelOrder(root)
print(res)