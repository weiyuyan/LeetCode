#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: ShidongDu time:2020/1/13
'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

# 暴力解法
from typing import List
# class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     tmp_result = []
    #     result = []
    #     def generate(s: str, n: int) -> List[str]:
    #         if n == 0:
    #             tmp_result.append(s)
    #         else:
    #             generate(s + '(', n - 1)
    #             generate(s + ')', n - 1)
    #
    #     def judgeParenthesis(s: str) -> bool:
    #         symbol_list = ['(', ')']
    #         result = []
    #         for char in s:
    #             if char in symbol_list:
    #                 if len(result) == 0:
    #                     result.append(char)
    #                 elif char == ')' and result[-1] == '(':
    #                     result.pop(-1)
    #                 else:
    #                     result.append(char)
    #         if len(result) == 0:
    #             return True
    #         else:
    #             return False
    #
    #     generate('', 2*n)
    #     for i in tmp_result:
    #         if judgeParenthesis(i):
    #             result.append(i)
    #     return result


# 方法二：回溯法
'''
只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。我们可以通过跟踪到目前为止放置的左括号和
右括号的数目来做到这一点，

如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。

'''
# class Solution(object):
#     def generateParenthesis(self, N):
#         ans = []
#         def backtrack(S = '', left = 0, right = 0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 return
#             if left < N:
#                 backtrack(S+'(', left+1, right)
#             if right < left:
#                 backtrack(S+')', left, right+1)
#
#         backtrack()
#         return ans


# 方法三： 闭合数
'''
对于每个闭合数 c，我们知道起始和结束括号必定位于索引 0 和 2*c + 1。
然后两者间的 2*c 个元素一定是有效序列，其余元素一定是有效序列。
'''
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    solution = Solution()
    result = solution.generateParenthesis(3)
    print(result)