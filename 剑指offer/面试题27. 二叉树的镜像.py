#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
'''
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 思路： 前序遍历二叉树，如果该节点有子节点，交换它的两个子节点，当交换完所有的叶子节点后，就得到了树的影像
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 前序遍历二叉树
        if not root: return None   # 如果是空节点
        # if root.left or root.right:  # 如果不是叶子节点，那就换
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root  # 是叶子节点



tree_node = TreeNode(0)
tree_node.left = TreeNode(1)
tree_node.right = TreeNode(2)
solution = Solution()
new_node = solution.mirrorTree(tree_node)
print(new_node)