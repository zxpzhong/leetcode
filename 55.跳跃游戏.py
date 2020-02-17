#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (36.29%)
# Likes:    443
# Dislikes: 0
# Total Accepted:    56.2K
# Total Submissions: 148.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 这一题在帮达叔做面试题时做过一摸一样的
        # 总是跳向范围内最大的那个
        # current_loc = 0
        # # for i in range(len(nums)):
        # while current_loc < len(nums):
        #     max_loc = 0
        #     max_step = 0
        #     if current_loc+1+nums[current_loc] >= len(nums):
        #         return True
        #     for j in range(current_loc+1,current_loc+1+nums[current_loc]):
        #         # 找最大,包括自己本身
        #         if nums[j] >= max_step:
        #             max_step = nums[j]
        #             max_loc = j
        #     # 如果最大值还小于自己-1，那么直接跳往最后一步
        #     if nums[current_loc]-1 > max_step and max_loc + max_step < current_loc + nums[current_loc]:
        #         max_loc = current_loc + nums[current_loc]
        #     if max_loc == 0:
        #         return False
        #     current_loc = max_loc
        #     # if current_loc == len(nums)-1
        
        # return True


        # 如果可以到达该位置，那么一定可以到达该位置前所有的位置
        if len(nums) <= 1:
            return True
        max_loc = 0
        for i in range(len(nums)):
            if i > max_loc:
                return False
            elif i + nums[i] > max_loc:
                max_loc = i + nums[i]
                if max_loc >= len(nums)-1:
                    return True
        else:
            return False



        
# @lc code=end

nums = [2,0,0]
# nums = [5,9,3,2,1,0,2,3,3,1,0,0]
solu = Solution()
print(solu.canJump(nums))

