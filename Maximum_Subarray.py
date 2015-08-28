#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, max_sum = 0, -2147483648
        for i in nums:
            sum += i
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        return max_sum

    # 该方法比上面快！
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, max_sum = 0, -2147483648
        for i in nums:
            sum = i if sum < 0 else sum + i
            max_sum = max(max_sum, sum)
        return max_sum

if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print solution.maxSubArray(nums)
    print solution.maxSubArray([])
    print solution.maxSubArray([1])