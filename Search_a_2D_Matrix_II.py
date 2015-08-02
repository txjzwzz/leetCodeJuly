#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        length = min(len(matrix), len(matrix[0]))
        for i in range(length-1):
            if matrix[i][i] == target:
                return True
            if matrix[i][i] < target and matrix[i+1][i+1] > target:
                matrix1 = [matrix[j][:i+1] for j in range(i+1, len(matrix))]
                matrix2 = [matrix[j][i+1:] for j in range(0, i+1)]
                return self.searchMatrix(matrix1, target) or self.searchMatrix(matrix2, target)
        # matrix[length-1][length-1] < target
        if matrix[length-1][length-1] == target:
            return True
        elif len(matrix) < len(matrix[0]):
            matrixN = [matrix[j][length:] for j in range(len(matrix))]
            return self.searchMatrix(matrixN, target)
        else:
            matrixN = [matrix[j][:] for j in range(length, len(matrix))]
            return self.searchMatrix(matrixN, target)

if __name__ == '__main__':
    matrix = [[1, 4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    solution = Solution()
    print solution.searchMatrix(matrix, target)
    target = 20
    print solution.searchMatrix(matrix, target)
    target = 1
    print solution.searchMatrix(matrix, target)
    target = 30
    print solution.searchMatrix(matrix, target)
    target = 15
    print solution.searchMatrix(matrix, target)
    target = 18
    print solution.searchMatrix(matrix, target)
    target = 9
    print solution.searchMatrix(matrix, target)
    print "go to false #######################"
    target = 0
    print solution.searchMatrix(matrix, target)
    target = 25
    print solution.searchMatrix(matrix, target)
    target = 27
    print solution.searchMatrix(matrix, target)
    target = 28
    print solution.searchMatrix(matrix, target)
    target = 31
    print solution.searchMatrix(matrix, target)
