#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (36.99%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    89.1K
# Total Submissions: 237.8K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        elif x < 4:
            return 1
        # 起点设置为x/2看看超时不
        end = x//2
        start = 2
        while not abs(start-end) <= 1:
            ans = start+(end-start)//2
            val = ans**2
            if val > x:
                end = ans
            elif val < x:
                start = ans
            else:
                return ans
        return start
        
# @lc code=end
solu = Solution()
print(solu.mySqrt(9))
