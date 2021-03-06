#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (41.77%)
# Likes:    640
# Dislikes: 0
# Total Accepted:    75.3K
# Total Submissions: 175.2K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        # 转移方程：
        # dp(k) = max(dp(k-1),dp(k-2)+a(k))
        # 边界条件：
        # dp(0) = a(0)
        # dp(1) = max(a(0),a(1))
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        prepre = nums[0]
        pre = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            cur = max(pre,prepre+nums[i])
            prepre = pre
            pre = cur
        return cur
            


        
# @lc code=end
s = [1,2,3,1]
solu = Solution()
print(solu.rob(s))

