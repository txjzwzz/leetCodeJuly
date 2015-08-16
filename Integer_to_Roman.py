#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
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
    print solution.intToRoman(1)
    print solution.intToRoman(3)
    print solution.intToRoman(5)
    print solution.intToRoman(7)
    print solution.intToRoman(9)
    print solution.intToRoman(11)
    print solution.intToRoman(41)
    print solution.intToRoman(51)
    print solution.intToRoman(91)
