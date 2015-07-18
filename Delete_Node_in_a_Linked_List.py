#-*- coding=utf-8 -*-
"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
"""

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        node.val = node.next.val
        while node.next.next is not None:
            node = node.next
            node.val = node.next.val
        node.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    solution = Solution()
    s4 = ListNode(4)
    s3 = ListNode(3)
    s2 = ListNode(2)
    s1 = ListNode(1)
    s1.next = s2
    s2.next = s3
    s3.next = s4
    solution.deleteNode(s3)
    tmp = s1
    while tmp is not None:
        print tmp.val
        tmp = tmp.next

