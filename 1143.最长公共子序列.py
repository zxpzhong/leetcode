#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (51.63%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 21.1K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。
# 
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde"
# 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
# 
# 若这两个字符串没有公共子序列，则返回 0。
# 
# 
# 
# 示例 1:
# 
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 
# 
# 示例 2:
# 
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
# 
# 
# 示例 3:
# 
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
# 
# 
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        # 初始化
        # 第一行
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1
                for j in range(i+1,len(text1)):
                    dp[j][0] = 1
        # 第一列
        for i in range(len(text2)):
            if text2[i] == text1[0]:
                dp[0][i] = 1
                for j in range(i+1,len(text2)):
                    dp[0][j] = 1
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

text1 = "abcde"
text2 = "ace" 

solu = Solution()
print(solu.longestCommonSubsequence(text1,text2))
