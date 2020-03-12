#
# @lc app=leetcode.cn id=216 lang=python
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (68.62%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 21.7K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 找出第一组
        # (1~k)累加和
        a = sum([i for i in range(1,k+1)])
        if a > n:
            return []
        elif a == n:
            return [[i for i in range(1,k+1)]]
        # 先找出最小那一组：[1,2,...k-1,n-sum(1~k-1)]

        

# @lc code=end
k = 3, n = 7
solu = Solution()
print(solu.combinationSum3(k,n))
