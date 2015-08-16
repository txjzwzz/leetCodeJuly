#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        dictlist = {}
        dictlist['M'] = 1000
        dictlist['CM'] = 900
        dictlist['D'] = 500
        dictlist['CD'] = 400
        dictlist['C'] = 100
        dictlist['XC'] = 90
        dictlist['L'] = 50
        dictlist['XL'] = 40
        dictlist['X'] = 10
        dictlist['IX'] = 9
        dictlist['V'] = 5
        dictlist['IV'] = 4
        dictlist['I'] = 1
        res = 0
        startIndex = 0
        while startIndex < len(s):
            if startIndex+1 < len(s) and s[startIndex:startIndex+2] in dictlist:
                res += dictlist[s[startIndex:startIndex+2]]
                startIndex += 2
            else:
                res += dictlist[s[startIndex]]
                startIndex += 1
        return res

    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        dictlist = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ansList = []
        for key in range(len(keys)):
            for i in range(num/keys[key]):
                ansList.append(dictlist[key])
            num -= num/keys[key]*keys[key]
        return "".join(ansList)

if __name__ == '__main__':
    solution = Solution()
    print solution.romanToInt(solution.intToRoman(1))
    print solution.romanToInt(solution.intToRoman(2))
    print solution.romanToInt(solution.intToRoman(3))
    print solution.romanToInt(solution.intToRoman(4))
    print solution.romanToInt(solution.intToRoman(5))
    print solution.romanToInt(solution.intToRoman(9))
    print solution.romanToInt(solution.intToRoman(10))
    print solution.romanToInt(solution.intToRoman(11))
    print solution.romanToInt(solution.intToRoman(999))
    print solution.romanToInt(solution.intToRoman(3999))