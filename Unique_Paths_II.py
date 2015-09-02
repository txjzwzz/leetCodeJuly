#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        # use this construct to void the initial of first column and row
        matrix = [[0 for i in range(n+1)] for j in range(m+1)]
        matrix[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] if obstacleGrid[i-1][j-1] == 0 else 0
        return matrix[m][n]




if __name__ == '__main__':
    solution = Solution()
    matrix = [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    print solution.uniquePathsWithObstacles(matrix)
    matrix = [
      [0,0,0],
      [0,1,0],
      [0,0,1]
    ]
    print solution.uniquePathsWithObstacles(matrix)
    matrix = [
      [0,0,0,0],
      [0,1,0,0],
      [0,0,1,0]
    ]
    print solution.uniquePathsWithObstacles(matrix)
    matrix = [
      [0,0,0,0],
      [0,1,0,0]
    ]
    print solution.uniquePathsWithObstacles(matrix)
    matrix = [[0,0],[1,0]]
    print solution.uniquePathsWithObstacles(matrix)