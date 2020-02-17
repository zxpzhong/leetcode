#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (37.21%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    38K
# Total Submissions: 99.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]
        self.ans = []
        dimen = len(matrix)
        min_rowcolumn = min(len(matrix),len(matrix[0]))
        rotate_time = min_rowcolumn//2
        # 一圈一圈转圈,转rotate_time次
        for i in range(rotate_time):
            self.rotate_round(matrix,i)
        # 如果是奇数，那么还会剩下最后中间那一行/列
        if min_rowcolumn%2 == 1:
            if len(matrix) < len(matrix[0]):
                # 最后一行
                self.ans+=matrix[rotate_time][rotate_time:(len(matrix[0])-rotate_time)]
            else:
                self.ans+=[matrix[i][rotate_time] for i in range(rotate_time,len(matrix)-rotate_time)]
        return self.ans

    def rotate_round(self,matrix,base):
        # print(self.ans)
        length1 = len(matrix)
        length2 = len(matrix[0])
        dimen1 = length1-base*2
        dimen2 = length2-base*2
        # 第一行
        self.ans += matrix[base][base:length2-base-1]
        # 最右侧那一列
        self.ans += [matrix[base+i][-1-base] for i in range(dimen1-1)]
        # 最下面哪一行
        self.ans += matrix[-base-1][base+1:length2-base][::-1]
        # 最左边那一列
        self.ans += [matrix[base+i][base] for i in range(1,dimen1)][::-1]
        
        
# @lc code=end
# matrix = [
#  [ 1, 2, 3,0 ],
#  [ 4, 5, 6,1 ],
#  [ 7, 8, 9,2 ],
#  [ 7, 8, 9,2 ]
# ]
# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
solu = Solution()
print(solu.spiralOrder(matrix))
