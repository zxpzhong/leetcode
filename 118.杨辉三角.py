#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (64.17%)
# Likes:    246
# Dislikes: 0
# Total Accepted:    58.9K
# Total Submissions: 89.7K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 先给定第一行第二行

        ans = []
        if numRows == 0:
            return ans
        ans.append([1])
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        for i in range(numRows-2):
            temp = [0]*(i+3)
            temp[0] = 1
            temp[-1] = 1
            for j in range(1,i+2):
                temp[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(temp)
        return ans
        
# @lc code=end

solu = Solution()
print(solu.generate(5))