#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (75.07%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 31.6K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dimen = n
        rotate_time = n//2
        # 一圈一圈转圈,转rotate_time次
        base_num = 1
        import numpy as np
        matrix = np.zeros([n,n,],dtype=int)
        for i in range(rotate_time):
            matrix,base_num = self.rotate_round(matrix,i,base_num)
        # 如果是奇数，那么还会剩下中间那一个
        if n%2 == 1:
            matrix[n//2,n//2] = base_num
        return matrix
        
    def rotate_round(self,matrix,base,base_num):
        # print(self.ans)
        length1 = len(matrix)
        length2 = len(matrix[0])
        dimen1 = length1-base*2
        dimen2 = length2-base*2
        # 第一行
        matrix[base,base:length2-base-1] = range(base_num,base_num+length2-1-base*2)
        base_num = base_num+length2-1-base*2
        # 最右侧那一列
        for i in range(dimen1-1):
            matrix[base+i,-1-base] = base_num
            base_num+=1
        # 最下面哪一行
        matrix[-base-1,base+1:length2-base] = range(base_num,base_num+length2-base*2-1)[::-1]
        base_num = base_num+length2-1-base*2
        # 最左边那一列
        for i in range(dimen1-1,0,-1):
            matrix[base+i,base] = base_num
            base_num+=1
        return matrix,base_num
        
# @lc code=end
solu = Solution()
print(solu.generateMatrix(4))

