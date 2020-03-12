#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (61.50%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    26.3K
# Total Submissions: 40.3K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
# 示例:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 
# 说明:
# 
# 
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
# 
# 
#

# @lc code=start
# class Trie(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = []


#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         self.dict.append(word)

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         if word in self.dict:
#             return True
#         return False

#     def match_prefix(self,prefix,candi):
#         if len(candi) < len(prefix):
#             return False
#         for i in range(len(prefix)):
#             if not prefix[i] == candi[i]:
#                 return False
#         return True

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         for candi in self.dict:
#             # 匹配单个字符candi和word
#             # 只要开头可以匹配上就可以
#             if self.match_prefix(prefix,candi):
#                 return True
#         return False
#----------上面一段是傻子暴力解法

#----------尝试构建前缀树
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
trie = Trie()

["app"],["apple"],["beer"],["add"],["jam"],["rental"]

print(trie.insert("app"))
print(trie.insert("apple"))
print(trie.insert("beer"))
print(trie.insert("add"))
print(trie.insert("jam"))
print(trie.insert("rental"))
# print(trie.search("apple"))   
# print(trie.search("app"))    
print(trie.startsWith("jan")) 
# print(trie.insert("app"))   
# print(trie.search("app"))    