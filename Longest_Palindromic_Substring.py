#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""
class Solution:
    # @param {string} s
    # @return {string}
    # def longestPalindrome(self, s):
    #     if not s:
    #         return ""
    #     matrix = [[False for i in range(len(s))] for j in range(len(s))]
    #     for i in range(len(s)):
    #         matrix[i][i] = True
    #     maxDis = 0
    #     for i in range(len(s)-1):
    #         if s[i] == s[i+1]:
    #             matrix[i][i+1] = True
    #             maxDis = 1
    #     distance = 2
    #     while distance < len(s):
    #         flag = False
    #         for i in range(len(s)-distance):
    #             if matrix[i+1][i+distance-1] == True and s[i] == s[i+distance]:
    #                 matrix[i][i+distance] = True
    #                 flag = True
    #         if flag:
    #             maxDis = distance
    #         distance += 1
    #     for i in range(len(s)-maxDis):
    #         if matrix[i][i+maxDis] == True:
    #             return s[i:i+maxDis+1]

    def longestPalindrome(self, s):
        if not s:
            return ""
        res = ""
        length = 0
        startIndex = 0
        while startIndex < len(s):
            endIndex = startIndex
            while endIndex < len(s) and s[endIndex] == s[startIndex]:
                endIndex += 1
            endIndex -= 1
            count = 0
            while startIndex-count-1 >= 0 and endIndex+count+1 < len(s) and s[startIndex-count-1] == s[endIndex+count+1]:
                count += 1
            if endIndex - startIndex + 2 * count + 1 > length:
                length = endIndex - startIndex + 2 * count
                res = s[startIndex-count:endIndex+count+1]
            startIndex = endIndex + 1
        return res



if __name__ == '__main__':
    solution = Solution()
    s = ""
    print solution.longestPalindrome(s)
    s = "a"
    print solution.longestPalindrome(s)
    s = "aaa"
    print solution.longestPalindrome(s)
    s = "aba"
    print solution.longestPalindrome(s)
    s = "abababababababc"
    print solution.longestPalindrome(s)