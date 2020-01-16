#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/16
'''
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例 1:

输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"
注:

输入只包含小写字母。
1 <= 字典单词数 <=1000
1 <=  句中词语数 <= 1000
1 <= 词根长度 <= 100
1 <= 句中词语长度 <= 1000

'''

# 方法一：前缀哈希
from typing import List
# class Solution:
#     def replaceWords(self, dict: List[str], sentence: str) -> str:
#         rootset = set(dict)
#
#         def replace(word):
#             for i in range(1, len(word)):
#                 if word[:i] in rootset: return word[:i]
#             return word
#         return  ' '.join(map(replace, sentence.split()))

# 方法二：前缀树
import collections
from functools import reduce
# class Solution:
#     def replaceWords(self, root_dict: List[str], sentence: str) -> str:
#         Trie = lambda: collections.defaultdict(Trie)
#         trie = Trie()
#         END = True
#
#         for root in root_dict:
#             reduce(dict.__getitem__, root, trie)[END] = root
#
#         def replace(word):
#             cur = trie
#             for letter in word:
#                 if letter not in cur or END in cur: break
#                 cur = cur[letter]
#             return cur.get(END, word)
#         return " ".join(map(replace, sentence.split()))
# 这个运行不了，不好

# 方法三：前缀树
class Solution:
    def replaceWords(selfself, dict:List[str], sentence: str) -> str:
        d = {}  # 字典树初始化
        for word in dict:   # 把前缀放入字典树
            t = d
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['end'] = True

        def f(word):    #单词前缀判断
            t = d
            for i, c in enumerate(word):
                if 'end' in t:
                    return word[: i]    # 存在前缀就返回前缀
                elif c not in t:
                    break               # 不存在前缀就跳出循环并返回原词
                t = t[c]
            return word
        return ' '.join(map(f, sentence.split(' ')))




if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    solution = Solution()
    print(solution.replaceWords(dict, sentence))


