#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""
# 光数数量不看顺序是不行的！
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if s == None or t == None or len(s) != len(t):
            return False
        mapDictForword = {}
        mapDictBackword = {}
        for i in range(len(s)):
            if s[i] not in mapDictForword:
                if t[i] not in mapDictBackword:
                    mapDictForword[s[i]] = t[i]
                    mapDictBackword[t[i]] = s[i]
                else:
                    return False
            else:
                if t[i] != mapDictForword[s[i]]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "egg"
    t = "add"
    print solution.isIsomorphic(s, t)
    s = "foo"
    t = "bar"
    print solution.isIsomorphic(s, t)
    s = "paper"
    t = "title"
    print solution.isIsomorphic(s, t)
    s = ""
    t = ""
    print solution.isIsomorphic(s, t)