#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/7
'''
给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。

示例 1：

输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
示例 2：

输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
示例 3：

输入：root = [1]
输出：0


提示：

每棵树最多有 50000 个节点。
每个节点的值在 [1, 100] 之间。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import functools
# 超时了
# class Solution:
#     def longestZigZag(self, root: TreeNode) -> int:
#         self.longest = 0
#         if not root: return 0
#         self.back_track(root, 0, 0)
#         self.back_track(root, 0, 1)
#         return self.longest
#     @functools.lru_cache(None)
#     def back_track(self, root: TreeNode, depth: int, left_or_right: int):
#         '''
#
#         :param root:
#         :param depth: 当前zigzag深度
#         :param left_or_right: 0是left，1是right
#         :return:
#         '''
#         if not root:
#             self.longest = max(self.longest, depth-1)
#             return
#
#         if left_or_right:   # 是1，说明上一层向右，所以这一层向左，然后置0
#             self.back_track(root.left, depth+1, 0)
#         else:
#             self.back_track(root.right, depth+1, 1)
#         self.back_track(root.left, 1, 0)
#         self.back_track(root.right, 1, 1)

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.maxx = 0

        def dfs(node, prev, depth):
            self.maxx = max(depth, self.maxx)
            if node.left:
                if prev == 0:  # 当前节点为左边，上一节点为左边，重新计数
                    dfs(node.left, 0, 1)
                else:  # 当前节点为左边，上一节点为右边，+1
                    dfs(node.left, 0, depth + 1)
            if node.right:
                if prev == 1:  # 当前节点为右边，上一节点也为右边，重新计数
                    dfs(node.right, 1, 1)
                else:  # 当前节点为右边，上一节点左边，+1
                    dfs(node.right, 1, depth + 1)

        dfs(root, 0, 0)
        return self.maxx


solution = Solution()
root = TreeNode(1)
root.left = None
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(1)
root.right.right.left.left = None
root.right.right.left.right = TreeNode(1)
root.right.right.left.left = None
root.right.right.left.right.left = None
root.right.right.left.right.right = TreeNode(1)
res = solution.longestZigZag(root)
print(res)