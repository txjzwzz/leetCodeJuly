#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

暂时思路：分解，按照每个数位上面1出现的次数来算
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n < 1:
            return 0
        analy = []
        tmp = n
        while tmp > 0:
            analy.append(tmp % 10)
            tmp = tmp / 10
        # 标记之前位数的值
        prev = 0
        count = 0
        for i in range(len(analy)-1, -1, -1):
            if analy[i] == 0:
                count = count + prev * (pow(10, i))
            elif analy[i] > 1:
                count = count + (prev + 1) * pow(10, i)
            else:
                tmpCount = 0
                for j in range(i-1, -1, -1):
                    tmpCount = tmpCount * 10 + analy[j]
                count = count + prev * (pow(10, i)) + tmpCount + 1
            prev = prev * 10 + analy[i]
        return count

if __name__ == '__main__':
    solution = Solution()
    print solution.countDigitOne(20)