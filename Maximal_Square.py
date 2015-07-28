#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    # 一个点一个点去搜索在时间上来不及
    # 使用动态规划，一行行地进行处理
    # 思路如下，看上一行的状态，如果有连续的1，这一行对应有连续的1，长度也够组成正方形，就标上2 2 2
    # 以此类推，每行都这样处理
    # 这种思路的问题在于，如果有2和3的重叠的部分就没有办法处理了
    # 而且既然是动态规划，就不应该引入这么多自己要处理的东西，应该很简洁的相关关系！
    # 关系就是如果以(i, j)为终点的是正方形的话，那么以(i-1, j) (i, j-1) (i-1, j-1)为终点的也必须是正方形
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        res = 0
        mark = [0 for i in range(len(matrix[0]))]
        for i in matrix:
            tmpMark = [0 for k in range(len(i))]
            for j in range(len(i)):
                if i[j] == '1':
                    tmpMark[j] = 1
                    if j > 0:
                        tmpMark[j] = min(tmpMark[j-1], min(mark[j], mark[j-1])) + 1
                    if tmpMark[j] > res:
                        res = tmpMark[j]
            mark = tmpMark[:]
        return res * res

if __name__ == '__main__':
    solution = Solution()
    matrix = []
    print solution.maximalSquare(matrix)
    matrix = [[], []]
    print solution.maximalSquare(matrix)
    matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]
    print solution.maximalSquare(matrix)
    matrix = [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]
    print solution.maximalSquare(matrix)
    matrix = [['1', '1', '1'], ['1', '1', '1'], ['1', '0', '1']]
    print solution.maximalSquare(matrix)
    matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    print solution.maximalSquare(matrix)
    matrix = [['1']]
    print solution.maximalSquare(matrix)
    matrix = ['11', '11']
    print solution.maximalSquare(matrix)
