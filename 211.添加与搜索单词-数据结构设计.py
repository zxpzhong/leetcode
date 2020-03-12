#
# @lc app=leetcode.cn id=211 lang=python
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (38.96%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 18.8K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
# 
# 示例:
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# 说明:
# 
# 你可以假设所有单词都是由小写字母 a-z 组成的。
# 
#

# @lc code=start
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word not in self.dict:
            try:
                self.dict[len(word)].append(word)
            except:
                self.dict[len(word)] = []
                self.dict[len(word)].append(word)
            
    def matchone(self, candi,word):
        if not len(candi) == len(word):
            return False
        for i in range(len(candi)):
            if not word[i] == '.':
                if not candi[i]  == word[i]:
                    return False
        return True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        try:
            for candi in self.dict[len(word)]:
                # 匹配单个字符candi和word
                if self.matchone(candi,word):
                    return True
        except:
            pass
        return False
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

solu = WordDictionary()
solu.addWord("bad")
solu.addWord("dad")
solu.addWord("mad")
print(solu.search("pad"))
print(solu.search("bad"))
print(solu.search(".ad"))
print(solu.search("b.."))
# ["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]