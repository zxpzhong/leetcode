#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (36.99%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    23.6K
# Total Submissions: 58.8K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
    #     self.endWord = endWord
    #     return self.change_one([beginWord],[wordList],0)

    # def sub_one(self,str1,str2):
    #     sum = 0
    #     for i in range(len(str1)):
    #         if not str1[i] == str2[i]:
    #             sum+=1
    #     return True if sum == 1 else False

    # def change_one(self,cur_list,wordList,k):
    #     new_cur_list = []
    #     new_wordList = []
    #     for i,cur in enumerate(cur_list):
    #         for j,wordlst in enumerate(wordList[i]):
    #             if self.sub_one(cur,wordlst):
    #                 new_cur_list.append(wordlst)
    #                 if wordlst == self.endWord:
    #                     return k+2
    #                 new_wordList.append(wordList[i][:j]+wordList[i][j+1:])
    #     if len(new_wordList) == 0:
    #         return 0
    #     elif len(new_wordList[0]) == 0:
    #         return 0
    #     return self.change_one(new_cur_list,new_wordList,k+1)
        # 上面是自己的超时了
        # 建立通用list
        from collections import defaultdict
        from collections import deque
        size, general_dic = len(beginWord), defaultdict(list)
        for w in wordList:
            for _ in range(size):
                general_dic[w[:_]+"*"+w[_+1:]].append(w)
        # BFS
        queue = deque()
        queue.append((beginWord, 1))  # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了，要区分层就要queue中直接加入当前node所属层数。
        mark_dic = defaultdict(bool)  # bool 的默认值是false，因此所有不在list里的是false
        mark_dic[beginWord] = True
        while queue:
            cur_word, level = queue.popleft()   # queue头出来一个
            for i in range(size):               # 找邻居，这里的所有邻居都在level+1层
                for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                    if neighbour == endWord: return level + 1
                    if not mark_dic[neighbour]:
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level+1))  #符合条件（neighbour + unmarked)的进去
        return 0

        

# @lc code=end
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
solu = Solution()
print(solu.ladderLength(beginWord, endWord, wordList))
