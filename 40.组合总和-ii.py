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
        min_val = min(candidates)
        max_val = min(candidates)
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
        candidates = candidates[:i+1]

        # 回溯
        self.candidates = candidates
        self.ans = []
        self.cut_one(target,[],candidates)
        self.ans.sort()
        if len(self.ans) == 0:
            return []
        self.new_ans = []
        self.new_ans.append(self.ans[0])
        pre_val = self.ans[0]
        for i in range(1,len(self.ans)):
            if not self.ans[i] == pre_val:
                self.new_ans.append(self.ans[i])
            pre_val = self.ans[i]
        return self.new_ans

    def cut_one(self,res,candi,candidates):
        for i,item in enumerate(candidates):
            if item == res:
                self.ans.append(candi+[item])
            elif item < res:
                self.cut_one(res-item,candi+[item],candidates[i+1:])
            else:
                return
        
# @lc code=end
candidates = [2]
target = 1
solu = Solution()
print(solu.combinationSum2(candidates,target))
