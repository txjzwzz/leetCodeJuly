#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        while self:
            print self.val,
            self = self.next
        print

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        tmp_head = ListNode(-1)
        tmp_head.next = head
        length = 0
        index = tmp_head
        # index point to the last point
        while index.next != None:
            length += 1
            index = index.next
        k = k % length
        if k == 0:
            return head
        index1 = head
        for i in range(length-k-1):
            index1 = index1.next
        tmp_head.next = index1.next
        index1.next = None
        index.next = head
        return tmp_head.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 0)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 1)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 2)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 3)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 4)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 5)
    res.print_list()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.rotateRight(head, 6)
    res.print_list()