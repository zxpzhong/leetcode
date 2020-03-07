#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.02%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 57.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if self.board[i][j] == 'O':
                    # 从这个位置开始向四周扩展，如果可以通过O延展到边界，则不变否则变X
                    ways = self.ifget([[i,j]],i,j)
                    if not ways == False:
                        # 额外检查防止陷入
                        # for way in ways:
                        #     if ([way[0]-1,way[1]] not in ways and self.board[way[0]-1][way[1]] == 'O' )or ([way[0]+1,way[1]] not in ways and self.board[way[0]+1][way[1]] == 'O' ) or ([way[0],way[1]-1] not in ways and self.board[way[0]][way[1]-1] == 'O' ) or ([way[0],way[1]+1] not in ways and self.board[way[0]][way[1]+1] == 'O' ):
                        #         ways = []
                        #         break
                        for way in ways:
                            self.board[way[0]][way[1]] = 'X'
        # return self.board
        pass
    
    def ifget(self,way,i,j):
        if i-1 == 0 and self.board[i-1][j] == 'O':
            return False
        if i+1 == len(self.board)-1 and self.board[i+1][j] == 'O':
            return False
        if j-1 == 0 and self.board[i][j-1] == 'O':
            return False
        if j+1 == len(self.board[0])-1 and self.board[i][j+1] == 'O':
            return False

        if i>=2 and self.board[i-1][j] == 'O' and [i-1,j] not in way:
            # 上
            if not self.ifget(way+[[i-1,j]],i-1,j):
                return False
        # and i <= len(board)-3 and j>=2 and j <= len(board[0])-3 
        if i <= len(self.board)-3 and self.board[i+1][j] == 'O'and [i+1,j] not in way:
            # 下
            if not self.ifget(way+[[i+1,j]],i+1,j):
                return False
        if j>=2 and self.board[i][j-1] == 'O'and [i,j-1] not in way:
            # 左
            if not self.ifget(way+[[i,j-1]],i,j-1):
                return False
        if j <= len(self.board[0])-3 and self.board[i][j+1] == 'O'and [i,j+1] not in way:
            # 下
            if not self.ifget(way+[[i,j+1]],i,j+1):
                return False
        return way

        


# @lc code=end

# board = [
# ["O","X","O","O","O","X"],
# ["O","O","X","X","X","O"],
# ["X","X","X","X","X","O"],
# ["O","O","O","O","X","X"],
# ["X","X","O","O","X","O"],
# ["O","O","X","X","X","X"]]
board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

solu = Solution()
print(solu.solve(board))
