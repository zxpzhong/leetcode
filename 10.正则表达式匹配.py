#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.93%)
# Likes:    886
# Dislikes: 0
# Total Accepted:    47.7K
# Total Submissions: 185.3K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# 
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 回溯

    # 先写回溯函数：每次匹配掉一个字符
    def matchone(self,s,p):
        # 如果直接相等，那肯定没得洗，直接过
        if s[0] == p[0]:
            self.matchone(s[1:],p[1:])
        elif p[0] == '.':
            # 如果已经到了最后一个字符：
            if len(s) == 1 and len(p) == 1:
                # 匹配完毕
                return True
            elif p[1] = '*':
                # 那么匹配到的下一个
                for t in range(1,len(s)):
                    self.matchone(s[t:],p)
        elif p[0] == '*':
            # 前面的字符可以使用任意多次


        
        
# @lc code=end

s = "mississippi"
p = "mis*is*p*."
solu = Solution()
print(solu.isMatch(s,p))