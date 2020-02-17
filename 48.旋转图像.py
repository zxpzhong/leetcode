#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#
# https://leetcode-cn.com/problems/rotate-image/description/
#
# algorithms
# Medium (64.75%)
# Likes:    351
# Dislikes: 0
# Total Accepted:    51.3K
# Total Submissions: 77.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵表示一个图像。
# 
# 将图像顺时针旋转 90 度。
# 
# 说明：
# 
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
# 
# 示例 1:
# 
# 给定 matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# 示例 2:
# 
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def rotate_round(matrix,base):
            length = len(matrix)
            dimen = len(matrix)-base*2
            # 记录顶点值
            fourpoint = [matrix[base][base],matrix[base][-1-base],matrix[-1-base][-1-base],matrix[-1-base][base]]
            # 取出最后一列
            temp = [matrix[base+i][-1-base] for i in range(dimen)][::-1]
            for i in range(dimen-1,-1,-1):
                matrix[i+base][-1-base] = matrix[base][i+base]
            temp2 = matrix[-1-base][base:length-base]
            matrix[-1-base][base:length-base] = temp
            temp3 = [matrix[i+base][base] for i in range(dimen)][::-1]
            for i in range(dimen-1,-1,-1):
                matrix[i+base][base] = temp2[i]
            matrix[base][base:length-base] = temp3
            # 最后修改顶点
            matrix[base][base] = fourpoint[-1]
            matrix[base][-1-base] = fourpoint[0]
            matrix[-1-base][-1-base] = fourpoint[1]
            matrix[-1-base][base] = fourpoint[2]

        dimen = len(matrix)
        rotate_time = dimen//2
        # 一圈一圈转圈,转rotate_time次
        for i in range(rotate_time):
            rotate_round(matrix,i)
        print(matrix)
            
        
# @lc code=end
# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8]]
solu = Solution()
(solu.rotate(matrix))