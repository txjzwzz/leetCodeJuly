#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        mark00 = 1
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                mark00 = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(len(matrix)-1, -1, -1):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if mark00 == 0:
                matrix[i][0] = 0

if __name__ == '__main__':
    solution = Solution()
    matrix = [[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print matrix
    matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print matrix
    matrix = [[1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 1, 1]]
    solution.setZeroes(matrix)
    print matrix
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]
    solution.setZeroes(matrix)
    print matrix
    matrix = [[1, 0]]
    solution.setZeroes(matrix)
    print matrix