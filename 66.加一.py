#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (41.07%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    113.6K
# Total Submissions: 265.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        later_add = 0
        digits[-1] = digits[-1]+1
        for i in range(length-1,-1,-1):
            digits[i] = digits[i]+later_add
            later_add = digits[i]//10
            digits[i] = digits[i]%10
        if later_add == 1:
            digits.insert(0,1)
        return digits
            
        
# @lc code=end
digits = [1,2,3]
solu = Solution()
print(solu.plusOne(digits))