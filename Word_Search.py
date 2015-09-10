#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        matrix = [[1 for i in board[0]] for j in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, 0, i, j, matrix):
                    return True
        return False

    def dfs(self, board, word, index, i, j, matrix):
        if index == len(word)-1:
            return True
        matrix[i][j] = 0
        if i > 0 and board[i-1][j] == word[index+1] and matrix[i-1][j] and self.dfs(board, word, index+1, i-1, j, matrix):
            return True
        if j > 0 and board[i][j-1] == word[index+1] and matrix[i][j-1] and self.dfs(board, word, index+1, i, j-1, matrix):
            return True
        if i < len(board)-1 and board[i+1][j] == word[index+1] and matrix[i+1][j] and self.dfs(board, word, index+1, i+1, j, matrix):
            return True
        if j < len(board[0])-1 and board[i][j+1] == word[index+1] and matrix[i][j+1] and self.dfs(board, word, index+1, i, j+1, matrix):
            return True
        matrix[i][j] = 1
        return False

if __name__ == '__main__':
    solution = Solution()
    board = [
              "ABCE",
              "SFCS",
              "ADEE"
            ]
    word = "ABCCED"
    print solution.exist(board, word)
    word = "SEE"
    print solution.exist(board, word)
    word = "ABCB"
    print solution.exist(board, word)