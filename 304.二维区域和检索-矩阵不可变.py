#
# @lc app=leetcode.cn id=304 lang=python
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (40.71%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 13.7K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
# 
# 
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 
# 示例:
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 说明:
# 
# 
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2。
# 
# 
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        print('111')
        if not matrix:
            self.ans = -2147483648
            return
        print('222')
        self.ans = []
        for _ in range(len(matrix)):
            self.ans.append([0]*len(matrix[0]))
        sum = 0
        for i in range(len(matrix)):
            # 为第一列赋初值
            sum = sum + matrix[i][0]
            self.ans[i][0] = sum
            
        sum = 0
        for i in range(len(matrix[0])):
            # 为第一行赋初值
            sum = sum + matrix[0][i]
            self.ans[0][i] = sum
        
        for i in range(1,len(self.ans)):
            for j in range(1,len(self.ans[0])):
                # 每一个位置都是以从开头到以i,j为顶点长方形的和
                self.ans[i][j] = self.ans[i][j-1]+self.ans[i-1][j]-self.ans[i-1][j-1]+matrix[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.ans == -2147483648:
            return -2147483648
        if row1 == col1 == row2 == col2:
            return self.matrix[row1][col1]
        elif col1 == row1 == 0:
            return self.ans[row2][col2]
        elif row1 == 0:
            return self.ans[row2][col2]-self.ans[row2][col1-1]
        elif col1 ==0:
            return self.ans[row2][col2]-self.ans[row1-1][col2]
        else:
            return self.ans[row2][col2]-self.ans[row1-1][col2]-self.ans[row2][col1-1]+self.ans[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

matrix = [[1,-3],[-4,9]]
solu = NumMatrix(matrix)
print(solu.sumRegion(0,0,1,1))