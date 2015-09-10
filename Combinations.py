#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        tmp_res = [0 for i in range(k)]
        self.get_combine(1, n, 0, k, tmp_res, res)
        return res

    def get_combine(self, i, n, index, k, tmp_res, res):
        if index == k:
            res.append(tmp_res[:])
            return
        for j in range(i, n+1):
            tmp_res[index] = j
            self.get_combine(j+1, n, index+1, k, tmp_res, res)

if __name__ == '__main__':
    solution = Solution()
    print solution.combine(4, 2)