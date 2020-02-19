#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (42.67%)
# Likes:    309
# Dislikes: 0
# Total Accepted:    34.6K
# Total Submissions: 79.8K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 动态规划
        # 只要你当前到了该位置，具体前面怎么划分，不管
        dp = [False]*(len(s)+1)
        # 边界条件
        dp[0] = True
        for i in range(1,len(dp)):
            for j in range(i,len(dp)):
                if dp[i-1] == True and s[i-1:j] in wordDict:
                    dp[j] = True
        return dp[-1]

        
# @lc code=end
# s = "leetcode"
# wordDict = ["leet", "code"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

solu = Solution()
print(solu.wordBreak(s,wordDict))
