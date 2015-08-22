#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        parenthese_list = []
        match_map = {}
        match_map['('] = ')'
        match_map['['] = ']'
        match_map['{'] = '}'
        for i in s:
            if i == '(' or i == '{' or i == '[':
                parenthese_list.append(i)
            else:
                if not parenthese_list:
                    return False
                tmp = parenthese_list.pop()
                if i != match_map[tmp]:
                    return False
        return True if not parenthese_list else False

if __name__ == '__main__':
    solution = Solution()
    print solution.isValid("(()){}{}[][]{()[]}")
    print solution.isValid("([))")
    print solution.isValid("(()}")