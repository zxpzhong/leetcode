#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (47.72%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 44.6K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)
        add_len = min(length1,length2)
        extra = 0
        val = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(add_len):
            sum_val = int(num1[i]) + int(num2[i]) + extra
            current_bit = sum_val%10
            val+=str(current_bit)
            extra = sum_val//10
        if length1 > length2:
            for j in range(add_len,length1):
                sum_val = int(num1[j]) + extra
                current_bit = sum_val%10
                val+=str(current_bit)
                extra = sum_val//10
        else:
            for j in range(add_len,length2):
                sum_val = int(num2[j]) + extra
                current_bit = sum_val%10
                val+=str(current_bit)
                extra = sum_val//10
        if extra == 1:
            val+=('1')
        val = val[::-1]
        return val

            



        
# @lc code=end
num1 = '9'
num2 = '1'
solu = Solution()
print(solu.addStrings(num1,num2))

