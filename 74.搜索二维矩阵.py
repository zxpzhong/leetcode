#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.85%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    29.5K
# Total Submissions: 79.4K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 示例 1:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        if len(matrix) == 1 and matrix[0][0] == target:
            return True

        # 二分法的矩阵版本嘛。。
        # 如果直接从行中间开始搞，那么会遇到多行合并的时候，有一行的数据只有一半有用
        # 先确定行，再确定列
        rows = len(matrix)
        start = 0
        end = rows-1

        while end - start > 1:
            middle = start+(end-start)//2
            if target > matrix[middle][0]:
                # 比中间大，end上移
                start = middle
            elif target < matrix[middle][0]:
                end = middle
            else:
                return True

        if matrix[start][0] == target or matrix[end][0] == target:
            return True
        if target > matrix[end][0]:
            line = end
        else:
            line = start
        # 确定在第start行，二分确定列
        start = 0
        end = len(matrix[0])-1
        while  end-start > 1:
            middle = start+(end-start)//2
            if target > matrix[line][middle]:
                # 比中间大，end上移
                start = middle
            elif target < matrix[line][middle]:
                end = middle
            else:
                return True
        if matrix[line][start] == target or matrix[line][end] == target:
            return True
        return False

        
# @lc code=end

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3

solu = Solution()
print(solu.searchMatrix(matrix,target))
