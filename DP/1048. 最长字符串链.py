#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/2/11
'''
给出一个单词列表，其中每个单词都由小写英文字母组成。

如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
 

示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
'''

'''
题解：
思路

动态规划

word1在任意位置添加一个字母变成word2”等价于“word2在任意一个位置减去一个字母变成word1”（假设叫做逆前身），
则word中最长的词链就是[word_1,word_2,...,word_k]组成的序列，其中word_3是word_2的逆前身，word_2是word_1的逆前身，以此类推；
假设有一个笔记本note，记录words中所有单词的词链长度chain，则对于word，他的最长词链长度为chain = max(1,1+note[subWord])，
其中subWord表示的是word的每一个逆前身，且这个逆前身在words中（也就是说note中有subWord的记录）；
对于words按照word的长度进行排序，排序后逐个对word按照步骤2的公式进行判断。如果word在note中没有记录，
则说明word没有逆前身，他的chain为1.

举例:
words=["a","b","ba","bca","bda","bdca"]

初始化note={}
对于a，note中无记录，则chain为1，note={"a":1}
对于b，同上，note={"a":1,"b":1}
对于ba，chain=max(1,1+note[b],1+note[a])=2,note={"a":1,"b":1,"ba"=2}
对于bca，chain=max(1,1+note[ba])=3,note={"a":1,"b":1,"ba"=2,"bca":3}
对于bda，同上，note={"a":1,"b":1,"ba"=2,"bca":3,"bda":3}
对于bdca，chain=max(1,1+note[bca],1+note[bda])=4
遍历所有word之后，可知最大词链长度为4

'''
from typing import List
class Solution:
    def longestStrainChain(self, words: List[str]) -> int:
        words.sort(key=len)
        note = {}
        for word in words:
            if word not in note:
                note[word] = 1  # 如果第一次遇到，置一
            # 接下来
            for j in range(len(word)):
                new_word = word[: j]+ word[j+1:]
                if new_word in note:
                    note[word] = max(note[word], note[new_word]+1)

        return max(note.values())

solution = Solution()
res = solution.longestStrainChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh",
                                   "zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj",
                                   "zczpzfvdhx","gru"])
print(res)
