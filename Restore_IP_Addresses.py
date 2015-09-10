#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, tmp_res = [], []
        self.sol(s, 0, 0, tmp_res, res)
        return res

    def sol(self, s, index, start_index, tmp_res, res):
        if index == 3:
            if int(s[start_index:]) <= 255:
                if s[start_index:] == '0' or s[start_index] != '0':
                    tmp_res.append(s[start_index:])
                    res.append('.'.join(tmp_res[:]))
                    tmp_res.pop()
            return
        if start_index < len(s) and s[start_index] == '0':
            if start_index < len(s)-3+index:
                tmp_res.append('0')
                self.sol(s, index+1, start_index+1, tmp_res, res)
                tmp_res.pop()
            return
        for i in range(0, 3):
            if start_index+i < len(s)-(3-index) and int(s[start_index:start_index+i+1]) <= 255:
                    tmp_res.append(s[start_index:start_index+i+1])
                    self.sol(s, index+1, start_index+i+1, tmp_res, res)
                    tmp_res.pop()

if __name__ == '__main__':
    solution = Solution()
    s = "25525511135"
    print solution.restoreIpAddresses(s)
    print solution.restoreIpAddresses("")
    print solution.restoreIpAddresses("111")
    print solution.restoreIpAddresses("1111")
    print solution.restoreIpAddresses("0000")
    print solution.restoreIpAddresses("010010")