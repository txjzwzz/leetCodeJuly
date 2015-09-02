#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        coef = [1 for i in range(n)]
        index = [i+1 for i in range(n)]
        for i in range(1,n):
            coef[i] = coef[i-1] * i
        res = ""
        for i in range(n-1, -1, -1):
            coe = k / coef[i]
            res+=(str(index.pop(coe)))
            k -= coe * coef[i]
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.getPermutation(3, 6)
    print solution.getPermutation(1, 1)
    print solution.getPermutation(2, 1)
    print solution.getPermutation(2, 2)