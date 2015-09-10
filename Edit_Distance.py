#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        matrix = [i for i in range(len2+1)]

        for i in range(1, len1+1):
            prev = matrix[0]
            matrix[0] = i
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:  # matrix[i][j] = matrix[i-1][j-1]
                    cur = prev
                else:
                    cur = min(matrix[j-1], matrix[j], prev)+1 # matrix[i][j-1]  matrix[i-1][j]  matrix[i-1][j-1]
                prev = matrix[j]
                matrix[j] = cur
        return matrix[len2]

if __name__ == '__main__':
    solution = Solution()
    print solution.minDistance("a", "abc")
    print solution.minDistance("", "abc")
    print solution.minDistance("a", "")
    print solution.minDistance("acde", "abc")
    print solution.minDistance("acde", "abcdef")