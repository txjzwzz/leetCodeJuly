#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the
candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        res = []
        candidates.sort()
        # 利用哈希过滤重复项
        filterDict = {}
        for i in range(len(candidates)-1, -1, -1):
            tmpRes = self.calculate(candidates, target, i)
            if tmpRes:
                for tmp in tmpRes:
                    tmpVal = self.hashVal(tmp)
                    if not filterDict.has_key(tmpVal):
                        res.append(tmp)
                        filterDict[tmpVal] = 1
        return res

    def calculate(self, candidates, target, index):
        if candidates[index] > target:
            return []
        res = []
        if candidates[index] == target:
            res.append([candidates[index]])
            return res
        for i in range(index-1, -1, -1):
            subRes = self.calculate(candidates, target-candidates[index], i)
            if subRes:
                for tmp in subRes:
                    tmp.append(candidates[index])
                    res.append(tmp)
        return res

    def hashVal(self, resList):
        res = 0
        for i in resList:
            res = res * 10 + i
        return res

if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print solution.combinationSum2(candidates, target1)