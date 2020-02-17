#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (31.79%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 118.9K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        # 将左行和上列的1拓展到尾巴
        for i in range(len(obstacleGrid[0])-1):
            # 上行
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i+1] = 1
        for i in range(len(obstacleGrid)-1):
            # 左列
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i+1][0] = 1


        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            if 1 in obstacleGrid[0] or 1 in [obstacleGrid[i][0] for i in range(len(obstacleGrid))]:
                return 0
            else:
                return 1 
            
        import numpy as np
        # 转化为np矩阵
        obstacleGrid = np.array(obstacleGrid,dtype=int)
        index = obstacleGrid == 1
        # 初始化左行和上列
        obstacleGrid[0,:] = 1
        obstacleGrid[:,0] = 1
        obstacleGrid[index] = -1
        for i in range(1,obstacleGrid.shape[0]):
            for j in range(1,obstacleGrid.shape[1]):
                if obstacleGrid[i,j] == -1:
                    # 如果是障碍不能走，那么继续保持-1
                    continue
                # 通过max函数跳过-1
                obstacleGrid[i,j] = max(obstacleGrid[i-1,j],0)  +  max(obstacleGrid[i,j-1],0)
        return max(obstacleGrid[-1,-1],0)
                        
# @lc code=end
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
obstacleGrid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
solu = Solution()
print(solu.uniquePathsWithObstacles(obstacleGrid))