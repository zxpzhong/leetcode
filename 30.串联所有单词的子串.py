#
# @lc app=leetcode.cn id=30 lang=python
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (27.30%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 73.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
# 
# 示例 2：
# 
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
# 
# 
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # from collections import Counter
        # if s == '' or len(words) == 0:
        #     return []
        # single_length = len(words[0])
        # all_length = len(words)*single_length

        # all_words = Counter(words[0])
        # for i in range(1,len(words)):
        #     all_words+=Counter(words[i])
        
        # def subfind(s,words):
        #     if len(s) == 0:
        #         return True
        #     # s的长度等于words中所有的长度
        #     for i in range(len(words)):
        #         if s[:single_length] == words[i]:
        #             if subfind(s[single_length:],words[:i]+words[i+1:]):
        #                 return True
        #     return False
        # result = []
        # for i in range(len(s)-all_length+1):
        #     if True:
        #         if subfind(s[i:i+all_length],words) == True:
        #             result.append(i)
        # return result

        # 巧妙啊
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            # 人家这里是充分利用了长度相等，直接把词且分开，然后统计短语数量
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res

                    
        
# @lc code=end
s = "barfoothefoobarman"
words = ["foo","bar"]

# s = 'a'
# words = []

solu = Solution()
print(solu.findSubstring(s,words))

