#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to
n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        perfect_num = [i * i for i in range(1, int(math.sqrt(n))+1)]
        res, index =[2147483648], len(perfect_num)-1
        self.search(perfect_num, index, n, 0, res)
        return res[0]


    def search(self, perfect_num, index, tmp_n, tmp_res, res):
        if index == 0:
            tmp_res += tmp_n
            res[0] = tmp_res if tmp_res < res[0] else res[0]
            return
        for i in range(int(tmp_n/perfect_num[index]), -1, -1):
            if i + tmp_res < res[0]:
                self.search(perfect_num, index-1, tmp_n-i*perfect_num[index], tmp_res+i, res)

if __name__ == '__main__':
    solution = Solution()
    print solution.numSquares(1)
    print solution.numSquares(2)
    print solution.numSquares(3)
    print solution.numSquares(4)
    print solution.numSquares(5)
    print solution.numSquares(6)
    print solution.numSquares(7)
    print solution.numSquares(8)
    print solution.numSquares(9)
    print solution.numSquares(10)
    print solution.numSquares(11)
    print solution.numSquares(12)
    print solution.numSquares(13)
    print solution.numSquares(14)
    print solution.numSquares(14)
    print solution.numSquares(312)