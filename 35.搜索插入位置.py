#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (44.32%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    110.7K
# Total Submissions: 246.6K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def find_index(nums,target,start):
            length = len(nums)
            if length == 1 and nums[0] < target:
                return start+1
            elif length == 1 and nums[0] > target:
                return start
            if nums[length//2] == target:
                return length//2+start
            # ans = -1
            if nums[length//2] > target:
                start +=0
                ans = find_index(nums[:length//2],target,start)
            else:
                start +=length//2
                ans = find_index(nums[length//2:],target,start)
            return ans
        return find_index(nums,target,0)
# @lc code=end
nums = [1,3,5,6]
target = 0

solu = Solution()
print(solu.searchInsert(nums,target))

