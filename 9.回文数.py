#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        # if str_x[0] == '-':
        #     # 如果为负数，返回false
        #     return False
        if str_x[::-1] == str_x:
            return True
        else:
            return False
        
# @lc code=end

