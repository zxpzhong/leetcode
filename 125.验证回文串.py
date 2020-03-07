#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.07%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    81.3K
# Total Submissions: 191.3K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution(object):
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
s = "a"
solu = Solution()
print(solu.isPalindrome(s))
