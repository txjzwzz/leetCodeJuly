#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return -1
        matrix = [1 for i in range(n)]
        t2, t3, t5 = 0, 0, 0
        for i in range(1, n):
            matrix[i] = min(matrix[t2] * 2, min(matrix[t3] * 3, matrix[t5] * 5))
            if matrix[i] == matrix[t2] * 2:
                t2 += 1
            if matrix[i] == matrix[t3] * 3:
                t3 += 1
            if matrix[i] == matrix[t5] * 5:
                t5 += 1
        return matrix[n-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.nthUglyNumber(7)