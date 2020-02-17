#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (71.95%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    67.8K
# Total Submissions: 92.9K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def add_one(str,n):
            out = []
            for i in range(len(str)):
                left_number = str[i].count('(')
                right_number = str[i].count(')')
                # 加左边括号条件
                if left_number < n:
                    out.append(str[i]+'(')
                # 加右边括号条件
                if left_number > right_number:
                    out.append(str[i]+')')
            return out
        ans = ['']
        for i in range(2*n):
            ans = add_one(ans,n)
        return ans   

# @lc code=end

solu = Solution()
n = 3
print(solu.generateParenthesis(n))