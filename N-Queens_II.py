#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
ollow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        pos_list = [-1 for i in range(n)]
        self.dfs(pos_list, 0, n, res, 0, 0, 0)
        return res[0]

    def dfs(self, pos_list, index, n, res, vertical, left, right):
        if index == n:
            res[0] += 1
            return
        for i in range(n):
            if vertical & ( 1 << i) or left & (1 << (i-index+n-1)) or right & (1 << (i+index)):
                continue
            pos_list[index] = i
            next_vertical = vertical | ( 1<< i)
            next_left = left | (1<<(i-index+n-1))
            next_right = right | (1<<(i+index))
            self.dfs(pos_list, index+1, n, res, next_vertical, next_left, next_right)

if __name__ == '__main__':
    solution = Solution()
    print solution.totalNQueens(3)
    print solution.totalNQueens(4)
    print solution.totalNQueens(5)
    print solution.totalNQueens(6)
    print solution.totalNQueens(7)