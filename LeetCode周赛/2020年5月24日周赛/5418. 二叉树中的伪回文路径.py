#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/5/24
'''
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。



示例 1：



输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
示例 2：



输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
示例 3：

输入：root = [9]
输出：1


提示：

给定二叉树的节点数目在 1 到 10^5 之间。
节点值在 1 到 9 之间。
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def pseudoPalindromicPaths(self, root: TreeNode) -> int:
#         self.res = 0
#         nodelist = [0 for _ in range(10)]
#         self.back_track(root, nodelist)
#         return self.res
#
#     def back_track(self, root: TreeNode, nodelist: List):
#         if not root: return
#         if not root.left and not root.right:
#             nodelist[root.val] -= 1
#             if sum(nodelist) == 0 or sum(nodelist) == 1 or sum(nodelist) == -1:
#                 self.res += 1
#                 nodelist[root.val] += 1
#                 return
#             else:
#                 nodelist[root.val] += 1
#                 return
#         else:
#             nodelist[root.val] = (nodelist[root.val]+1)%2
#             self.back_track(root.left, nodelist)
#             self.back_track(root.right, nodelist)
#             return

# class Solution:
#     def pseudoPalindromicPaths (self, root: TreeNode) -> int:
#         self.res=[]
#
#         self.dfs(root, [])
#         count=0
#         for num in self.res:
#             hash={}
#             for i in num:
#                 if i not in hash:
#                     hash[i]=1
#             else:
#                 hash[i]+=1
#                 ans=0
#             for i in hash:
#                 if hash[i]%2==1:
#                     ans+=1
#                 if ans==0 or ans==1:
#                     count+=1
#
#         return count
#
#     def dfs(self, root, path):
#         if not root.left and not root.right:
#             self.res.append(path + [root.val])
#         if root.left:
#             self.dfs(root.left, path + [root.val])
#         if root.right:
#             self.dfs(root.right, path + [root.val])
#         if not root:
#             return 0

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0

        # 把集合移入和移出操作提取出来, 简化代码
        def changeset(oddsets, v):
            if v in oddsets:
                oddsets.remove(v)
            else:
                oddsets.add(v)

        def dfs(node, oddsets):
            if not node.left and not node.right:
                # 叶子节点, 且奇数个数的元素数目不大于1就是满足条件的路径
                if len(oddsets) <= 1:
                    self.res += 1
                return
            if node.left:
                # 注意每次改变集合状态后, 在dfs遍历完要恢复成原始状态, 避免对后面的遍历产生影响, 下同
                changeset(oddsets, node.left.val)
                dfs(node.left, oddsets)
                changeset(oddsets, node.left.val)
            if node.right:
                changeset(oddsets, node.right.val)
                dfs(node.right, oddsets)
                changeset(oddsets, node.right.val)

        dfs(root, {root.val})
        return self.res

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.res = 0
        if not root: return 0

        self.dfs(root, {root.val})
        return self.res

    def dfs(self, root: TreeNode, oddsets: set):
        if not root.left and not root.right:
            if len(oddsets) <= 1:
                self.res += 1
            return

        if root.left:
            self.changeset(oddsets, root.left.val)
            self.dfs(root.left, oddsets)
            self.changeset(oddsets, root.left.val)

        if root.right:
            self.changeset(oddsets, root.right.val)
            self.dfs(root.right, oddsets)
            self.changeset(oddsets, root.right.val)

    def changeset(self, oddsets: set, v: int):
        if v in oddsets:
            oddsets.remove(v)
        else:
            oddsets.add(v)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(8)
    root.left = TreeNode(8)
    root.left.left = TreeNode(7)
    root.right = TreeNode(7)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(7)
    res = solution.pseudoPalindromicPaths(root)
    print(res)
