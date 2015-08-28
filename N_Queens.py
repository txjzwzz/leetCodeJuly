#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
"""
class Solution(object):
    # def solveNQueens(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[List[str]]
    #     """
    #     res = []
    #     pos_list = [-1 for i in range(n)]
    #     index = 0
    #     while index >= 0:
    #         if index >= n:
    #             tmp = []
    #             for i in range(n):
    #                 str_list = ['.' for j in range(n)]
    #                 str_list[pos_list[i]] = 'Q'
    #                 str_ith = "".join(str_list)
    #                 tmp.append(str_ith)
    #             res.append(tmp)
    #             index -= 1
    #             continue
    #         pos_list[index] += 1
    #         if pos_list[index] >= n:
    #             pos_list[index] = -1
    #             index -= 1
    #             continue
    #         if self.is_valid(pos_list, index):
    #             index += 1
    #     return res
    #
    # def is_valid(self, pos, index):
    #     if index == 0:
    #         return True
    #     for i in range(index):
    #         if pos[i] == pos[index]:
    #             return False
    #         if pos[index] == pos[i]-(index-i):
    #             return False
    #         if pos[index] == pos[i]+(index-i):
    #             return False
    #     return True
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        pos_list = [-1 for i in range(n)]
        self.dfs(pos_list, 0, n, res, 0, 0, 0)
        return res

    def dfs(self, pos_list, index, n, res, vertical, left, right):
        if index == n:
            tmp = []
            for i in range(n):
                str_list = ['.' for j in range(n)]
                str_list[pos_list[i]] = 'Q'
                tmp.append("".join(str_list))
            res.append(tmp)
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
    print solution.solveNQueens(3)
    print solution.solveNQueens(4)
    print solution.solveNQueens(5)
    print solution.solveNQueens(6)