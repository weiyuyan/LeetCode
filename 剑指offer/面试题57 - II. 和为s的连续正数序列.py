#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2020/3/5
'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 
限制：

1 <= target <= 10^5
'''
# from typing import List
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         res = []
#         tmp_res = []
#         tmp_target = target
#         for i in range(1, target):
#             if tmp_target == 0: res.append(tmp_res)
#             if tmp_target-i >= 0:
#                 tmp_res.append(i)
#                 tmp_target -= i
#             while tmp_target-i < 0 and tmp_target!=0:
#                 tmp_target += tmp_res.pop(0)
#         return res

# solution = Solution()
# res = solution.findContinuousSequence(9)
# print(res)

# C++写法
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> ans;
        int l = 1, r = 0, sum = 0, i;
        while(r <= (target+1)/2)//r最多不会超过一半
        {
        	if(sum == target)
        	{	//相等
        		vector<int> t;
        		for(i = l; i <= r; ++i)
        			t.push_back(i);
        		if(t.size() > 1)
        			ans.push_back(t);
        		sum -= l;//更新左边界，让他少一个数
        		l++;
        	}
        	while(sum > target)
        	{	//大了，减少左边的数
        		sum -= l;
        		l++;
        	}
        	while(sum < target)
        	{	//小了，增加右边的数
        		r++;
        		sum += r;
        	}
        }
        return ans;
    }
};
