#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        step, direction, i, j = 1, 0, 0, 0
        while step <= n * n:
            matrix[i][j] = step
            if direction == 0:
                if j + 1 < n - i:
                    j += 1
                else:
                    direction = 1
                    i += 1
            elif direction == 1:
                if i < j:
                    i += 1
                else:
                    direction = 2
                    j -= 1
            elif direction == 2:
                if j >= n - i:
                    j -= 1
                else:
                    direction = 3
                    i -= 1
            else:
                if i - 1 > j:
                    i -= 1
                else:
                    direction = 0
                    j += 1
            step += 1
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print solution.generateMatrix(1)
    print solution.generateMatrix(3)
    print solution.generateMatrix(4)