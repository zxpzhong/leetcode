#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (38.12%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 56.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 动态规划
        # 状态：dp[i][j] ：i,j位置的最大矩形
        # 状态转移方程：
        # if a[i][j] == 1  dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1(这个1就是1自己本身)
        # else dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        # 边界条件：dp[0][0] = ? dp[0][:] = matrix dp[:][0] = matrix
        
        if len(matrix) == 0:
            return 0
        max_ele = 0
        dp = []
        for i in range(len(matrix)):
            dp.append([0]*len(matrix[0]))
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            max_ele = max(max_ele,dp[0][i])
        
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            max_ele = max(max_ele,dp[i][0])

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                else:
                    dp[i][j] = 0
                max_ele = max(dp[i][j],max_ele)
        return max_ele**2
        



# @lc code=end
matrix = [
    ["1","0","1","1","0","1"],
    ["1","1","1","1","1","1"],
    ["0","1","1","0","1","1"],
    ["1","1","1","0","1","0"],
    ["0","1","1","1","1","1"],
    ["1","1","0","1","1","1"]]

# matrix = [['1']]
solu = Solution()
print(solu.maximalSquare(matrix))