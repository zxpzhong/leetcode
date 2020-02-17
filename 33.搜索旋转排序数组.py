#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.08%)
# Likes:    486
# Dislikes: 0
# Total Accepted:    68.2K
# Total Submissions: 187.9K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_half(nums,target,start):

            length = len(nums)
            if length == 1 and not nums[0] == target:
                return -1
            # 递归

            direction = 0
            # 判断截断位置与目标关系
            if nums[0] > target:
                # 小数那边
                direction = -1
            elif nums[0] < target:
                # 大数那边
                direction = 1
            else:
                return start

            if nums[-1] == target:
                return len(nums)-1+start
            if nums[length//2] == target:
                return start+length//2
            ans = -1

            left = 0
            right = 0
            if direction == -1:
                if nums[length//2] < target:
                    right = 1
                elif nums[length//2] > nums[0]:
                    right = 1
                else:
                    left = 1
            else:
                if nums[length//2] > target:
                    left = 1
                elif nums[length//2] < nums[0]:
                    left = 1
                else:
                    right = 1
            if right == 1:
                start = start + length//2
                ans = find_half(nums[length//2:],target,start)
            else:
                # 返回左边
                start = start + 0
                ans = find_half(nums[:length//2],target,start)
            
            return ans

        if len(nums) == 0:
            return -1
        ans = find_half(nums,target,0)
        return ans
            

        
# @lc code=end

nums = [4,5,6,7,0,1,2]
target = 3
# nums = [8,1,2,3,4,5,6,7]
# target = 6
solu = Solution()
print(solu.search(nums,target))
