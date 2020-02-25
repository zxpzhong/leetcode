#
# @lc app=leetcode.cn id=343 lang=python
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (52.50%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 31.6K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 第一种，拆解法
        # 两数拆分乘积大于和的数是从4开始
        
        # 先排除不需要划分的
    #     if n==2:
    #         return 1
    #     elif n == 3:
    #         return 2
    #     self.ans = []
    #     self.seg_one(n)
    #     temp = 1
    #     for i in range(len(self.ans)):
    #         temp*=self.ans[i]
    #     return temp
        
    #     # 分解为奇数和偶数，两偶数或者是一奇一偶
    #     # 可以无限次拆分
    # def seg_one(self,number):
    #     if number <=4:
    #         self.ans.append(number)
    #     else:
    #         self.seg_one(number//2)
    #         self.seg_one(number//2+number%2)

        
        #----------------分解为两个数可以平分，三个数不行！！！

        # 动归
        dp = [i for i in range(1,n+1)]
        if n <= 2:
            return 1
        elif n <= 3:
            return 2
        for i in range(4,n):
            temp = 0
            for j in range(1,(i-1)//2+1):
                temp = max(temp,dp[j]*dp[i-1-j])
            dp[i] = temp
        return dp[-1]

            


# @lc code=end

n = 3
solu = Solution()
print(solu.integerBreak(n))