#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.65%)
# Likes:    1104
# Dislikes: 0
# Total Accepted:    132.1K
# Total Submissions: 333.1K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','{','[']
        right = [')','}',']']
        for i in range(len(s)):
            if s[i] in left:
                stack.append(left.index(s[i]))
            elif s[i] in right:
                try:
                    pop_item = stack.pop()
                except:
                    return False
                if right.index(s[i]) == pop_item:
                    pass
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
# @lc code=end
solu = Solution()
s = ']'
print(solu.isValid(s))

