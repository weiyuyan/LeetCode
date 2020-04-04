#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/30
'''
设有N堆石子排成一排，其编号为1，2，3，…，N。

每堆石子有一定的质量，可以用一个整数来描述，现在要将这N堆石子合并成为一堆。

每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和，合并后与这两堆石子相邻的石子将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同。

例如有4堆石子分别为 1 3 5 2， 我们可以先合并1、2堆，代价为4，得到4 5 2， 又合并 1，2堆，代价为9，得到9 2 ，再合并得到11，总代价为4+9+11=24；

如果第二步是先合并2，3堆，则代价为7，得到4 7，最后一次合并代价为11，总代价为4+7+11=22。

问题是：找出一种合理的方法，使总的代价最小，输出最小代价。

输入格式
第一行一个数N表示石子的堆数N。

第二行N个数，表示每堆石子的质量(均不超过1000)。

输出格式
输出一个整数，表示最小代价。

数据范围
1≤N≤300
输入样例：
4
1 3 5 2
输出样例：
22
'''
# 状态表示：①集合：f[i][j]表示将[i, j]合并成一堆的方案的集合，所以共(j-i+1)! 个方案   ②属性：min
# 状态计算：将f[i][j]这个集合按下标分成(i, i+1, i+2,..., k,..., j-1)块，表示以k作为最后一次合并的位置
# 既f[i][k]和f[k+1][j]，f[i][j]
# f[i][k] = min(f[i][k]+f[k+1][j]  for k in range(i, j))
# 时间复杂度：n^3：既300x300x300 = 27000000（两千七百万）

# from typing import List
# class Solution:
#     def mergeStone(self, stone: List[int]):
#         n = len(stone)
#         dp = [[0 for _ in range(n)] for _ in range(n+1)]
#         pass
#
# if __name__ == '__main__':
#     n = int(input())
#     stone = list(map(int, input().strip().split(' ')))
#     solution = Solution()


n = int(input().strip())

nums = [0]
nums.extend(list(map(int, input().split())))

s = [0]
for i in range(1, n+1):
    s.append(s[-1]+nums[i])

# 2. 初始化dp数组
dp = [[0 for i in range(n+1)] for j in range(n+1)]

for length in range(2, n+1):    # 遍历区间可能的长度
    for i in range(1, n+1-length+1):    # ！！！出错：在长度一定下，遍历可能的起点，需要满足 i+length-1<=n，边界条件是i=1，length=n时，边界应该小于等于n
        l = i
        r = i + length - 1

        dp[l][r] = float("inf")
        for k in range(l, r):    # ！！！出错：这里k可以取到左边界l，此时表示为dp[1][1] + dp[2][r],即分隔将第一堆和其他堆分开；但是k不可以取到右边界r，此时表示为dp[1][r] + dp[r+1][r],而当r=n时，n+1超出了索引范围
#             print(l,r,k) l=1;r = 5,k =5
            # 3. 状态转移方程
            dp[l][r] = min(dp[l][r], dp[l][k]+dp[k+1][r]+s[r]-s[l-1])    # s[r]-s[l-1]:表示最后两队合并的cost
print(dp[1][n])
