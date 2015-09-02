#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        index, length = 0, len(path)
        for i in range(1, length+1):
            if i == length or path[i] == '/':
                tmp_s = path[index+1:i]
                if not tmp_s:
                    pass
                elif tmp_s == '.':
                    pass
                elif tmp_s == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(tmp_s)
                index = i
        res = ""
        if not stack:
            return '/'
        for i in stack:
            res = res + "/" + i
        return res

if __name__ == '__main__':
    solution = Solution()
    path = "/a/./b/../../c/"
    print solution.simplifyPath(path)
    path = "/home/"
    print solution.simplifyPath(path)
    path = "/../"
    print solution.simplifyPath(path)
    path = ""
    print solution.simplifyPath(path)
    path = "///"
    print solution.simplifyPath(path)
    path = "/..."
    print solution.simplifyPath(path)
    path = "/./"
    print solution.simplifyPath(path)