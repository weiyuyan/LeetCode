#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/16
'''
维护一个字符串集合，支持两种操作：

“I x”向集合中插入一个字符串x；
“Q x”询问一个字符串在集合中出现了多少次。
共有N个操作，输入的字符串总长度不超过 105，字符串仅包含小写英文字母。

输入格式
第一行包含整数N，表示操作数。

接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。

输出格式
对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。

每个结果占一行。

数据范围
1≤N≤2∗104
输入样例：
5
I abc
Q abc
Q ab
I ab
Q ab
输出样例：
1
0
1
'''
# Trie树：高效地存储和查找字符串
#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/16

'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

'''
'''
Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)O(n)，
其中 nn 是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间。
此时 Trie 树只需要 O(m)O(m) 的时间复杂度，其中 mm 为键长。而在平衡树中查找键值需要 O(mlog n)时间复杂度。

'''

# 方法一：
# class Trie:
#
#     class TrieNode(object):
#         def __init__(self):
#             self.is_word = False
#             self.children = [None] * 26
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Trie.TrieNode()
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         p = self.root
#         for c in word:
#             index = ord(c) - ord('a')
#             if not p.children[index]:
#                 p.children[index] = Trie.TrieNode()
#             p = p.children[index]
#             p.is_word = True
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         node = self.find(word)
#         return node is not None and node.is_word
#
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         return self.find(prefix) is not None
#
#     def find(self, prefix):
#         p = self.root
#         for c in prefix:
#             index = ord(c) - ord('a')
#             if not p.children[index]: return None
#             p = p.children[index]
#         return p
# pass
# # 方法二：利用Python特有的动态语言特点，利用字典
# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {}
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         p = self.root
#         for c in word:
#             if c not in p:
#                 p[c] = {}
#             p = p[c]
#         p['#'] = True
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         node = self.find(word)
#         return node is not None and '#' in node
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         return self.find(prefix) is not None
#
#     def find(self, prefix):
#         p = self.root
#         for c in prefix:
#             if c not in p: return None
#             p = p[c]
#         return p
#
# # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert('word')
# param_2 = obj.search('word')
# param_3 = obj.startsWith('prefix')
# param_4 = obj.startsWith('wo')
# print(param_2)
# print(param_3)
# print(param_4)

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        p = self.root
        for char in word:
            if char not in p:
                p[char] = {}
            p = p[char]
        p['#'] = p.get('#', 0) + 1

    def search(self, word: str) -> int:
        p = self.root
        for char in word:
            if char not in p:
                return 0
            p = p[char]
        return p.get('#', 0)

if __name__ == '__main__':
    trie_tree = Trie()
    N = int(input())
    res = []
    for i in range(N):
        option, string = list(input().split())
        if option == 'I':
            trie_tree.insert(string)
        if option == 'Q':
            res.append(trie_tree.search(string))
    for i in res:
        print(i)
