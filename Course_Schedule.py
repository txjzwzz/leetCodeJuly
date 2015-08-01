#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0
you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
"""
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses <= 0 or not prerequisites:
            return True
        needDict = {}
        for i in prerequisites:
            if len(i) == 2:
                if i[0] in needDict:
                    needDict[i[0]].append(i[1])
                else:
                    needDict[i[0]] = [i[1]]
        while True:
            edit = False
            for key in needDict.keys():
                for val in needDict[key]:
                    if val not in needDict:
                        needDict[key].remove(val)
                        edit = True
                if len(needDict[key]) == 0:
                    needDict.pop(key)
            if not needDict:
                return True
            if not edit:
                return False

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[0, 1]]
    solution = Solution()
    print solution.canFinish(numCourses, prerequisites)
    prerequisites = [[0, 1], [1, 0]]
    print solution.canFinish(numCourses, prerequisites)