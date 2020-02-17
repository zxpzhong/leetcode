#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (28.36%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    35.6K
# Total Submissions: 121.5K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        def isValid(s):
            """
            :type s: str
            :rtype: bool
            """
            stack = []
            left = '('
            right = ')'
            count = Counter(s)
            if not count['('] == count[')']:
                return False
            for i in range(len(s)):
                if s[i] == left:
                    stack.append(left)
                elif s[i] == right:
                    try:
                        pop_item = stack.pop()
                    except:
                        return False
                    if left == pop_item:
                        pass
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False

        # 快慢指针
        fast_pt = 0
        slow_pt = 0
        max_length = 0
        # for slow_pt in range(len(s)):
        while slow_pt < len(s):
            fast_pt = slow_pt+max_length
            if s[slow_pt] == '(':
                while not fast_pt == -1:
                    fast_pt = s.find(')',fast_pt+1)
                    a = s[slow_pt:fast_pt+1]
                    # if (fast_pt-slow_pt)%2 == 1:
                    if True:
                        if isValid(s[slow_pt:fast_pt+1]):
                            if fast_pt+1-slow_pt > max_length:
                                # 符合条件且为最长
                                max_length = fast_pt+1-slow_pt
                            continue
                        else:
                            break
            slow_pt = max(slow_pt+1,fast_pt)
        return max_length

        # # 网上解法1：栈优化不排序
        # if(not s):
        #     return 0
        # for i in range(len(s)):
        #     if s[i] == '(':

        
# @lc code=end
s = '(()'
# s = '(()))()()()()('
solu = Solution()
print(solu.longestValidParentheses(s))
