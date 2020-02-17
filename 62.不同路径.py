#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (56.59%)
# Likes:    409
# Dislikes: 0
# Total Accepted:    67.1K
# Total Submissions: 114.4K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 动态规划直接上解法
        # dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # #print(dp)
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]

        # 优化1空间复杂度 O(2n)，逻辑和上面是一样的，只不过减少了所需要的储存空间，原来空间复杂度为n^2
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

        # 优化2：空间复杂度 O(n)O(n)
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]



        # 其实最开始的时候想法是对的：m-1个右和n-1个下，请问一共有多少种不同的排列
        # 但是你的高中知识忘的一干二净，所以你TMD写不出来
        # import math
        # 一共需要走m+n-2步，这其中选m-1步出来，颁奖
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))



        # 分解的方法，每一个m*n的矩阵可以分解为(m-1)*n + m*(n-1)的矩阵
        # 一直分解直到分解为t*2的矩阵，每个t*2的矩阵有t种走法
        # for i in 
        # 这个思路和下面的全排列是一样的




        # 全排列的方法不行，超时
        # m-1个右和n-1个下，请问一共有多少种不同的排列
    #     if m == 1 or n == 1:
    #         return 1
    #     down = m
    #     right = n
    #     self.ans = 0
    #     self.get_one_path(down,right)
    #     return self.ans 
    # def get_one_path(self,down,right):
    #     if (down) == 2:
    #         self.ans += right
    #     elif right == 2:
    #         self.ans += down
    #     else:
    #         if (down) > 2:
    #             self.get_one_path(down-1,right)
    #         if (right) > 2:
    #             self.get_one_path(down,right-1)



# @lc code=end
solu = Solution()
print(solu.uniquePaths(3,3))
