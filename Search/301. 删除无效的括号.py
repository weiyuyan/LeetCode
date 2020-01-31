#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/1/31
'''
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

'''
from typing import List
# 我拉了，这道题没搞出来。。。
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#
#         len_str = len(s)
#         used = [False for _ in range(len_str)]
#         list_s = list(s)
#         res = []
#
#         def _is_complete(string: List[str]) -> bool:
#             '''
#             本函数用以判断string是否是合法字符串
#             :param string:
#             :return:
#             '''
#             res = 0
#             for char in string:
#                 if char == '(':
#                     res -= 1
#                 if char == ')':
#                     res += 1
#                 if res < 0:
#                     return False
#             return res == 0
#
#         def _track_back(depth: int, path: List[str], used: List[bool]):
#             '''
#             回溯函数，用来求得无重复的排列数组
#             :param depth: 当前深度
#             :param path: 当前路径
#             :param used: 元素使用情况
#             :return:
#             '''
#             if _is_complete(path):
#                 res.append(''.join(path))
#                 return
#
#             for i in range(len_str):
#                 if not used[i]:
#                     # 剪枝
#                     if list_s[i]!='(' and list_s[i]!=')':
#                         used[i] = True
#                         path.append(list_s[i])
#                         continue
#                     if i>0 and used[i-1]==True and list_s[i-1]==list_s[i]:
#                         continue
#
#                     used[i] = True
#                     path.append(list_s[i])
#                     _track_back(depth+1, path, used)
#
#                     # 回复现场
#                     used[i] = False
#                     path.pop()
#         _track_back(0,[],used)
#         return res


# 网友的，感觉思路很棒

class Solution:
    def removeInvalidParentheses(self, string: str) -> List[str]:

        self.res = []

        # 统计右括号不匹配的数量放入r，左括号没有被匹配的数量放入l
        # 这段感觉很不错
        # 太哲学了，，，如果left > 0，那么还有挽回的余地，如果right > 0， 那么就没有挽回的余地
        # 和做饭一样，盐放少了不怕，怕的是盐放多了（泪目
        left = 0
        right = 0

        for char in string:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        # 验证目前的s中左右括号数目是否匹配
        def _isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                if char == ')':
                    count -= 1
                if count < 0:
                    return False  # ())))
            return count == 0

        # 回溯法
        def dfs(string: str, start: int, left: int, right: int):
            # 如果左右括号匹配，添加进结果集
            if left == 0 and right == 0:
                if _isValid(string):
                    self.res.append(string)
                return
            # 如果左右不匹配
            for i in range(start, len(string)):
                # 如果i和前一个相同，那么删哪个结果都一样，故跳过
                if i - 1 >= start and string[i] == string[i - 1]:
                    continue
                # 如果右括号有不匹配的，删去右括号，判断是否匹配
                if right > 0 and string[i] == ')':
                    dfs(string[:i] + string[i+1:], i, left, right-1)
                # 如果左括号有不匹配的，删去左括号，判断是否匹配
                if left > 0 and string[i] == '(':
                    dfs(string[:i] + string[i+1:], i, left-1, right)

        dfs(string, 0, left, right)
        return self.res




if __name__ == '__main__':
    solution = Solution()
    res = solution.removeInvalidParentheses('()())()')
    print(res)

