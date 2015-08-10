#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        addHead = ListNode(0)
        tmpNode = addHead
        while head:
            tmp = head
            head = head.next
            tmp.next = None
            if tmp.val != val:
                tmpNode.next = tmp
                tmpNode = tmpNode.next
        return addHead.next