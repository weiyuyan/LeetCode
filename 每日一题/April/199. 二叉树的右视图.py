#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/22
'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
通过次数37,189提交次数58,398
'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 思路：按照左->根->右的顺序遍历，然后设置一个数组floor，用来纪录每一层的代表节点，然后不断更新floor数组
        self.floor = [float('inf')] * 10000
        self.preView(0, root)
        res = []
        for i in range(len(self.floor)):
            if self.floor[i] != float('inf'):
                res.append(self.floor[i])
            else:
                break
        return res

    def preView(self, cur_floor: int, root: TreeNode):
        # cur_floor是当前层数
        # 顺序：左中右
        if not root: return
        self.preView(cur_floor+1, root.left)
        self.floor[cur_floor] = root.val
        self.preView(cur_floor+1, root.right)
        return

if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.right = TreeNode(5)
    a.right.right = TreeNode(4)
    solution = Solution()
    res = solution.rightSideView(a)
    print(res)