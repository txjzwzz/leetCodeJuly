#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if s == None or t == None or len(s) != len(t):
            return False
        chars = [0 for i in range(26)]
        numA = ord('a')
        for i in range(len(s)):
            chars[ord(s[i])-numA] += 1
            chars[ord(t[i])-numA] -= 1
        for i in chars:
            if i != 0:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print solution.isAnagram(s, t)
    s = "rat"
    t = "car"
    print solution.isAnagram(s, t)
    s = ""
    t = ""
    print solution.isAnagram(s, t)
    s = None
    t = ""
    print solution.isAnagram(s, t)
