#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    # 一个点一个点去搜索在时间上来不及
    # 使用动态规划，一行行地进行处理
    # 思路如下，看上一行的状态，如果有连续的1，这一行对应有连续的1，长度也够组成正方形，就标上2 2 2
    # 以此类推，每行都这样处理
    # 这种思路的问题在于，如果有2和3的重叠的部分就没有办法处理了
    # 而且既然是动态规划，就不应该引入这么多自己要处理的东西，应该很简洁的相关关系！
    def maximalSquare(self, matrix):
        pass

