#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is
empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
(double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        if not self.queue:
            return
        tmpQueue = []
        while len(self.queue) > 1:
            tmpQueue.append(self.queue[0])
            self.queue = self.queue[1:]
        self.queue = tmpQueue

    # @return an integer
    def top(self):
        return self.queue[len(self.queue)-1]

    # @return an boolean
    def empty(self):
        if self.queue:
            return False
        else:
            return True

if __name__ == '__main__':
    solution = Stack()
    print solution.empty()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    solution.push(4)
    solution.push(5)
    print solution.top()
    solution.pop()
    print solution.top()
    solution.pop()
    print solution.top()
    solution.pop()
    print solution.top()
    solution.pop()
    print solution.top()
    solution.pop()
    print solution.empty()
