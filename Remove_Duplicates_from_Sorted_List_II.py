#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original
list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp_head = ListNode(-1)
        tmp_head.next = head
        prev = tmp_head
        while prev.next:
            if not prev.next.next or prev.next.val != prev.next.next.val:
                prev = prev.next
            else:
                tmp_node = prev.next
                while tmp_node.next and tmp_node.val == tmp_node.next.val:
                    tmp_node = tmp_node.next
                prev.next = tmp_node.next
        return tmp_head.next