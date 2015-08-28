#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or divisor == 0:
            return 0
        flag = False if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else True
        dividend = abs(dividend)
        divisor = abs(divisor)
        div_info = [0, divisor]
        coefficient_info = [0, 1]
        current_div = divisor
        current_coe = 1
        while current_div < dividend:
            current_div += current_div
            current_coe += current_coe
            div_info.append(current_div)
            coefficient_info.append(current_coe)
        res = 0
        for i in range(len(div_info)-1, 0, -1):
            if dividend >= div_info[i]:
                res += coefficient_info[i]
                dividend -= div_info[i]
        res = res if flag else -res
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        else:
            return res

if __name__ == '__main__':
    solution = Solution()
    print solution.divide(10, 2)
    print solution.divide(100, 3)
    print solution.divide(10, 0)
    print solution.divide(0, 2)
    print solution.divide(10, 100)