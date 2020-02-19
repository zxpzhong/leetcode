#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (35.52%)
# Likes:    378
# Dislikes: 0
# Total Accepted:    35K
# Total Submissions: 94K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 边界条件
        maxDP = nums[0]
        minDP = nums[0]
        dp = nums[0]
        for i in range(1,len(nums)):
            # 状态转移方程 + 转移状态
            temp = maxDP
            maxDP = max(maxDP*nums[i],nums[i],minDP*nums[i])
            minDP = min(minDP*nums[i],nums[i],temp*nums[i])
            dp = max(dp,maxDP)
        return dp
# @lc code=end

s = [-4,-3,-2]
solu = Solution()
print(solu.maxProduct(s))
