#-*- coding=utf-8 -*-
__author__ = 'zz'
"""
Implement a trie with insert, search, and startsWith methods.
"""
class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val):
        self.val = val
        self.freq = 0
        self.child = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("root")

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if not word:
            return
        currentNode = self.root
        for i in word:
            if i not in currentNode.child:
                currentNode.child[i] = TrieNode(i)
            currentNode = currentNode.child[i]
        currentNode.freq += 1

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        if not word:
            return False
        currentNode = self.root
        for i in word:
            if i not in currentNode.child:
                return False
            currentNode = currentNode.child[i]
        if currentNode.freq > 0:
            return True
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if not prefix:
            return False
        currentNode = self.root
        for i in prefix:
            if i not in currentNode.child:
                return False
            currentNode = currentNode.child[i]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    solution = Trie()
    solution.insert("a")
    solution.insert("and")
    solution.insert("as")
    solution.insert("abcd")
    solution.insert("bcfa")
    solution.insert("na")
    solution.insert("after")
    solution.insert("avoid")
    solution.insert("cba")
    solution.insert("nba")
    print solution.search("and")
    print solution.search("af")
    print solution.search("avoid")
    print solution.search("nbc")
    print solution.startsWith("a")
    print solution.startsWith("an")
    print solution.startsWith("ba")