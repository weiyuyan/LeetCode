#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
宠物小精灵是一部讲述小智和他的搭档皮卡丘一起冒险的故事。

一天，小智和皮卡丘来到了小精灵狩猎场，里面有很多珍贵的野生宠物小精灵。

小智也想收服其中的一些小精灵。

然而，野生的小精灵并不那么容易被收服。

对于每一个野生小精灵而言，小智可能需要使用很多个精灵球才能收服它，而在收服过程中，野生小精灵也会对皮卡丘造成一定的伤害（从而减少皮卡丘的体力）。

当皮卡丘的体力小于等于0时，小智就必须结束狩猎（因为他需要给皮卡丘疗伤），而使得皮卡丘体力小于等于0的野生小精灵也不会被小智收服。

当小智的精灵球用完时，狩猎也宣告结束。

我们假设小智遇到野生小精灵时有两个选择：收服它，或者离开它。

如果小智选择了收服，那么一定会扔出能够收服该小精灵的精灵球，而皮卡丘也一定会受到相应的伤害；如果选择离开它，那么小智不会损失精灵球，皮卡丘也不会损失体力。

小智的目标有两个：主要目标是收服尽可能多的野生小精灵；如果可以收服的小精灵数量一样，小智希望皮卡丘受到的伤害越小（剩余体力越大），因为他们还要继续冒险。

现在已知小智的精灵球数量和皮卡丘的初始体力，已知每一个小精灵需要的用于收服的精灵球数目和它在被收服过程中会对皮卡丘造成的伤害数目。

请问，小智该如何选择收服哪些小精灵以达到他的目标呢？

输入格式
输入数据的第一行包含三个整数：N，M，K，分别代表小智的精灵球数量、皮卡丘初始的体力值、野生小精灵的数量。

之后的K行，每一行代表一个野生小精灵，包括两个整数：收服该小精灵需要的精灵球的数量，以及收服过程中对皮卡丘造成的伤害。

输出格式
输出为一行，包含两个整数：C，R，分别表示最多收服C个小精灵，以及收服C个小精灵时皮卡丘的剩余体力值最多为R。

数据范围
0<N≤1000,
0<M≤500,
0<K≤100
输入样例1：
10 100 5
7 10
2 40
2 50
1 20
4 20
输出样例1：
3 30
输入样例2：
10 100 5
8 110
12 10
20 10
5 200
1 110
输出样例2：
0 100
'''
# 这是一个二维费用的01背包问题
# 花费1：精灵球的数量
# 花费2：皮卡丘的体力
# 价值：小精灵的数量

# 状态表示：①集合：dp[i][j][k]表示所有从前i个精灵中选，且花费1不超过j，花费2不超过k的选法的集合   ②属性：max
# 状态计算：dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-v1[i]][k-v2[i]] + 1)

# 最多收复的小精灵数量：dp[K][N][M]
# 最少消耗的体力：dp[K][N][m] == dp[K][N][M]

from typing import List
class Solution:
    def adventure(self, elf: List[List[int]], balls: int, health: int):
        dp = [[[0 for _ in range(health+1)] for _ in range(balls+1)] for _ in range(len(elf)+1)]
        for i in range(1, len(dp)):
            # j：精灵球数
            for j in range(1, len(dp[0])):
                # k：生命值
                for k in range(1, len(dp[0][0])):
                    if j >= elf[i-1][0] and k >= elf[i-1][1]:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-elf[i-1][0]][k-elf[i-1][1]]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        max_elf = dp[-1][-1][-1]
        max_health = 99999
        for i in range(len(dp)):
            # j：精灵球数
            for j in range(len(dp[0])):
                # k：生命值
                for k in range(len(dp[0][0])):
                    if dp[i][j][k] == max_elf:
                        max_health = min(max_health, k)
        return [max_elf, max_health]

#
# from typing import List
# class Solution:
#     def adventure(self, elf: List[List[int]], balls: int, health: int):
#         dp = [[[0 for _ in range(health+1)] for _ in range(balls+1)] for _ in range(len(elf)+1)]
#         for i in range(1, len(dp)):
#             # j：精灵球数
#             for j in range(elf[i-1][0], len(dp[0])):
#                 # k：生命值
#                 for k in range(elf[i-1][1], len(dp[0][0])):
#                     if j >= elf[i-1][0] and k >= elf[i-1][1]:
#                         dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-elf[i-1][0]][k-elf[i-1][1]]+1)
#                     else:
#                         dp[i][j][k] = dp[i-1][j][k]
#
#         max_elf = dp[-1][-1][-1]
#         max_health = 99999
#         for i in range(len(dp)):
#             # j：精灵球数
#             for j in range(len(dp[0])):
#                 # k：生命值
#                 for k in range(len(dp[0][0])):
#                     if dp[i][j][k] == max_elf:
#                         max_health = min(max_health, k)
#         return [max_elf, max_health]

if __name__ == '__main__':
    solution = Solution()
    balls, health, elf_nums = list(map(int, input().split()))
    elf = []
    for i in range(elf_nums):
        elf.append(list(map(int, input().split())))
    res = solution.adventure(elf, balls, health)
    print(res[0], end=' ')
    print(health-res[1])