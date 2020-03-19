#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.89%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 62.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        stack = {}
        for i in range(len(t)):
            stack[t[i]] = 0
        l = 0
        r = 0
        ans = ''
        while r < len(s):
            if min(stack.values()) == 0: 
                if s[r] in t:
                    stack[s[r]]+=1
                r+=1
            # 如果已经全部集齐，则l开始移动
            else:
                if r-l+1 < len(ans):
                    ans = s[l:r+1]
                l+=1
                if s[l] in t:
                    stack[s[r]]-=1
                
        
# @lc code=end

