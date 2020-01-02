#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：ShidongDu time:2019/9/24
from typing import List
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont) == 1:
            return [cont[0], 1]
        if len(cont) == 2:
            return [cont[0]*cont[1]+1, cont[1]]
        if len(cont) > 2:
            return [(cont[0]*self.fraction(cont[1:])[0]+self.fraction(cont[1:])[1]), self.fraction(cont[1:])[0]]

    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        now_x = 0
        now_y = 0
        max_distance = x + y
        distance = max_distance
        while(distance <= max_distance):
            distance = now_x + now_y -x -y
            for i in command:
                if i == 'U':
                    now_y += 1
                else:
                    now_x += 1
                if x==now_x and y==now_y:
                    return True
                if [now_x, now_y] in obstacles:
                    return False
        return False






if __name__ == '__main__':
    solution = Solution()
    # num = solution.fraction([3, 4, 2])
    # print(num)
    True_False = solution.robot(command='URRUUUUUUUUUUUUUUUUUUUU', obstacles=[], x=30000000000, y=200)
    print(True_False)