#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.67%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    67.7K
# Total Submissions: 159K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]+nums[1] + nums[2]
        
        nums_bak = nums
        nums_bak.sort()
        # sum_val = nums[0]+nums[1]+nums[2]
        min_sub_val = abs(nums[0]+nums[1]+nums[2]-target)
        # 先排序
        for i in range(len(nums_bak)-2):
            L = i+1
            R = len(nums_bak) - 1
            while R > L:
                sum_val = nums_bak[i] + nums_bak[L] + nums_bak[R] 
                sub_val = abs(sum_val-target)
                if (sum_val-target) == 0:
                    return sum_val
                
                if sub_val <= min_sub_val:
                    min_sub_val = sub_val
                    ans = sum_val


                if sum_val > target:
                    # 大于，右指针左移动
                    R = R-1
                elif sum_val < target:
                    L = L+1
        return ans


# @lc code=end

nums = [-1,0,1,2,-1,-4]
target = 0
solu = Solution()
print(solu.threeSumClosest(nums,target))