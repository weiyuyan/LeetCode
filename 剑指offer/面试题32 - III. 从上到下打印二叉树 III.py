#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/19
'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]
 

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
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         current_layer_last = 0  # 当前层剩余节点
#         next_layer_last = 0 # 下一层剩余节点
#         current_layer = 0   # 当前层
#
#         assist_list = []
#         res = [[]]
#         if root:  # 如果非空
#             assist_list.append(root)
#             current_layer_last = 1
#
#         switch = 0
#
#         while assist_list:
#             if switch == 0:
#                 tmp_node = assist_list.pop(-1)
#                 res[current_layer].append(tmp_node.val)
#                 current_layer_last -= 1
#                 if tmp_node.right:
#                     assist_list.append(tmp_node.right)
#                     next_layer_last += 1
#                 if tmp_node.left:
#                     assist_list.append(tmp_node.left)
#                     next_layer_last += 1
#
#                 if current_layer_last == 0:  # 当前层遍历完了
#                     current_layer_last, next_layer_last = next_layer_last, 0  # 重置计数
#                     current_layer += 1  # 进入下一层
#                     switch = 1 if switch == 0 else 0  # switch由0到1切换
#                     res.append([])  # 构建一层，以防出现list index out of range
#
#             elif switch == 1:
#                 tmp_node = assist_list.pop(0)
#                 res[current_layer].append(tmp_node.val)
#                 current_layer_last -= 1
#                 if tmp_node.left:
#                     assist_list.append(tmp_node.left)
#                     next_layer_last += 1
#                 if tmp_node.right:
#                     assist_list.append(tmp_node.right)
#                     next_layer_last += 1
#
#                 if current_layer_last == 0:  # 当前层遍历完了
#                     current_layer_last, next_layer_last = next_layer_last, 0  # 重置计数
#                     current_layer += 1  # 进入下一层
#                     switch = 1 if switch == 0 else 0    # switch由0到1切换
#                     res.append([])  # 构建一层，以防出现list index out of range
#
#         return res[:-1] # 由于最后肯定会出现一个空层，所以过滤掉

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)

            # if level == len(res):
            #     res.append(deque([]))
            ##append操作，偶数行从左到右；奇数行从右到左
            # if level % 2 == 0:
            #     res[level].append(node.val)
            # else:
            #     res[level].appendleft(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        return res


solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

res = solution.levelOrder(root)
print(res)