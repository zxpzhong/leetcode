#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (74.83%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    57.5K
# Total Submissions: 75.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        # candi = [i for i in range(1,n+1)]
        self.candi = nums
        for k in range(1,len(nums)+1):
            self.add_one([],0,k,1)
        return self.ans

    def add_one(self,curlist,pt,k,len_cur):
        # 退出条件
        if len(curlist) == k:
            self.ans.append(curlist)
            return
        for i in range(pt,len(self.candi)):
            self.add_one(curlist+[self.candi[i]],i+1,k,len_cur+1)
          
# @lc code=end
nums = [1,2,3,4]
solu = Solution()
print(solu.subsets(nums))