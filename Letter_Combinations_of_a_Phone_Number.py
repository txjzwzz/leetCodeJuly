#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
"""
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits:
            return []
        strList = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = [""]
        ascii_0 = ord('0')
        for i in digits:
            tmpQueue = []
            for ele in queue:
                for j in strList[ord(i)-ascii_0]:
                    tmpQueue.append(ele + j)
            queue = tmpQueue
        return queue

if __name__ == '__main__':
    solution = Solution()
    print solution.letterCombinations("23")
    print solution.letterCombinations("")