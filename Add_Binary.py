#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexA = len(a)-1
        indexB = len(b)-1
        count = 0
        res = []
        while indexA >= 0 and indexB >= 0:
            sum = count + ord(a[indexA]) + ord(b[indexB]) - 96
            count = sum / 2
            res.append(str(sum % 2))
            indexA -= 1
            indexB -= 1
        while indexA >= 0:
            sum = count + ord(a[indexA]) - 48
            count = sum / 2
            res.append(str(sum % 2))
            indexA -= 1
        while indexB >= 0:
            sum = count + ord(b[indexB]) - 48
            count = sum / 2
            res.append(str(sum % 2))
            indexB -= 1
        if count != 0:
            res.append(str(1))
        res.reverse()
        return "".join(res)

if __name__ == '__main__':
    solution = Solution()
    a = ""
    b = "111"
    print solution.addBinary(a, b)
    a = "11"
    b = ""
    print solution.addBinary(a, b)
    a = "11"
    b = "1"
    print solution.addBinary(a, b)
