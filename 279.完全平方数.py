#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (50.70%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    37.2K
# Total Submissions: 69.1K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#

# @lc code=start

import math
class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS
    #     return self.get_one([n],0)

    # def get_one(self,n_list,time):
        
    #     for item in n_list:
    #         if (math.sqrt(item)) == int(math.sqrt(item)):
    #             return time+1
    #     new_list = []
    #     for item in n_list:
    #         i = 1
    #         while i**2 < item:
    #             new_list.append(item-i**2)
    #             i+=1
    #     return self.get_one(new_list,time+1)


        # 动归解法
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                # i = j*j这一个完全平方数+(i-j*j)的最小组成
                # 遍历j取最小个数
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]

# @lc code=end

solu = Solution()
print(solu.numSquares(11))