#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/20
'''
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Codec:  # 层序遍历

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        out = ""

        if not root:
            return "[]"

        queue = [root]
        while 1:
            if len(queue) == 0:
                break
            temp = queue.pop(0)

            if not temp:
                out += "null,"
                continue
            else:
                out += (str(temp.val) + ",")
                queue.append(temp.left)
                queue.append(temp.right)

        out = out[:-1]
        # print(out)
        # return "[" + out + "]"
        return out

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        point = data.split(',')
        # print(point)
        stack = []
        new = TreeNode(int(point.pop(0)))
        stack = [new]
        while len(stack) != 0:
            now = stack.pop(0)
            # print(now)
            if not now:
                continue
            try:
                left = TreeNode(int(point.pop(0)))
            except:
                left = None
            try:
                right = TreeNode(int(point.pop(0)))
            except:
                right = None
            stack.append(left)
            stack.append(right)
            now.left = left
            now.right = right

        return new
'''


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        else:
            data = ''
            data += str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if (len(data) < 3): return None
        data_l = data.split(' ')[::-1]

        # 重构二叉树
        def func():
            if not data_l:
                return None
            # 遇到'#'说明该节点为空
            if data_l[-1] == '#':
                data_l.pop()
                return None
            # 前序第一个数为头节点
            head = TreeNode(int(data_l[-1]))
            data_l.pop()
            # 接下来是左子树
            head.left = func()
            # 左子树完成右子树
            head.right = func()
            return head

        return func()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))