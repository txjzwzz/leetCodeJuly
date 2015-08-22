#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear
exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
# 思路：想办法把两个单独的数字分到不同的组群中间去
# 由于两个单独的数字总有不同的位数，找到最低的不同位数，也就是xor结果中间第一个为1的位数
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor_two = 0
        for i in nums:
            xor_two ^= i
        # find first 1
        bitmap = xor_two & (-xor_two)
        res = [0, 0]
        for i in nums:
            if i & bitmap:
                res[0] ^= i
            else:
                res[1] ^= i
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.singleNumber([0, 1])
    print solution.singleNumber([1, 1, 0, 2, 3, 2])