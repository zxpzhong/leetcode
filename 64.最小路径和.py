#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (62.45%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    55K
# Total Submissions: 85.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        # 穷举，列举所有路径然后加和
        down = len(grid)-1
        right = len(grid[0])-1
        self.m = down
        self.n = right
        self.ans = []
        self.get_one_path(down,right,0)
        print(self.ans)
        return min(self.ans)
    def get_one_path(self,down,right,base):
        if (down) == 0:
            self.ans.append(base+sum(self.grid[-1][(self.n-right):]))
        elif right == 0:
            self.ans.append(base+sum([self.grid[i][-1] for i in range(self.m-down,self.m+1)]))
        else:
            if (down) > 0:
                self.get_one_path(down-1,right,base+self.grid[self.m-down][self.n-right])
            if (right) > 0:
                self.get_one_path(down,right-1,base+self.grid[self.m-down][self.n-right])
                
# @lc code=end
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
solu = Solution()
solu.minPathSum(grid)

