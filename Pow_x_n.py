#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Implement pow(x, n).
"""
class Solution(object):
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True if n >= 0 else False
        n = abs(n)
        power_x = [x]
        index_list = [1]
        end_index, tmp_coe = 0, 1
        while tmp_coe * 2 <= n:
            power_x.append(power_x[end_index] * power_x[end_index])
            tmp_coe = tmp_coe * 2
            index_list.append(tmp_coe)
            end_index += 1
        res, index = 1, len(index_list)-1
        while index >= 0:
            if n >= index_list[index]:
                res *= power_x[index]
                n -= index_list[index]
            index -= 1
        return res if flag else 1.0 / res

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True if n >= 0 else False
        n = abs(n)
        tmp_power, tmp_coe, res = x, 1, 1
        while n > 0:
            minus = n % (tmp_coe * 2)
            if minus != 0:
                res = res * tmp_power
                n -= minus
            tmp_power *= tmp_power
            tmp_coe *= 2
        return res if flag else 1.0 / res

    # 本质上是看该位上面是否为1！这种问题要记得使用bit的思想！
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True if n >= 0 else False
        n = abs(n)
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res if flag else 1.0 / res


if __name__ == '__main__':
    solution = Solution()
    print solution.myPow(2, 0)
    print solution.myPow(2, 1)
    print solution.myPow(2, 2)
    print solution.myPow(2, 3)
    print solution.myPow(2, 4)
    print solution.myPow(2, 5)
    print solution.myPow(2, 6)
    print solution.myPow(0, 6)
    print solution.myPow(-2, 6)
    print solution.myPow(-2, 5)
    print solution.myPow(-1, 0)
    print solution.myPow(2, -1)
    print solution.myPow(34.00515, -3)