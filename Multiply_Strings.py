#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ""
        list_num1 = [ord(i)-48 for i in num1]
        list_num2 = [ord(i)-48 for i in num2]
        tmp_sum_list = [[0], list_num1]
        tmp_sum = list_num1
        for i in range(8):
            tmp_sum = self.add_offset(tmp_sum, list_num1, 0)
            tmp_sum_list.append(tmp_sum)
        res = []
        for i in range(len(num2)-1, -1, -1):
            res = self.add_offset(res, tmp_sum_list[list_num2[i]], len(num2)-1-i)
        flag = False
        for i in range(len(res)):
            if res[i] != 0:
                flag = True
            res[i] = str(res[i])
        return ''.join(res) if flag else "0"


    def add_offset(self, num1, num2, offset):
        res = []
        if offset < len(num1):
            res = num1[len(num1)-offset:]
            res.reverse()
        else:
            res = num1[:]
            res.reverse()
            for i in range(0, offset-len(num1)):
                res.append(0)
        index = 0
        count = 0
        while len(num1)-1-offset-index >= 0 and len(num2)-1-index >= 0:
            tmp_sum = num1[len(num1)-1-offset-index] + num2[len(num2)-1-index] + count
            res.append(tmp_sum % 10)
            count = tmp_sum / 10
            index += 1
        while len(num1)-1-offset-index >= 0:
            tmp_sum = num1[len(num1)-1-offset-index] + count
            res.append(tmp_sum % 10)
            count = tmp_sum / 10
            index += 1
        while len(num2)-1-index >= 0:
            tmp_sum = num2[len(num2)-1-index] + count
            res.append(tmp_sum % 10)
            count = tmp_sum / 10
            index += 1
        if count != 0:
            res.append(count)
        res.reverse()
        return res

if __name__ == '__main__':
    solution = Solution()
    num1 = [1,2,3,4]
    num2 = [1]
    num3 = [1,2,3,4]
    num4 = [1,2,3,4,5]
    print solution.add_offset(num1, num2, 0)
    print solution.add_offset(num1, num3, 0)
    print solution.add_offset(num1, num4, 0)
    print solution.add_offset(num1, num2, 3)
    print solution.add_offset(num1, num2, 5)
    num1 = "1234"
    num2 = "1"
    print solution.multiply(num1, num2)
    num2 = "5"
    print solution.multiply(num1, num2)
    num2 = "10"
    print solution.multiply(num1, num2)
    num2 = "15"
    print solution.multiply(num1, num2)
    num2 = "55"
    print solution.multiply(num1, num2)
    print solution.multiply("0", "55")
