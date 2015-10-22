#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight
neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches the border of the array. How would you address these problems?
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            tmp, live_count = board[i][:], 0
            for j in range(len(tmp)):
                if i > 0:
                    if j > 0 and tmp_last[j-1] == 1:
                        live_count += 1
                    live_count = live_count if tmp_last[j] == 0 else live_count + 1
                    if j < len(tmp)-1 and tmp_last[j+1] == 1:
                        live_count += 1
                if j > 0 and tmp[j-1] == 1:
                    live_count += 1
                if j < len(tmp)-1 and tmp[j+1] == 1:
                    live_count += 1
                if i < len(tmp)-1:
                    if j > 0 and board[i+1][j-1] == 1:
                        live_count += 1
                    if board[i+1][j] == 1:
                        live_count += 1
                    if j < len(tmp)-1 and board[i+1][j+1] == 1:
                        live_count += 1
                if tmp[j] == 0 and live_count == 3:
                    board[i][j] = 1
                if tmp[j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = 0
            tmp_last = tmp[:]
