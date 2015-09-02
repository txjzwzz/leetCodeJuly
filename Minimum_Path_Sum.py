#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        matrix = [[2147483647 for i in range(n+1)] for j in range(m+1)]
        matrix[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1])+grid[i-1][j-1]
        return matrix[m][n]

if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 2, 3], [1, 4, 5]]
    print solution.minPathSum(grid)