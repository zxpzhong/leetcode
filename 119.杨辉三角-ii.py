#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (58.18%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 65K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 先给定第一行第二行
        numRows = rowIndex+1
        ans = []
        if numRows == 0:
            return ans[-1]
        ans.append([1])
        if numRows == 1:
            return ans[-1]
        ans.append([1,1])
        if numRows == 2:
            return ans[-1]

        pre_line = [0]*(rowIndex+1)
        pre_line[0]=1
        pre_line[1]=1
        temp = [0]*(rowIndex+1)
        for i in range(numRows-2):
            # temp = [0]*(i+3)
            temp[0] = 1
            temp[i+2] = 1
            for j in range(1,i+2):
                temp[j] = pre_line[j-1] + pre_line[j]
            for i in range(len(temp)):
                pre_line[i] = temp[i]
        return pre_line

# @lc code=end


solu = Solution()
print(solu.getRow(3))