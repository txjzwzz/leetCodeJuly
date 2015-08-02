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
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        if not input:
            return 0
        valList = []
        opList = []
        startIndex = 0
        for i in input:
            if i == '+' or i == '-' or i == '*':
                opList.append(i)
                if input[startIndex:i]:
                    valList.append(int(input[startIndex:i]))
                startIndex = startIndex + 1
        res = [valList[0]]
        for i in