#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
利用栈将中缀表达转换为后缀表达
"""
class Solution:
    def postfix(self, expression):
        stack = []
        isp = {}   # 栈内优先数
        icp = {}   # 栈外优先数
        isp['#'] = 0
        isp['('] = 1
        isp['*'] = 5
        isp['/'] = 5
        isp['%'] = 5
        isp['+'] = 3
        isp['-'] = 3
        isp[')'] = 6
        icp['#'] = 0
        icp['('] = 6
        icp['*'] = 4
        icp['/'] = 4
        icp['%'] = 4
        icp['+'] = 2
        icp['-'] = 2
        icp[')'] = 1
        stack.append('#')
        index = 0
        while stack:
            ascii = ord(expression[index])
            if 65 <= ascii <= 90:
                print expression[index]
                index += 1
            else:
                tmp_op = stack[-1]
                #print isp[tmp_op], icp[expression[index]]
                if isp[tmp_op] < icp[expression[index]]:
                    stack.append(expression[index])
                    index += 1
                elif isp[tmp_op] > icp[expression[index]]:
                    print stack.pop()
                else:
                    tmp_op = stack.pop()
                    if tmp_op == '(':
                        index += 1

if __name__ == '__main__':
    solution = Solution()
    expression = "A+B*C#"
    solution.postfix(expression)