#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.96%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    120.1K
# Total Submissions: 305.1K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0 :
            return 0
        if len(haystack) == 0:
            return -1

        slow_pt = 0
        fast_pt = 0
        while fast_pt < len(haystack):
            if len(needle) == 1:
                if haystack[fast_pt] == needle[fast_pt]:
                    return fast_pt
                fast_pt+=1
                if fast_pt == len(needle):
                    return -1
                
            else:
                if haystack[fast_pt] == needle[fast_pt-slow_pt]:
                    if fast_pt-slow_pt+1 == len(needle):
                        return slow_pt
                    fast_pt+=1
                else:
                    slow_pt+=1
                    fast_pt = slow_pt
        if not fast_pt < len(haystack):
            return -1
        return slow_pt
        
# @lc code=end
haystack = 'mississippi'
needle = "issip"

solu = Solution()
print(solu.strStr(haystack,needle))

