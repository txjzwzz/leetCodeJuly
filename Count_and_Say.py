#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        res_list = ['1']
        for i in range(1, n):
            tmp_list = []
            count = 1
            for j in range(len(res_list)):
                if j == len(res_list)-1 or res_list[j] != res_list[j+1]:
                    tmp_list.append(str(count))
                    tmp_list.append(res_list[j])
                    count = 1
                else:
                    count += 1
            res_list = tmp_list
        return ''.join(res_list)

if __name__ == '__main__':
    solution = Solution()
    print solution.countAndSay(1)
    print solution.countAndSay(2)
    print solution.countAndSay(3)
    print solution.countAndSay(4)
    print solution.countAndSay(5)
    print solution.countAndSay(6)