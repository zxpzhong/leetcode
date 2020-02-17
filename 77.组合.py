#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (70.51%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 44.6K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # import math
        # return int(math.factorial(n)/math.factorial(k)/math.factorial(n-k))
        self.ans = []
        candi = [i for i in range(1,n+1)]
        self.k = k
        self.add_one([],candi,0)

        return self.ans
    def add_one(self,curlist,candi,pt):
        # 退出条件
        if len(curlist) == self.k:
            self.ans.append(curlist)
            return
        for i in range(pt,len(candi)):
            self.add_one(curlist+[candi[i]],candi,i+1)
        
# @lc code=end
n = 4
k = 2
solu = Solution()
a = solu.combine(n,k)
print(a)
