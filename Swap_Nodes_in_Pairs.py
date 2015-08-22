#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
changed.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        tmp_head = ListNode(0)
        tmp_head.next = head
        tmp_node = tmp_head
        while tmp_node.next and tmp_node.next.next:
            node_next = tmp_node.next
            node_next_next = tmp_node.next.next
            node_next_next_next = tmp_node.next.next.next
            tmp_node.next = node_next_next
            node_next_next.next = node_next
            node_next.next = node_next_next_next
            tmp_node = node_next
        return tmp_head.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    tmp = head
    while tmp:
        print tmp.val
        tmp = tmp.next
    res_head = solution.swapPairs(head)
    while res_head:
        print res_head.val
        res_head = res_head.next