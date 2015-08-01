#-*- coding=utf-8 -*-
__author__ = 'txjzw'
"""
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
For example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class WordDictionary:

    # initialize your data structure here.
    def __init__(self):
        self.first_dict = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    # 为了避免产生输入and 搜索an为true的情况，必须加入结束符，设定为end
    def addWord(self, word):
        if not word:
            return
        stage_dict = self.first_dict
        for i in range(len(word)+1):
            if i == len(word):
                stage_dict["end"] = "stop"
            else:
                if word[i] not in stage_dict:
                    stage_dict[word[i]] = {}
                stage_dict = stage_dict[word[i]]

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if not word:
            return False
        stage_dict = self.first_dict
        return self.deepSearch(word, 0, stage_dict)

    def deepSearch(self, word, index, stage_dict):
        if index == len(word):
            if "end" in stage_dict:
                return True
            return False
        if word[index] == '.':
            # 这里要注意，有可能有"end"存在
            for i in stage_dict:
                if i == "end":
                    continue
                if self.deepSearch(word, index+1, stage_dict[i]):
                    return True
            return False
        else:
            if word[index] in stage_dict:
                return self.deepSearch(word, index+1, stage_dict[word[index]])
            else:
                return False



# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    solution = WordDictionary()
    solution.addWord("bad")
    solution.addWord("dad")
    solution.addWord("mad")
    print solution.search("pad")
    print solution.search("bad")
    print solution.search(".ad")
    print solution.search("b..")
    print solution.search("")
    print "Second:#################################"
    solution = WordDictionary()
    solution.addWord("at")
    solution.addWord("and")
    solution.addWord("an")
    solution.addWord("add")
    print solution.search("a")
    print solution.search(".at")
    solution.addWord("bat")
    print solution.search(".at")
    print solution.search("an.")
    print solution.search("a.d.")
    print solution.search("b.")
    print solution.search("a.d")
    print solution.search(".")