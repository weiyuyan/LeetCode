#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/17
'''
实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5

'''

# 解法一
# 这道题可以用前缀树trie的思路来解决
import collections
# class MapSum:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = {}
#         self.p = collections.defaultdict(set)
#
#     def insert(self, key: str, val: int) -> None:
#         self.d[key] = val
#         for i in range(len(key)):
#             self.p[key[: i+1]].add(key)
#
#     def sum(self, prefix: str) -> int:
#         return sum(self.d[key] for key in self.p[prefix])
pass

# 解法二
# 利用系统前缀判断函数startswith()，在字典里搜索对应的单词并求和，最简单直接，效率也可，但是存值没有多余空间。
import collections
# class MapSum:
#     def __init__(self):
#         self.d = {}
#
#     def insert(self, key: str, val: int) -> None:
#         self.d[key] = val
#
#     def sum(self, prefix: str) -> int:
#         return sum(self.d[s] for s in self.d if s.startswith(prefix))

# Your MapSum object will be instantiated and called as such:

# 解法三
# 前缀树

class Node:
    def __init__(self, value=0):
        self.value = value
        self.isWord = False
        self.next = dict()

class MapSum:
    def __init__(self):
        self.root = Node()

    def reset(self, key, val, add=True):
        node = self.root
        for k in key:
            node.next[k].value = val + (node.next[k].value if add else 0)
            node = node.next[k]

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for k in key:
            if not node.next.get(k):
                node.next[k] = Node()
            node = node.next[k]
        if not node.isWord:
            self.reset(key, val, add=True)
        else:
            self.reset(key, val, add=False)
        node.isWord = True

    def sum(self, prefix: str) -> int:
        node = self.root
        for p in prefix:
            if not node.next.get(p):
                return 0
            node = node.next[p]
        return node.value


obj = MapSum()
obj.insert('apple', 3)
param_2 = obj.sum('ap')
print(param_2)