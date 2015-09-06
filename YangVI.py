#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
利用队列打印二项展开式的系数
"""
import Queue

class Solution:
    def YangVI(self, n):
        queue = Queue.Queue(n+1)
        queue.put(1)
        queue.put(1)
        s, k = 0, 0
        for i in range(1, n):
            print
            queue.put(k)
            for j in range(1, i+3):
                t = queue.get()
                u = s + t
                queue.put(u)
                s = t
                if j != i+2:
                    print s,

    def YangVI2(self, n):
        queue = [0, 1, 0]
        for i in range(1, n+1):
            print
            tmp_queue = [0]
            for j in range(1, len(queue)):
                tmp_sum = queue[j-1] + queue[j]
                print tmp_sum,
                tmp_queue.append(tmp_sum)
            tmp_queue.append(0)
            queue = tmp_queue


if __name__ == '__main__':
    solution = Solution()
    solution.YangVI2(4)