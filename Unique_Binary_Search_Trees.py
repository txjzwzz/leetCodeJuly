#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        matrix = [0 for i in range(n+1)]
        matrix[0] = matrix[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                matrix[i] += matrix[j]*matrix[i-j-1]
        return matrix[n]