#
# @lc app=leetcode.cn id=357 lang=python
#
# [357] 计算各个位数不同的数字个数
#
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (47.17%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 13.5K
# Testcase Example:  '2'
#
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
# 
# 示例:
# 
# 输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
# 
# 
#

# @lc code=start
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # import math
        # # 只要包含重复数字就要被删除！！
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return 10
        # elif n == 2:
        #     return 91
        # ans = 91+10
        # n = min(n,9)
        # for i in range(3,n+1):
        #     ans+=(math.factorial(9)/math.factorial(9-i))
        #     ans+=(math.factorial(9)/math.factorial(9-i+1))
        # return int(ans)

        # 傻子么？？？每位都不一样，那多出来的一位不就也是不一样的，只能从剩下的选，不就有递推公式了么
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        ans2 = 91
        ans = 81
        for i in range(n-2):
            ans = ans*(10-i-2)
            ans2+=ans
        return ans2


# @lc code=end

