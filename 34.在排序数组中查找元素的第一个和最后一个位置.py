#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.71%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    56.8K
# Total Submissions: 146.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def find_index(nums,target,start):
            length = len(nums)
            if length == 1 and not nums[0] == target:
                return -1
            if nums[length//2] == target:
                return length//2+start
            ans = -1
            if nums[length//2] > target:
                start +=0
                ans = find_index(nums[:length//2],target,start)
            else:
                start +=length//2
                ans = find_index(nums[length//2:],target,start)
            return ans
        if len(nums) == 0:
            return [-1,-1]
        
        location = find_index(nums,target,0)
        if location == -1:
            return [-1,-1]
        # 前面
        pre = location
        while True:
            pre = pre - 1
            if pre < 0:
                break
            if not nums[pre] == target:
                break
        
        after = location
        while True:
            after = after + 1
            if after > len(nums)-1:
                break
            if not nums[after] == target:
                break
        # 从pre+1到after全是
        return [pre+1,after-1]
        
# @lc code=end

nums = [5,7,7,8,8,10]
target = 8
# nums = [1]
# target = 1
solu = Solution()
print(solu.searchRange(nums,target))
