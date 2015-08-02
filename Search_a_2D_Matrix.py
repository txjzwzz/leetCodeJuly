#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        indexX = len(matrix)-1
        indexY = 0
        while True:
            if indexX < 0 or indexY > len(matrix[0])-1:
                return False
            if matrix[indexX][indexY] == target:
                return True
            elif matrix[indexX][indexY] > target:
                indexX -= 1
            else:
                indexY += 1

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    print solution.searchMatrix(matrix, target)
    target = 20
    print solution.searchMatrix(matrix, target)
    target = 34
    print solution.searchMatrix(matrix, target)
    target = 1
    print solution.searchMatrix(matrix, target)
    target = 7
    print solution.searchMatrix(matrix, target)
    target = 100
    print solution.searchMatrix(matrix, target)
    target = 0
    print solution.searchMatrix(matrix, target)
    target = 8
    print solution.searchMatrix(matrix, target)
    target = 22
    print solution.searchMatrix(matrix, target)