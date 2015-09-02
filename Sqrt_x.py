#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        xmax = 65536
        xmin = 0
        ans = xmax >> 1
        while True:
            if ans * ans == x:
                return ans
            if ans * ans < x and (ans+1) * (ans+1) > x:
                return ans
            if ans * ans < x:
                xmin = ans
                ans = xmin + ((xmax-xmin) >> 1)
            else:
                xmax = ans
                ans = xmin + ((xmax-xmin) >> 1)

if __name__ == '__main__':
    solution = Solution()
    print solution.mySqrt(1)
    print solution.mySqrt(10)
    print solution.mySqrt(100)
    print solution.mySqrt(1000)
    print solution.mySqrt(10000)
    print solution.mySqrt(100000)