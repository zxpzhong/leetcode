#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (57.20%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 35.5K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.ans = []
        # candi = [i for i in range(1,n+1)]
        for k in range(len(nums)+1):
            self.add_one([],nums,0,k)
        return self.ans

    def add_one(self,curlist,candi,pt,k):
        # 退出条件
        if len(curlist) == k and not curlist in self.ans:
            self.ans.append(curlist)
            return
        for i in range(pt,len(candi)):
            self.add_one(curlist+[candi[i]],candi,i+1,k)
        
# @lc code=end



nums = [1,2,2]
solu = Solution()
print(solu.subsetsWithDup(nums))