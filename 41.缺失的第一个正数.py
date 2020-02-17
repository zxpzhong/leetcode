#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (36.53%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 91.5K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 说明:
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
# 
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)  == 0:
            return 1
        if len(nums) == 1:
            return 1 if not nums[0] == 1 else 2
        
        # 排序
        nums.sort()
        # 二分查找最小正整数
        def find_index(nums,target,start):
            length = len(nums)
            if length == 1 and not nums[0] == target:
                if nums[0] < target:
                    return length//2+start+1
                else:
                    return length//2+start
            if nums[length//2] == target:
                return length//2+start+1
            ans = -1
            if nums[length//2] > target:
                start +=0
                ans = find_index(nums[:length//2],target,start)
            else:
                start +=length//2
                ans = find_index(nums[length//2:],target,start)
            return ans
        
        zero_index = find_index(nums,0,0)
        # 正数子列
        positive_list = nums[zero_index:]
        i = 0
        while i < len(positive_list):
            if not positive_list[i] == 0:
                break
            i+=1
        positive_list = positive_list[i:]

        if len(positive_list)  == 0:
            return 1
        if len(positive_list) == 1:
            return 1 if not positive_list[0] == 1 else 2
        min_inter = 1
        for i in range(len(positive_list)-1):
            if not positive_list[i] == min_inter:
                return min_inter
            else:
                if not positive_list[i] == positive_list[i+1]: 
                    min_inter = min_inter+1
        if not positive_list[-1] == min_inter:
            return min_inter
        else:
            return min_inter+1

    
# @lc code=end
# nums = [1,2,0]
nums = [10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6]
solu = Solution()
print(solu.firstMissingPositive(nums))

