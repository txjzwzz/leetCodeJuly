#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        valList = []
        opList = []
        startIndex = 0
        while startIndex < len(s):
            if s[startIndex] == '+':
                opList.append('+')
            elif s[startIndex] == '-':
                opList.append('-')
            elif s[startIndex] == '*':
                opList.append('*')
            elif s[startIndex] == '/':
                opList.append('/')
            elif s[startIndex] == ' ':
                pass
            else:
                tmpVal = ord(s[startIndex]) - 48
                while startIndex+1 < len(s) and ord(s[startIndex+1]) >= 48 and ord(s[startIndex+1]) <= 57:
                    tmpVal = tmpVal * 10 + ord(s[startIndex+1]) - 48
                    startIndex += 1
                if opList:
                    if opList[-1] == '*':
                        tmp = valList.pop()
                        tmpVal = tmp * tmpVal
                    elif opList[-1] == '/':
                        tmp = valList.pop()
                        tmpVal = tmp / tmpVal
                    if opList[-1] == '*' or opList[-1] == '/':
                        opList.pop()
                valList.append(tmpVal)
            startIndex += 1
        res = valList[0]
        startIndex = 0
        while startIndex < len(opList):
            if opList[startIndex] == '+':
                res += valList[startIndex+1]
            elif opList[startIndex] == '-':
                res -= valList[startIndex+1]
            startIndex += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    s = "3+20*2-10 + 9 / 3"
    print solution.calculate(s)
    s = '3 + 5 / 2'
    print solution.calculate(s)
    s = ""
    print solution.calculate(s)
    s = "10"
    print solution.calculate(s)

