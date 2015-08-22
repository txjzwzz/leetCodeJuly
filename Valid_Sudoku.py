#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return True
        col = [0 for i in range(len(board[0]))]
        for i in range(len(board)):
            tmp = 0
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                else:
                    if tmp & (1 << (ord(board[i][j])-48)) or col[j] & (1 << (ord(board[i][j]))-48):
                        return False
                    else:
                        tmp |= (1 << (ord(board[i][j]))-48)
                        col[j] |= (1 << ord(board[i][j])-48)
        return True

if __name__ == '__main__':
    solution = Solution()
    board = [['1', '.', '2'], ['2', '.', '3'], ['3', '.', '1']]
    print solution.isValidSudoku(board)
    board = [['1', '3', '2'], ['2', '.', '3'], ['3', '.', '1']]
    print solution.isValidSudoku(board)
    board = [['1', '1', '2'], ['2', '.', '3'], ['3', '.', '1']]
    print solution.isValidSudoku(board)
    board = [['1', '.', '2'], ['3', '.', '3'], ['3', '.', '1']]
    print solution.isValidSudoku(board)
    board = [['1', '.', '2'], ['2', '.', '2'], ['3', '.', '1']]
    print solution.isValidSudoku(board)
