#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        lengthX = len(matrix)-1
        for i in range((lengthX+1)>>2):
            for j in range(lengthX>>2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[lengthX-j][i]
                matrix[lengthX-j][i] = matrix[lengthX-i][lengthX-j]
                matrix[lengthX-i][lengthX-j] = matrix[j][lengthX-i]
                matrix[j][lengthX-i] = tmp

if __name__ == '__main__':
    solution = Solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix)
    print matrix
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    solution.rotate(matrix)
    print matrix

