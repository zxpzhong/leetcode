#
# @lc app=leetcode.cn id=132 lang=python
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (40.77%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 17.5K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回符合要求的最少分割次数。
# 
# 示例:
# 
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
#

# @lc code=start
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动归
        # dp = [i for i in range(len(s))]
        # dp[0] = 0
        # for i in range(len(s)):
        #     if dp[i] < i:
        #         continue
        #     for j in range(i,len(s)):
        #         temp = s[i:j+1]
        #         if dp[j] < j:
        #             continue
        #         if self.isPalindrome(s[i:j+1]):
        #             # 如果是回文串，则
        #             dp[j] = min(dp[i],dp[i-1]+1)
        # return dp[-1]

        dp = [2147483647 for i in range(len(s))]
        dp[0] = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = s[i:j+1]
                if self.isPalindrome(s[i:j+1]):
                    # 如果是回文串，则
                    if not dp[i] < i:
                        dp[j] = min(dp[i],dp[i-1]+1)
        return dp[-1]


    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isengchar(char):
            if 'z'>=char>='a' or '9'>=char>='0':
                return char
            else:
                return False

        s = s.lower()
        #首尾指针法
        # s[pt1] == s[pt2]
        if len(s) ==2:
            if not isengchar(s[0]) or not isengchar(s[1]):
                return True
            if s[0] == s[1]:
                return True
            else:
                return False
        pt1 = 0
        pt2 = len(s)-1
        while pt2-pt1>=1:
            if not isengchar(s[pt1]):
                pt1+=1
                continue
            if not isengchar(s[pt2]):
                pt2-=1
                continue
            if s[pt1] == s[pt2]:
                pt1+=1
                pt2-=1
                continue
            else:
                return False
        return True
        
# @lc code=end

s = "cabababcbc"
solu = Solution()
print(solu.minCut(s))