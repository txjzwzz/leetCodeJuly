#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_length = len(strs[0])
        for i in strs:
            min_length = len(i) if len(i) < min_length else min_length
        res = ""
        for i in range(min_length):
            common_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != common_char:
                    return res
            res += common_char
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.longestCommonPrefix(["a", "a"])
    print solution.longestCommonPrefix(["abc", "addd"])
    print solution.longestCommonPrefix(["abc", "adc"])
    print solution.longestCommonPrefix(["aasd", "asdfa"])
    print solution.longestCommonPrefix(["", "a"])
    print solution.longestCommonPrefix(["a"])
    print solution.longestCommonPrefix(["abcd", "abce"])