#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/20
'''
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

'''

# 方法一： 字典树
class WordDictionary:

    def __init__(self):
        self.d = {} # 字典树

    def addWord(self, word: str) -> None:
        t = self.d  # 将单词填进字典树
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True

    def search(self, word: str) -> bool:
        cut = False
        def f(td, s):   # 深度搜索，参数为当前字典，当前字符串
            nonlocal cut    # nonlocal的意思是该变量是上一层的局部变量，但又不是全局变量
            if cut: # 剪枝
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':
                    return sum(f(t[j], s[i+1:]) for j in t if j != 'end')   # 深度搜索
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut
        return f(self.d, word)


