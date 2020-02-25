#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.22%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    49.5K
# Total Submissions: 112.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每个位置的最大子列，为数值比他小的最大子列数+1
        # dp[n+1] = dp[k]+1
        # k为A[k]<A[n+1]且A【k】 >=A[i],i从1..n
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        dp = [1]*(len(nums))
        for i in range(1,len(nums)):
            # 遍历前面比当前小的最大子列值
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)


# @lc code=end
nums = [1,3,6,7,9,4,10,5,6]
solu = Solution()
print(solu.lengthOfLIS(nums))

