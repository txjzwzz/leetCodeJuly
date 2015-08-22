#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head1 = l1
        head2 = l2
        tmp_head = ListNode(0)
        tmp_node = tmp_head
        while head1 and head2:
            if head1.val < head2.val:
                tmp_node.next = head1
                head1 = head1.next
                tmp_node = tmp_node.next
            else:
                tmp_node.next = head2
                head2 = head2.next
                tmp_node = tmp_node.next
        while head1:
            tmp_node.next = head1
            head1 = head1.next
            tmp_node = tmp_node.next
        while head2:
            tmp_node.next = head2
            head2 = head2.next
            tmp_node = tmp_node.next
        return tmp_head.next
