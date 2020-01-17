#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/17

'''
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1:

输入:
words = ["w","wo","wor","worl", "world"]
输出: "world"
解释:
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2:

输入:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"
解释:
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
注意:

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。

'''

# 方法一：暴力法
# 对于每个单词，我们可以检查他的全部前缀是否都存在，可以通过set数据结构加快查找。
from typing import List
# class Solution:
#
#     def longestWord(self, words: List[str]) -> str:
#         ans = ""
#         wordset = set(words)    # 先去掉重复的集合
#         for word in wordset:
#             if len(word) > len(ans) or len(word) == len(ans) and word<ans:
#                 if all(word[:k] in wordset for k in range(1, len(word))):
#                     ans = word
#         return ans
#
#     def _longestWord(self, words: List[str]) -> str:
#         ans = ""
#         wordset = set(words)
#         for word in wordset:
#             if all(word[:k] in wordset for k in range(1, len(word))):
#                 if len(word) > len(ans) or len(word) == len(ans) and word<ans:
#                     ans= word
#         return ans
pass
# P.S.这里我使用了两种暴力方式：其区别在于两组判断条件对换，但是在运行的时候效率和速度却有很大差别：
# longestWord()方法先判断目标单词是否大于ans，然后才进行进一步的前缀匹配
# _longestWord()方法则是不管三七二十一，每个单词前缀都进行匹配，成功之后才进行单词长度比较
# 其思想看似相似，其实不然，先放运行结果。
### longestWord()：
### 执行用时：36ms，在所有Python3提交中击败了100%的用户
### 内存消耗：13.2MB，在所有Python3提交中击败了65.14%的用户

### _longestWord()：
### 执行用时：136ms，在所有Python3提交中击败了35.06%的用户
### 内存消耗：13.1MB，在所有Python3提交中击败了68.31%的用户

# 思考：有时候条件判断的先后顺序很重要，对性能的消耗会有几个数量级的变化

# 方法二： 前缀树+深度优先搜索遍历
# 由于涉及到前缀，故可以用trie(前缀树)解决此类问题
# 将所有单词插入trie，然后从trie中进行深度优先搜索，每找到一个单词表示该单词的全部前缀都存在，我们选取长度最长的单词。
import collections
from functools import reduce
class Solution(object):
    def longestWord(self, words) -> int:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans

solution = Solution()
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
ans = solution.longestWord(words)
print(ans)
