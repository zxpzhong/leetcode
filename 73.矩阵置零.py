#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (54.17%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 50.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 
# 示例 1:
# 
# 输入: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# 输出: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# 示例 2:
# 
# 输入: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# 输出: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 进阶:
# 
# 
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
# 
# 
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        comlumn = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    comlumn.append(j)
        # 去重
        row = list(set(row))
        comlumn = list(set(comlumn))
        for i in range(len(row)):
            # 整行置0
            matrix[row[i]] = [0]*len(matrix[0])
        for j in range(len(comlumn)):
            # 整列置0
            for t in range(len(matrix)):
                matrix[t][comlumn[j]] = 0
        
        
# @lc code=end
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

solu = Solution()
solu.setZeroes(matrix)
print(matrix)
