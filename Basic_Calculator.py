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
        return self.singleCal(s)

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
                startIndex += 1
                # 每等到一个)就处理这个对应的(，使得这个括号成为一个值加入到valList中间去
                tmpValList = [valList.pop()]
                tmpOpList = []
                tmpOp = opList.pop()
                while (tmpOp != '('):
                    tmpOpList.append(tmpOp)
                    tmpValList.append(valList.pop())
                    tmpOp = opList.pop()
                valList.append(self.calValue(tmpValList, tmpOpList))
            else:
                endIndex = startIndex
                while endIndex < len(s) and ord(s[endIndex]) >= 48 and ord(s[endIndex]) <= 57:
                    endIndex += 1
                valList.append(int(s[startIndex : endIndex]))
                startIndex = endIndex
        if not valList:
            return 0
        startIndex = 0
        res = valList[0]
        while startIndex < len(opList):
            if opList[startIndex] == '+':
                res = res + valList[startIndex+1]
            else:
                res = res - valList[startIndex+1]
            startIndex = startIndex + 1
        return res


    # 不包含一个括号，计算一个简单的表达时
    def calValue(self, valList, opList):
        if not valList:
            return 0
        res = valList.pop()
        while valList:
            if opList.pop() == '+':
                res = res + valList.pop()
            else:
                res = res - valList.pop()
        return res

if __name__ == '__main__':
    solution = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    print solution.calculate(s)
    s = "1+1-1"
    print solution.calculate(s)
    s = "1+(4+5+2)-3+(6+8)"
    print solution.calculate(s)
    s = "(1+(4+5+2)-3)+6+8"
    print solution.calculate(s)
    s = "(3)+1"
    print solution.calculate(s)
