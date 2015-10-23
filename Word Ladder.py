#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # if not beginWord or not endWord or len(beginWord) != len(endWord):
        #     return 0
        # queue, length = [beginWord], 1
        # while queue:
        #     tmp_queue = []
        #     for word in queue:
        #         for j in range(len(word)):
        #             for ch in 'abcdefghijklmnopqrstuvwxyz':
        #                 tmp_word = word[:j] + ch + word[j+1:]
        #                 if tmp_word == endWord:
        #                     return length + 1
        #                 if tmp_word in wordList:
        #                     tmp_queue.append(tmp_word)
        #                     wordList.remove(tmp_word)
        #     queue = tmp_queue[:]
        #     length += 1
        # return 0
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordList & (set(word[:index] + ch + word[index+1:] for word in front
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordList -= front
        return 0

if __name__ == '__main__':
    beginWord=  "hit"
    endWord = "cog"
    wordList = set(["hot","dot","dog","lot","log"])
    solution = Solution()
    print solution.ladderLength(beginWord, endWord, wordList)