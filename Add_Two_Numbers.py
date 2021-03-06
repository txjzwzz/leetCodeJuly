#-*- coding=utf-8 -*-
__author__ = 'txjzw'

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        startNode = ListNode(0)
        tmp = startNode
        addBit = 0
        while l1 != None and l2 != None:
            tmp.next = ListNode((l1.val+l2.val+addBit) % 10)
            addBit = (l1.val+l2.val+addBit) / 10
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next
        l = l1 if l1 != None else l2
        while l != None:
            tmp.next = ListNode((l.val+addBit) % 10)
            addBit = (l.val+addBit) / 10
            l = l.next
            tmp = tmp.next
        if addBit != 0:
            tmp.next = ListNode(addBit)
            tmp = tmp.next
        return startNode.next