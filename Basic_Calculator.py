#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        self.singleCal(s)

    # 计算单元的表达式的值，也就是没有括号的表达式的值
    def singleCal(self, s):
        valList = []
        opList = []
        startIndex = 0
        while startIndex < len(s):
            if s[startIndex] == ' ':
                startIndex += 1
            elif s[startIndex] == '+':
                opList.append('+')
                startIndex += 1
            elif s[startIndex] == '-':
                opList.append('-')
                startIndex += 1
            elif s[startIndex] == '(':
                opList.append('(')
                startIndex += 1
            elif s[startIndex] == ')':
                opList.append(')')
                startIndex += 1
            else:
                endIndex = startIndex
                while endIndex < len(s) and ord(s[endIndex]) >= 48 and ord(s[endIndex]) <= 57:
                    endIndex += 1
                print "str: " + s[startIndex: endIndex]
                valList.append(int(s[startIndex : endIndex]))
                startIndex = endIndex + 1
        print valList
        print opList
        if not valList:
            return 0


    def calValue(self, valList, opList):
        res = valList[0]
        startIndex = 0
        while startIndex < len(opList):
            if opList[startIndex] == '+':
                res = res + valList[startIndex + 1]
            elif opList[startIndex] == '-':
                res = res - valList[startIndex + 1]
            elif opList[startIndex] == '+':
                conOpNum = 1
                endIndex = startIndex + 1
                while opList[]

if __name__ == '__main__':
    solution = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    solution.calculate(s)