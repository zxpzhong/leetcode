#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (42.12%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 37.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 示例:
# 
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
# 
#

# @lc code=start
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def 
        row = len(matrix)
        column = len(matrix[0])

        # 遍历
        for i in range(row):
            for j in range(column):
                # 以ij为顶点的最大矩形面积是多少

        
# @lc code=end

