#
# @lc app=leetcode.cn id=377 lang=python
#
# [377] 组合总和 Ⅳ
#
# https://leetcode-cn.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (39.60%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    7.5K
# Total Submissions: 18.2K
# Testcase Example:  '[1,2,3]\n4'
#
# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
# 
# 示例:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# 请注意，顺序不同的序列被视作不同的组合。
# 
# 因此输出为 7。
# 
# 
# 进阶：
# 如果给定的数组中含有负数会怎么样？
# 问题会产生什么变化？
# 我们需要在题目中添加什么限制来允许负数的出现？
# 
# 致谢：
# 特别感谢 @pbrother 添加此问题并创建所有测试用例。
# 
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    #
    #     if len(nums) == 0:
    #         return 0
    #     self.nums = nums
    #     self.minnum = min(nums)
    #     self.ans = 0
    #     self.subone(target)
    #     return self.ans

    # def subone(self,target):
    #     if target in self.nums:
    #         self.ans += 1
    #     for item in self.nums:
    #         if target-item >= self.minnum:
    #             self.subone(target-item)
        #---------------以上是递归，不行

        # DP
        
# @lc code=end

nums = [1, 2, 3]
target = 4
solu = Solution()
print(solu.combinationSum4(nums,target))