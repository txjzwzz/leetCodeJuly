#-*- coding=utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
__author__ = 'zz'
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start_index = 0
        end_index = len(s)-1
        while start_index < end_index:
            while start_index < end_index and (ord(s[start_index]) < 48 or ord(s[start_index]) > 90 or
                                                   (ord(s[start_index]) > 57 and ord(s[start_index]) < 65)):
                start_index += 1
            while start_index < end_index and (ord(s[end_index]) < 48 or ord(s[end_index]) > 90 or
                                                   (ord(s[end_index]) > 57 and ord(s[end_index]) < 65)):
                end_index -= 1
            print s[start_index].upper(), s[end_index].upper()
            if start_index < end_index and s[start_index].upper() != s[end_index].upper():
                return False
            start_index += 1
            end_index -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome("A man, a plan, a canal: Panama")