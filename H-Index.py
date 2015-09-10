#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the
researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the
remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        matrix = [0 for i in range(length+2)]
        for i in citations:
            if i > length:
                matrix[length+1] += 1
            else:
                matrix[i] += 1
        large_amount = matrix[length+1]+matrix[length]
        for i in range(length, 0, -1):
            if large_amount >= i:
                return i
            else:
                large_amount += matrix[i-1]
        return 0

    #     citations.sort(reverse=True)
    #     return self.binary_search(citations, 0, len(citations)-1)
    #
    # def binary_search(self, A, p, q):
    #     if p > q or A[p] < p+1:
    #         return 0
    #     mid = p + ((q - p) >> 1)
    #     # search right is possible
    #     res = self.binary_search(A, mid+1, q)
    #     if res == 0:
    #         if A[mid] >= mid+1 and (mid+1 >= len(A) or (mid+1 < len(A) and A[mid+1] <= mid+1)):
    #             return mid+1
    #         else:
    #             return self.binary_search(A, p, mid-1)
    #     else:
    #         return res

if __name__ == '__main__':
    solution = Solution()
    citations = [3, 0, 6, 1, 5]
    print solution.hIndex(citations)
    print solution.hIndex([5, 5, 5])
    print solution.hIndex([])
    print solution.hIndex([1])
    print solution.hIndex([0, 1])
