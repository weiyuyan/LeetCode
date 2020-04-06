#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/5
'''
Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。

Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。
比赛一直持续到所有石头都被拿走。

每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。

假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回 "Tie" 。


示例 1：

输入：values = [1,2,3,7]
输出："Bob"
解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
示例 2：

输入：values = [1,2,3,-9]
输出："Alice"
解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
示例 3：

输入：values = [1,2,3,6]
输出："Tie"
解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。
示例 4：

输入：values = [1,2,3,-1,-2,-3,7]
输出："Alice"
示例 5：

输入：values = [-1,-2,-3]
输出："Tie"
 
提示：

1 <= values.length <= 50000
-1000 <= values[i] <= 1000
'''
from typing import List

# 动态规划
# 状态表示：①集合：dp[i]表示从第i个元素起到最后一个元素，当前玩家能拿到的分数的集合  ②属性：max
# 状态计算：
# 首先，dp[n-1] = a[n-1]
# 有三种情况：①只选择第i个元素  ②只选择第i，第i+1个元素  ③选择第i个，第i+1个，第i+2个元素
# 对于其他的 i，我们可以这样思考：当前你的选择有 “取走一、二、三堆”，结果就是给对方留下了
# dp[i+1] dp[i+2] dp[i+3] 对应的情况。
# 也就是对方能够得到的最高分就是 dp[i+1] dp[i+2] dp[i+3] 中的一个，
# 而我们能得到的分数就是剩下的所有分数减去对方能拿到的分数。为了让我们拿到的更多，就得让对方拿到的最少。
# dp[i] = sum{a[i]~a[n-1]} - min(dp[i+1], dp[i+2], dp[i+3])

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0 for _ in range(len(stoneValue)+2)]  # 加2是为了防止边界溢出
        n = len(stoneValue)
        dp[n-1] = stoneValue[n-1]
        tmp_sum = stoneValue[n-1]

        for i in range(n-2, -1, -1):
            tmp_sum += stoneValue[i]
            dp[i] = tmp_sum - min(dp[i+1], dp[i+2], dp[i+3])

        if dp[0]*2 > tmp_sum:
            return 'Alice'
        if dp[0]*2 < tmp_sum:
            return 'Bob'
        if dp[0]*2 == tmp_sum:
            return 'Tie'

if __name__ == '__main__':
    solution = Solution()
    stoneValue = [1, 2, 3, 7]
    res = solution.stoneGameIII(stoneValue)
    print(res)