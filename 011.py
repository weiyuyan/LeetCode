#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/9/25
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if height[-j-1] >= height[i]:




if __name__ == '__main__':
