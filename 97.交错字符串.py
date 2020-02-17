#
# @lc app=leetcode.cn id=97 lang=python
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (36.54%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 24.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 示例 1:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
# 
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
    #     if not len(s1)+len(s2) == len(s3):
    #         return False
    #     return self.one(s1,s2,s3)
        

    # def one(self,s1,s2,s3):
    #     if s3 == '':
    #         if s2 == '' and s1 == '':
    #             return True
    #         else:
    #             return False
    #     # ！！！每次尝试最大相同长度，不仅仅是一个一个

    #     if len(s1) > 0:
    #         if s3[0] == s1[0]:
    #             # 可以取S1可以往下
    #             if self.one(s1[1:],s2,s3[1:]):
    #                 return True
    #     if len(s2) > 0:
    #         if s3[0] == s2[0]:
    #             if self.one(s1,s2[1:],s3[1:]):
    #                 return True
    #     return False
         
        # 动态规划https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
        # s3如果到第i个位置可以了，那么不论前面i个字符由s1的m个，s2的n个组成，m+n=i，不论m个n个怎么取，对后面都没有影响，所以递归/回溯法会出现大量重复
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(0,len1+1):
            for j in range(0,len2+1):
                if not i==j==0:
                #         前一列的位置并且现在位置相等               # 前一行为True且现在位置相等
                    dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]

# @lc code=end

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

solu = Solution()
print(solu.isInterleave(s1,s2,s3))
