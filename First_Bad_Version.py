#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 1:
        return False
    return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(1, n)

    def binary_search(self, p, q):
        if p > q:
            return -1
        mid = p + ((q-p) >> 1)
        if isBadVersion(mid) == False:
            if mid == 1 or isBadVersion(mid-1) == True:
                return mid
            else:
                return self.binary_search(p, mid-1)
        else:
            return self.binary_search(mid+1, q)

if __name__ == '__main__':
    solution = Solution()
    print solution.firstBadVersion(1)
    print solution.firstBadVersion(2)
    print solution.firstBadVersion(3)