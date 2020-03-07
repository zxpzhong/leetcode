#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (63.59%)
# Likes:    1089
# Dislikes: 0
# Total Accepted:    156.5K
# Total Submissions: 238.4K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            # 异或实现了加法或者减法！！取决于遇见该数的次数
            ans = ans^nums[i]
        return ans
# @lc code=end
nums = [4,1,2,1,2]
solu = Solution()
print(solu.singleNumber(nums))
