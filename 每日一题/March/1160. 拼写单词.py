#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/17
'''
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：

输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母
'''
from typing import List
import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = collections.Counter(chars)
        res = 0
        for word in words:
            word_dict = collections.Counter(word)
            res += len(word)
            for key in word_dict:
                if key in char_dict and word_dict[key]<=char_dict[key]:
                    continue
                else:
                    res -= len(word)
                    break
        return res

solution = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
res = solution.countCharacters(words, chars)
print(res)


