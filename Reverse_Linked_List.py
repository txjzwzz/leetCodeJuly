#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Reverse a singly linked list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        startNode = ListNode(0)
        while head != None:
            tmp = head.next
            head.next = startNode.next
            startNode.next = head
            head = tmp
        return startNode.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    solution = Solution()
    res = solution.reverseList(head)
    print res.val