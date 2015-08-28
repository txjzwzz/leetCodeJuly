#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        step, direction, res, i, j = 0, 0, [], 0, 0
        while step < m * n:
            res.append(matrix[i][j])
            if direction == 0:
                if j + 1 < n - i:
                    j += 1
                else:
                    direction = 1
                    i += 1
            elif direction == 1:
                if i < m - n + j:
                    i += 1
                else:
                    direction = 2
                    j -= 1
            elif direction == 2:
                if j >= m - i:
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
        return res

if __name__ == '__main__':
    solution = Solution()
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print solution.spiralOrder(matrix)
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print solution.spiralOrder(matrix)
    matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
    print solution.spiralOrder(matrix)