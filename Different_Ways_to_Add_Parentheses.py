#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways
to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
# 本质是哪个运算先最后算的问题！
# 根据每个运算符来算
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        if not input:
            return []
        valList = []
        opList = []
        index = 0
        asc0 = ord('0')
        asc9 = ord('9')
        while index < len(input):
            if input[index] == '+' or input[index] == '-' or input[index] == '*':
                opList.append(input[index])
                index += 1
            elif ord(input[index]) >= asc0 and ord(input[index]) <= asc9:
                startIndex = index
                while index < len(input) and ord(input[index]) >= asc0 and ord(input[index]) <= asc9:
                    index += 1
                valList.append(int(input[startIndex:index]))
            else:
                index += 1
        matrix = [[[] for i in range(len(opList))] for j in range(len(opList))]
        return self.dfs(opList, valList, matrix, 0, len(opList)-1)

    def dfs(self, opList, valList, matrix, i, j):
        if i > j:
            return [valList[i]]
        if matrix[i][j]:
            return matrix[i][j]
        # i <= j
        res = []
        for k in range(i, j+1):
            left = self.dfs(opList, valList, matrix, i, k-1)
            right = self.dfs(opList, valList, matrix, k+1, j)
            for m in left:
                for n in right:
                    if opList[k] == '+':
                        res.append(m + n)
                    elif opList[k] == '-':
                        res.append(m - n)
                    else:  # *
                        res.append(m * n)
        matrix[i][j] = res
        return res


if __name__ == '__main__':
    solution = Solution()
    inputStr="2*3-4*5"
    print solution.diffWaysToCompute(inputStr)
    inputStr="2-1-1"
    print solution.diffWaysToCompute(inputStr)