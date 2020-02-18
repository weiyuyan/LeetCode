#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/19
'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        current_layer_last = 0  # 当前层剩余节点
        next_layer_last = 0 # 下一层剩余节点
        current_layer = 0   # 当前层

        assist_list = []
        res = [[]]
        if root:  # 如果非空
            assist_list.append(root)
            current_layer_last = 1

        while assist_list:
            tmp_node = assist_list.pop(0)
            res[current_layer].append(tmp_node.val)
            current_layer_last -= 1

            if tmp_node.left:
                assist_list.append(tmp_node.left)
                next_layer_last += 1
            if tmp_node.right:
                assist_list.append(tmp_node.right)
                next_layer_last += 1

            if current_layer_last == 0: # 当前层遍历完了
                current_layer_last, next_layer_last = next_layer_last, 0    # 重置计数
                current_layer += 1  # 进入下一层
                res.append([])  # 构建一层，以防出现list index out of range

        return res[:-1] # 由于最后肯定会出现一个空层，所以过滤掉

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