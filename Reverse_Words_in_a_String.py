#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s:
            return ""
        endIndex = len(s)
        res = []
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if i+1 < len(s) and s[i+1:endIndex]:
                    res.append(s[i+1:endIndex])
                endIndex = i
            else:
                if i == 0 and s[i:endIndex]:
                    res.append(s[i:endIndex])
        print res
        return " ".join(res)

if __name__ == '__main__':
    solution = Solution()
    s = "the sky is blue"
    print solution.reverseWords(s)