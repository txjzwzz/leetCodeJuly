#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.c_a_b(m+n-2, n-1) if n < m else self.c_a_b(m+n-2, m-1)

    def c_a_b(self, a, b):
        fenmu, fenzi = 1, 1
        for i in range(1, b+1):
            fenzi *= (a-i+1)
            fenmu *= i
        return fenzi / fenmu

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        fenmu, fenzi = 1, 1
        k = m-1 if m < n else n-1
        c = m+n-2
        for i in range(1, k+1):
            fenzi *= (c-i+1)
            fenmu *= i
        return fenzi/fenmu

if __name__ == '__main__':
    solution = Solution()
    print solution.uniquePaths(3, 3)
    print solution.uniquePaths(3, 4)
    print solution.uniquePaths(3, 5)
    print solution.uniquePaths(5, 3)
    print solution.uniquePaths(1, 2)