#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/4/16
'''
在网友的国度中共有 n 种不同面额的货币，第 i 种货币的面额为 a[i]，你可以假设每一种货币都有无穷多张。

为了方便，我们把货币种数为 n、面额数组为 a[1..n] 的货币系统记作 (n,a)。 

在一个完善的货币系统中，每一个非负整数的金额 x 都应该可以被表示出，即对每一个非负整数 x，都存在 n 个非负整数 t[i] 满足 a[i]× t[i] 的和为 x。

然而，在网友的国度中，货币系统可能是不完善的，即可能存在金额 x 不能被该货币系统表示出。

例如在货币系统 n=3, a=[2,5,9] 中，金额 1,3 就无法被表示出来。 

两个货币系统 (n,a) 和 (m,b) 是等价的，当且仅当对于任意非负整数 x，它要么均可以被两个货币系统表出，要么不能被其中任何一个表出。 

现在网友们打算简化一下货币系统。

他们希望找到一个货币系统 (m,b)，满足 (m,b) 与原来的货币系统 (n,a) 等价，且 m 尽可能的小。

他们希望你来协助完成这个艰巨的任务：找到最小的 m。

输入格式
输入文件的第一行包含一个整数 T，表示数据的组数。

接下来按照如下格式分别给出T组数据。 

每组数据的第一行包含一个正整数 n。

接下来一行包含 n 个由空格隔开的正整数 a[i]。

输出格式
输出文件共有T行，对于每组数据，输出一行一个正整数，表示所有与 (n,a) 等价的货币系统 (m,b) 中，最小的 m。

数据范围
1≤n≤100,
1≤a[i]≤25000,
1≤T≤20
输入样例：
2
4
3 19 10 6
5
11 29 13 19 17
输出样例：
2
5
'''
# 首先发现题目中隐含的一些性质
# 性质1：a1, a2, ... , an一定都可以被表示出来
# 性质2：bi 一定不能被b1, b2, ... , bm表示出来，否则就可以把bi删掉，{b}就不是最优解
# 性质3：b1, b2, b3, ... , bm一定都是从{ai}中选出来的。可以用反证法证明
# 假设bk 不在{ai}中，有两种可能：

# ①{ai}可以表示出bk，即bk = t1*a1 + t2*a2....，由于bk不在{ai}中，因此有效的式子至少有两个
# 记为bk = tq*aq + tr*ar ，其中tq, tr >= 1。
# 此外，由于{ai}中的元素可以由{bi}来表示，因此 aq ar也可以由{bi}表示，假设 aq, ar由bk等{bi}中的元素表示，假设有bk在里边
# 即aq = m*bk + n*b1... ，由于m>=1 ，这时原式子就变成
# bk = tq* (m*bk + n*b1 +...+) + tr*ar，这里ar以此类推，不举例了
# 显然矛盾，因为tq, m, n, ..., tr均 >= 1
# 所以可能①不成立

# 再来看可能②：
# ②{ai} 不可以表示出bk，显然矛盾，因为{ai}不可以表示出bk，但{bi}一定可以表示出bk，与题目相悖

# 综上，b1, b2, b3,...,bm 一定都是从{ai}中选出来的
# 于是答案的搜索空间从无穷降到了指数级别

# 正式开始：
# 首先，值较大的数肯定是由值较小的数表示出来的，所以我们把a数组进行一个排序
# 所以我们的核心就是，判断ai能否被a1~ai-1间的数字表示出来
# 也就是看a1~ai-1是否能装满容积为ai的背包  完全背包问题

# dp[i][j]表示只看前i张纸币，能组成j元钱的方案数
from typing import List
class Solution:
    def currency_system(self, money: List[int]):
        money.sort()
        dp = [[0 for _ in range(money[-1]+1)] for _ in range(len(money)+1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j >= money[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-money[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        # 这里我们遍历dp数组，从字典里消去那些重复的元素
        res = set(money[:])
        for i in range(1, len(money)):
            for j in range(i, len(money)):
                if dp[i][money[j]] != 0:
                    if money[j] in res:
                        res.remove(money[j])

        return len(res)

if __name__ == '__main__':
    solution = Solution()
    groups = int(input())
    res = []
    for i in range(groups):
        nums = int(input())
        money = list(map(int, input().split()))
        tmp = solution.currency_system(money)
        res.append(tmp)

    for i in res:
        print(i)
