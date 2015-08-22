#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        head_node = ListNode(0)
        head_node.next = head
        current_node = head_node
        flag = self.judge_nodes_none(current_node, k)
        while flag:
            tmp = current_node.next
            for i in range(k-1):
                tmp_node = tmp.next
                tmp_tail = tmp_node.next
                tmp.next = tmp_tail
                tmp_head = current_node.next
                current_node.next = tmp_node
                tmp_node.next = tmp_head
            current_node = tmp
            flag = self.judge_nodes_none(current_node, k)
        return head_node.next


    def judge_nodes_none(self, current_node, k):
        tmp = current_node
        for i in range(k):
            if not tmp.next:
                return False
            tmp = tmp.next
        return True


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
    res_head = solution.reverseKGroup(head, 3)
    while res_head:
        print res_head.val
        res_head = res_head.next