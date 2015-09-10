#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        matrix = [1 for i in range(len(s)+1)]
        asc_6 = ord('6')
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2': # invalid
                    return 0
                else:
                    matrix[i+1] = matrix[i-1]
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and ord(s[i]) <= asc_6):
                    matrix[i+1] = matrix[i] + matrix[i-1]
                else :
                    matrix[i+1] = matrix[i]
        return matrix[len(s)]

if __name__ == '__main__':
    solution = Solution()
    print solution.numDecodings("12")