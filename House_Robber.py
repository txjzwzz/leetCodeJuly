#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return 0
        matrix = [0 for i in range(len(num))]
        matrix[0] = num[0]
        if len(num) > 1:
            matrix[1] = max(num[0], num[1])
        for i in range(2, len(num)):
            matrix[i] = max(matrix[i-1], matrix[i-2] + num[i])
        return matrix[len(num)-1]

if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    solution = Solution()
    print solution.rob(num)