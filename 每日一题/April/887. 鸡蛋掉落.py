#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/11
'''
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

 

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4
 

提示：

1 <= K <= 100
1 <= N <= 10000
通过次数13,593提交次数55,197
'''
# 动态规划
# 首先，一共有N层楼梯，K个鸡蛋
# 状态表示：①集合：dp[i][j]表示在第i个位置抛，有j个鸡蛋，所能扔的方案的集合    ②属性：min
# 状态计算：这里一共有两种情况：鸡蛋碎了；鸡蛋没碎
# dp[i][j] = min【dp[i-1][j-1](鸡蛋碎了) , dp[N-i][j]】 + 1
# 初始化：
# dp[1][*] = 1  表示只有一层，那么不管几个鸡蛋，都1次即可
# dp[*][1] = *  表示只有一个鸡蛋，那么有几层就要试几次

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         res = N
#         dp = [[10000000000 for _ in range(1+K)] for _ in range(1+N)]
#
#         # 初始化
#         for j in range(len(dp[0])):
#             dp[1][j] = 1
#         for j in range(len(dp)):
#             dp[j][1] = j
#
#         for i in range(1, len(dp)):
#             for j in range(1, len(dp[0])):
#                 for k in range(1, i):
#                     dp[i][j] = min(dp[i][j], max(dp[k-1][j-1], dp[i-k][j])+1)
#                 # dp[i][j] = min(dp[i-1][j-1], dp[N-i][j]) + 1
#                 # dp[i][j] = min(dp[i - 1][j - 1], dp[N - i][j]) + 1
#         return dp[-1][-1]

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def parse(k, n):
            if n == 1:  # 如果只有1层，不管有多少蛋只需试1次
                return 1
            elif n == 0:
                return 0
            elif k == 1:  # 只有1个鸡蛋，则只能逐层试
                return n
            elif (k, n) in table:
                return table[(k, n)]

            f = float('inf')  # 定义一个无限大数作为初始条件
            for x in range(1, n + 1):  # 将鸡蛋扔在第x层，从第1层开始
                fx = 1 + max(parse(k - 1, x - 1), parse(k, n - x))
                f = min(f, fx)

            table[(k, n)] = f
            return f

        table = {}  # 记忆被计算过的情况
        return parse(k, n)
if __name__ == '__main__':
    solution = Solution()
    K = 3
    N = 2
    res = solution.superEggDrop(K, N)
    print(res)