#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
# 关键在于查看到底在什么地方变化了，+1则最后一位必为0
# +2则倒数第二位必为0，以此类推
# 所以找到第一个变化的地方，在这个地方之后肯定就是为0了！
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        mask = ~0
        while m & mask != n & mask:
            mask = mask << 1
        return m & mask

if __name__ == '__main__':
    solution = Solution()
    print solution.rangeBitwiseAnd(5, 7)
    print solution.rangeBitwiseAnd(5, 8)