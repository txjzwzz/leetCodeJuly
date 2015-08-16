#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
all the input requirements up front.

"""
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if not str:
            return 0
        startIndex = 0
        while startIndex < len(str) and str[startIndex] == " ":
            startIndex += 1
        flag = True
        if startIndex < len(str) and (str[startIndex] == "+" or str[startIndex] == '-'):
            flag = not flag if str[startIndex] == "-" else flag
            startIndex += 1
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        res = 0
        ascii_0 = ord('0')
        ascii_9 = ord('9')
        while startIndex < len(str) and str[startIndex] != " ":
            if ord(str[startIndex]) > ascii_9 or ord(str[startIndex]) < ascii_0:
                break
            res = res * 10 + ord(str[startIndex]) - ascii_0
            startIndex += 1
        if res > INT_MAX and flag:
            return INT_MAX
        if not flag and -res < INT_MIN:
            return INT_MIN
        return res if flag else -res

if __name__ == '__main__':
    solution = Solution()
    print solution.myAtoi("123")
    print solution.myAtoi("   123  ")
    print solution.myAtoi("  -123")
    print solution.myAtoi("-123")
    print solution.myAtoi("+-+-123")
    print solution.myAtoi("   ")