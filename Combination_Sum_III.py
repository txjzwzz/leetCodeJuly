#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.
Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if k > 9 or k < 1 or n < 0:
            return []
        maxVal = 0
        minVal = 0
        for i in range(1, k+1):
            minVal += i
            maxVal += (10 - i)
        if n < minVal or n > maxVal:
            return []
        res = []
        for i in range(9, k-1, -1):
            tmpRes = self.dep(i, 0, k, n)
            if tmpRes:
                for tmp in tmpRes:
                    res.append(tmp)
        return res

    def dep(self, index, tmpk, k, n):
        if tmpk >= k or index > n or index < (k - tmpk):
            return []
        if tmpk == k-1:
            if index != n:
                return []
            else:
                return [[index]]
        res = []
        for i in range(index-1, 0, -1):
            if i > n - index:
                continue
            tmpRes = self.dep(i, tmpk+1, k, n-index)
            if tmpRes:
                for tmp in tmpRes:
                    tmp.append(index)
                    res.append(tmp)
        return res

if __name__ == '__main__':
    solution = Solution()
    k = 3
    n = 7
    print solution.combinationSum3(k, n)
    k = 3
    n = 9
    print solution.combinationSum3(k, n)
    k = 3
    n = 6
    print solution.combinationSum3(k, n)