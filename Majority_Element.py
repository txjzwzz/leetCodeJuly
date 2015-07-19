#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n / 2) times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        res = []
        for i in num:
            if not res:
                res.append(i)
            else:
                if res[len(res)-1] != i:
                    res.pop()
                else:
                    res.append(i)
        return res[0]


if __name__ == '__main__':
    a = [1]
    b = [1, 2, 3, 1, 1, 1, 4, 5, 6, 1, 1]
    c = [2, 3, 4, 5, 1, 1, 1, 1, 1]
    d = [1, 1, 1, 1, 1, 2, 3, 4, 5]
    solution = Solution()
    print solution.majorityElement(a)
    print solution.majorityElement(b)
    print solution.majorityElement(c)
    print solution.majorityElement(d)