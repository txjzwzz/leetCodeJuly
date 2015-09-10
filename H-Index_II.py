#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.binary_search(citations, 0, len(citations)-1)

    def binary_search(self, A, p, q):
        if p > q or A[q] < len(A)-q:
            return 0
        mid = p + ((q - p) >> 1)
        # search right is possible
        res = self.binary_search(A, p, mid-1)
        if res == 0:
            if A[mid] >= len(A)-mid and (mid == 0 or (mid>0 and A[mid-1] <= len(A)-mid)):
                return len(A)-mid
            else:
                return self.binary_search(A, mid+1, q)
        else:
            return res

if __name__ == '__main__':
    solution = Solution()
    citations = [0, 1, 3, 5, 6]
    print solution.hIndex(citations)
    print solution.hIndex([5, 5, 5])
    print solution.hIndex([])