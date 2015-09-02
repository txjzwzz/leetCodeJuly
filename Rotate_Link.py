#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
使用循环链表解约瑟夫问题
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def solveJoseph(self, member_list, k):
        if not member_list:
            return
        first = ListNode(member_list[0])
        tmp = first
        for i in range(1, len(member_list)):
            tmp.next = ListNode(member_list[i])
            tmp = tmp.next
        tmp.next = first
        prev = tmp
        while prev.next != prev:
            for i in range(1, k):
                prev = prev.next
            print "本次出列为 " + str(prev.next.val)
            prev.next = prev.next.next
        return prev.val

if __name__ == '__main__':
    solution = Solution()
    member_list = [i for i in range(1, 10)]
    print solution.solveJoseph(member_list, 1)
    print solution.solveJoseph(member_list, 2)
    print solution.solveJoseph(member_list, 3)