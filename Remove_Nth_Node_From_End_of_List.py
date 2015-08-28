#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head or n < 1:
            return head
        tmp_head = ListNode(0)
        tmp_head.next = head
        node_first = tmp_head
        node_second = tmp_head
        for i in range(n):
            node_first = node_first.next
        while node_first.next:
            node_first = node_first.next
            node_second = node_second.next
        node_second.next = node_second.next.next
        return tmp_head.next

if __name__ == '__main__':
    head = ListNode(1)
    solution = Solution()
    res = solution.removeNthFromEnd(head, 1)
    print res.val
