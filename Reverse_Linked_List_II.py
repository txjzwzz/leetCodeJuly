#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        tmp_head = ListNode(-1)
        tmp_head.next = head
        prev = tmp_head
        # go to prev node
        for i in range(m-1):
            prev = prev.next
        start_node = prev.next
        for i in range(m, n):
            tmp = prev.next
            prev.next = start_node.next
            start_node.next = start_node.next.next
            prev.next.next = tmp
        return tmp_head.next