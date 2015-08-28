#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        if strs:
            strs.sort()
        for i in strs:
            str_list = list(i)
            str_list.sort()
            sorted_str = "".join(str_list)
            if sorted_str in dict:
                dict[sorted_str].append(i)
            else:
                dict[sorted_str] = [i]
        res = []
        for i in dict:
            res.append(dict[i])
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print solution.groupAnagrams([])