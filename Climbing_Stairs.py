#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        step = [0 for i in range(n+1)]
        step[0] = 1
        step[1] = 1
        for i in range(2, n+1):
            step[i] = step[i-1] + step[i-2]
        return step[n]