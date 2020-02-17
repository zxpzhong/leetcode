#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (57.03%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    36.5K
# Total Submissions: 61.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 排序
        candidates.sort()
        # 快慢指针
        fast_pt = 0
        slow_pt = 0
        length = len(candidates)
        ans = []
        while fast_pt < length and slow_pt < length:
            current_sum = sum(candidates[slow_pt:fast_pt])
            if current_sum == target:
                # 满足条件
                ans.append(candidates[slow_pt:fast_pt])
            elif current_sum > target:
                slow_pt+=1
                fast_pt=slow_pt
            else:
                fast_pt+=1
        return ans 
        
# @lc code=end
candidates = [10,1,2,7,6,1,5]
target = 8
solu = Solution()
solu.combinationSum2(candidates,target)
