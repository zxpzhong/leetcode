#
# @lc app=leetcode.cn id=140 lang=python
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (37.50%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 29.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#

# @lc code=start
# from typing import List 
from collections import deque
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
    #     self.wordDict = wordDict
    #     self.ans = []
    #     self.cutone(s,'')
    #     for i in range(len(self.ans)):
    #         self.ans[i] = self.ans[i][1:]
    #     return self.ans
        
    # def cutone(self,s,candi):
    #     length = len(s)
    #     if length == 0:
    #         self.ans.append(candi)
    #     for i in range(1,length+1):
    #         if s[:i] in self.wordDict:
    #             self.cutone(s[i:],candi + ' '+s[:i])
        # 递归超时
    #     self.length = len(s)
    #     self.ans = []
    #     self.dp = [ [] for _ in range(len(s))]
    #     # 动归
    #     for i in range(len(s)):
    #         for j in range(i+1,len(s)+1):
    #             temp = s[i:j]
    #             if s[i:j] in wordDict:
    #                 self.dp[i].append(s[i:j])
    #     for i in range(len(self.dp[0])):
    #         self.cutone(self.dp[0][i],len(self.dp[0][i]),self.dp[0][i])
    #     # for i in range(len(self.ans)):
    #         # self.ans[i] = self.ans[i][1:]
    #     return self.ans
    # def cutone(self,cur,count,candi):
    #     if count == self.length:
    #         self.ans.append(candi)
    #         return
    #     for i in range(len(self.dp[count])):
    #         self.cutone(self.dp[count][i],count + len(self.dp[count][i]),candi+' '+self.dp[count][i])

        # 学成归来，改用动归
        # wordDict.sort()
        # dp = [[] for _ in range(len(s)+1)]
        # dp[0].append([])
        # maxlen = len(wordDict[-1])
        # for i in range(len(s)):
        #     if i >= 1:
        #         dp[i-1] = []
        #     for j in range(i+1,min(i+maxlen,len(s))+1):
        #         temp = s[i:j]
        #         a = 1
        #         # 前一个位置不为空且后面可以被分割
        #         if temp in wordDict and not dp[i] == []:
        #             for item in dp[i]:
        #                 dp[j].append(item+[wordDict.index(temp)])
        # ans = []
        # # 从索引变为字串
        # for item in dp[-1]:
        #     ans.append('')
        #     for i in range(len(item)):
        #         ans[-1] = ans[-1]+ ' ' + wordDict[item[i]] 
        # return [item[1:] for item in ans]

        # 动归超内存！！！！！MD

        # 回溯
    #     self.ans = []
    #     self.wordDict = wordDict
    #     self.cutone(s,'')
    #     return [item[1:] for item in self.ans]
    # # 回溯函数：每次切分一个单词，传入下一级的是剩余字符
    # def cutone(self,s,output):
    #     if len(s) == 0:
    #         self.ans.append(output)
    #     for i in range(1,len(s)+1):
    #         if s[:i] in self.wordDict:
    #             self.cutone(s[i:],output+' '+s[:i])


        # 题解1
    #     size = len(s)
    #     # 题目中说非空字符串，以下 assert 一定通过
    #     assert size > 0

    #     # 预处理，把 wordDict 放进一个哈希表中
    #     word_set = {word for word in wordDict}
    #     # print(word_set)

    #     # 状态：以 s[i] 结尾
    #     # 这种状态定义很常见
    #     dp = [False for _ in range(size)]

    #     dp[0] = s[0] in word_set

    #     # print(dp)

    #     # 使用 r 表示右边界，可以取到
    #     # 使用 l 表示左边界，也可以取到
    #     for r in range(1, size):
    #         # Python 的语法，在切片的时候不包括右边界
    #         # 如果整个单词就直接在 word_set 中，直接返回就好了
    #         # 否则把单词做分割，挨个去判断
    #         if s[:r + 1] in word_set:
    #             dp[r] = True
    #             continue

    #         for l in range(r):
    #             # dp[l] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
    #             if dp[l] and s[l + 1: r + 1] in word_set:
    #                 dp[r] = True
    #                 # 这个 break 很重要，一旦得到 dp[r] = True ，循环不必再继续
    #                 break
    #     res = []
    #     # 如果有解，才有必要回溯
    #     if dp[-1]:
    #         queue = deque()

    #         self.__dfs(s, size - 1, wordDict, res, queue, dp)
    #     return res  

    # def __dfs(self, s, end, word_set, res, path, dp):
    #     # print('刚开始', s[:end + 1])
    #     # 如果不用拆分，整个单词就在 word_set 中就可以结算了
    #     if s[:end + 1] in word_set:
    #         path.appendleft(s[:end + 1])
    #         res.append(' '.join(path))
    #         path.popleft()

    #     for i in range(end):
    #         if dp[i]:
    #             suffix = s[i + 1:end + 1]
    #             if suffix in word_set:
    #                 path.appendleft(suffix)
    #                 self.__dfs(s, i, word_set, res, path, dp)
    #                 path.popleft()

    #     # 题解2
    #     size = len(s)

    #     # 题目中说非空字符串，以下 assert 一定通过
    #     assert size > 0

    #     # 预处理，把 wordDict 放进一个哈希表中
    #     word_set = {word for word in wordDict}

    #     # dp[i] 表示长度为 i 的 s，满足题意
    #     # 0 表示 False ，1 表示 True
    #     dp = [0 for _ in range(size + 1)]
    #     dp[0] = 1

    #     for i in range(1, size + 1):
    #         # i 表示 s 子串的长度
    #         for j in range(i):
    #             # j 表示后子串的起始位置，最多到 i-1
    #             # j 也正正好表示前子串的长度
    #             # dp[j] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
    #             if dp[j] and s[j:i] in word_set:
    #                 dp[i] = 1
    #                 break

    #     res = []
    #     # 如果有解，才有必要回溯
    #     if dp[-1]:
    #         queue = deque()
    #         self.__dfs(s, size, word_set, res, queue, dp)
    #     return res

    # def __dfs(self, s, length, word_set, res, path, dp):
    #     if length == 0:
    #         res.append(' '.join(path))
    #         return
    #     for i in range(length):
    #         if dp[i]:
    #             suffix = s[i:length]
    #             if suffix in word_set:
    #                 path.appendleft(suffix)
    #                 self.__dfs(s, i, word_set, res, path, dp)
    #                 path.popleft()

        # 题解3
        if not s:
            return []
        _len = len(s)  # 转换成字典用于O(1)判断in
        _min, _max = 2147483647, -2147483648   # 记录字典中的单词的最长和最短长度，用于剪枝
        wordDict.sort()
        # _min = len(wordDict[0])
        # _max = len(wordDict[-1])
        for word in wordDict:
            _min = min(_min, len(word))
            _max = max(_max, len(word))

        def dfs(start):  # 返回s[start:]能由字典构成的所有句子
            if start not in memo:
                res = []
                for i in range(_min, min(_max, _len-start)+1):  # 剪枝，只考虑从最小长度到最大长度查找字典
                    if s[start: start+i] in wordDict:  # 找到了
                        res.extend(list(map(lambda x: s[start: start+i]+' '+x, dfs(start+i))))  # 添加
                memo[start] = res  # 加入记忆
            return memo[start]

        memo = {_len: ['']}  # 初始化记忆化存储
        return list(map(lambda x: x[:-1], dfs(0)))  # 去掉末尾多出的一个空格


# @lc code=end

# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
solu = Solution()
print(solu.wordBreak(s,wordDict))