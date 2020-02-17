#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (50.77%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    60K
# Total Submissions: 115.3K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = '0'*(len(a)-len(b))+b
        if len(b) > len(a):
            a = '0'*(len(b)-len(a))+a
        pre_add = 0
        # ab扩充完毕，开始加法
        ans = ''
        for i in range(len(a)-1,-1,-1):
            temp = int(a[i]) + int(b[i]) + pre_add
            pre_add = temp//2
            ans=str(temp%2)+ans
        if pre_add == 1:
            ans = '1'+ans
        return ans



        

# @lc code=end
a = '1'
b = '111'
solu = Solution()
print(solu.addBinary(a,b))

