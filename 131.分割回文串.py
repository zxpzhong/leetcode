#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (63.88%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 35K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        self.segone([],s)
        return self.ans

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
            
    def segone(self,candi,left):
        if len(left) == 0:
            self.ans.append(candi)
        for i in range(len(left)):
            if self.isPalindrome(left[:i+1]):
                self.segone(candi+[left[:i+1]],left[i+1:])
        



# @lc code=end
s = 'aab'
solu = Solution()
print(solu.partition(s))
