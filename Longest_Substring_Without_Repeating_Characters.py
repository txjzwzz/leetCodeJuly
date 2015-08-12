#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
substring is "b", with the length of 1.
"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        startIndex = -1
        res = 0
        characterDict = {}
        for i in range(len(s)):
            if s[i] not in characterDict:
                res = max(res, i-startIndex)
            else:
                res = max(res, min(i-startIndex, i-characterDict[s[i]]))
                startIndex = max(startIndex, characterDict[s[i]])
            characterDict[s[i]] = i
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring("bbbb")
    print solution.lengthOfLongestSubstring("d")
    print solution.lengthOfLongestSubstring("abcabcbb")
    print solution.lengthOfLongestSubstring("aabbccdd")
    print solution.lengthOfLongestSubstring("abcdabc")
    print solution.lengthOfLongestSubstring("aab")