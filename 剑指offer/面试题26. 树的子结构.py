#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/17
'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result = False
        if not A or not B: return result    # 如果是空的话
        result = self.Does_Tree1_Have_Tree2(A, B)
        if not result:
            result = self.isSubStructure(A.left, B)
        if not result:
            result = self.isSubStructure(A.right, B)

        return result

    def Does_Tree1_Have_Tree2(self, Tree1: TreeNode, Tree2: TreeNode) -> bool:
        if not Tree2: return True   # Tree2空了，返回True
        if not Tree1: return False  # Tree2没空，Tree1空了，返回False
        if Tree1.val != Tree2.val: return False     # Tree1和Tree2当前根节点值不同，返回False

        result = self.Does_Tree1_Have_Tree2(Tree1.left, Tree2.left) and self.Does_Tree1_Have_Tree2(Tree1.right, Tree2.right)
        return result

a = 0.019
b = 0.019000000000000001
print(id(a))
print(id(b))
print(a == b)