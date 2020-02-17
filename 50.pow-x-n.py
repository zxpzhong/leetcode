#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (33.16%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    47.5K
# Total Submissions: 141.1K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # import math
        # return math.pow(x,n)
        # new_n = n//2

        # def pow_half(x,n):
        #     if n == 1:
        #         return x
        #     elif n == -1:
        #         return 1.0/x
        #     elif n == 0:
        #         return 1
        #     temp = pow_half(x,n//2)
        #     return temp*temp*(x if n%2 == 1 else 1)
        # return pow_half(x,n)
        return x**n
        
# @lc code=end
solu = Solution()
print(solu.myPow(2,-2))

