#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        tmp_fast, tmp_slow = head, head
        while tmp_fast and tmp_fast.next:
            tmp_slow = tmp_slow.next
            tmp_fast = tmp_fast.next.next
            if tmp_fast == tmp_slow:
                return False
        return True