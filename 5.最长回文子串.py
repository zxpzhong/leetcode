#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.29%)
# Likes:    1652
# Dislikes: 0
# Total Accepted:    169.6K
# Total Submissions: 602.6K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = ''
        length = len(s)
        if length == 1 or length == 0:
            return s
        max_len = 0
        # 遍历字符串
        t = 0
        h = 1
        for i in range(1,length-1):
            j = 1
            # 从指针位置开始遍历到左右两端

            # 第一种情况
            # print(i)

            if s[i-1] == s[i+1]:
                t = 0
                h = 1
                while i-j >0 and i+j <length:
                    if s[i-j] == s[i+j]:
                        j = j + 1
                    else:
                       break
                j = j-1
            # 第二种情况
            elif s[i] == s[i+1]:
                t = 1
                h = 1
                # print(i)
                while i-j >=0 and i+j <length:
                    if s[i-j+1] == s[i+j]:
                         j = j + 1
                    else:
                        break
                j = j-1
            print('i = ',i)
            if j > max_len:
                # print('j = ',j)
                # print(i-j,i+j)
                max_len = j
                final = s[i-j+t:i+j+h]
                # print(i,j,t,h)
                # print(i-j+t,i+j+h)
        if len(final) == 0:
            return s[0]
        return final

# @lc code=end

# input_string = 'babad'
# input_string = 'gacbbcfd'
input_string = 'cbbd'
# input_string = 'bb'
solu = Solution()
print(solu.longestPalindrome(input_string))

