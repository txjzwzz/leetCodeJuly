#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        index = len(s)-1
        while index >= 0 and s[index] == ' ':
            index -= 1
        tmp_index = index
        while tmp_index >= 0 and s[tmp_index] != ' ':
            tmp_index -= 1
        return index - tmp_index


if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLastWord("Hello World")
    print solution.lengthOfLastWord(" Hello World ")
    print solution.lengthOfLastWord("World")
    print solution.lengthOfLastWord(" World ")
    print solution.lengthOfLastWord(" ")
    print solution.lengthOfLastWord("")
    print solution.lengthOfLastWord("s")
    print solution.lengthOfLastWord(" s ")
    print solution.lengthOfLastWord("s ")
