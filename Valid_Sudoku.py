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
        inmatrix = [0 for i in range(len(board[0]))]
        for i in range(len(board)):
            tmp = 0
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                else:
                    bit_val = 1 << (ord(board[i][j])-48)
                    if tmp & bit_val or col[j] & bit_val or inmatrix[(i/3)*3+j/3] & bit_val:
                        return False
                    else:
                        tmp |= bit_val
                        col[j] |= bit_val
                        inmatrix[(i/3)*3+j/3] |= bit_val
        return True

if __name__ == '__main__':
    solution = Solution()
    board = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
    print solution.isValidSudoku(board)
