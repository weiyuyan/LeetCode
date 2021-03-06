#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/19
'''
给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。

如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。

示例 1：

输入：croakOfFrogs = "croakcroak"
输出：1
解释：一只青蛙 “呱呱” 两次
示例 2：

输入：croakOfFrogs = "crcoakroak"
输出：2
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"
示例 3：

输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。
示例 4：

输入：croakOfFrogs = "croakcroa"
输出：-1

提示：

1 <= croakOfFrogs.length <= 10^5
字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'
'''
# 超时了！日他妈的
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frog_list = [['c']]
        if croakOfFrogs[0] != 'c':
            return -1

        res = 0
        c_pos = 1
        r_pos = 0
        o_pos = 0
        a_pos = 0


        for i in range(1, len(croakOfFrogs)):
            res = max(res, (c_pos+r_pos+o_pos+a_pos))
            song = croakOfFrogs[i]
            if song == 'c':
                c_pos+=1

            elif song == 'r':
                c_pos -= 1
                r_pos += 1
                if c_pos < 0:
                    return -1

            elif song == 'o':
                r_pos -= 1
                o_pos += 1
                if r_pos < 0:
                    return -1

            elif song == 'a':
                o_pos -= 1
                a_pos += 1
                if o_pos < 0:
                    return -1

            elif song == 'k':
                a_pos -= 1
                if a_pos < 0:
                    return -1

        return res

if __name__ == '__main__':
    solution = Solution()
    croakOfFrogs = 'crcoakroak'
    res = solution.minNumberOfFrogs(croakOfFrogs)
    print(res)