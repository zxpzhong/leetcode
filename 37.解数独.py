#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (56.70%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 29.5K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#
"""
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
"""
	# 	def get_matrix(s,i,j):
	# 		# 取出行
	# 		t = s[i:i+3]
	# 		# 取出列 
	# 		return t[0][j:j+3]+t[1][j:j+3]+t[2][j:j+3]
	# 	candi = [str(i) for i in range(1,10)]
	# 	self.candi = [str(i) for i in range(1,10)]
		
	# 	for i in range(len(board)):
	# 		temp = deepcopy(candi)
	# 		for j in range(len(board[0])):
	# 			if board[i][j] in candi:
	# 				temp.remove(board[i][j])
	# 		# 每一行的temp
	# 		for j in range(len(board[0])):
	# 			if board[i][j] not in candi:
	# 				board[i][j] = temp
		
	# 	for j in range(len(board[0])):
	# 		temp = deepcopy(candi)
	# 		for i in range(len(board)):
	# 			if board[i][j] in candi:
	# 				temp.remove(board[i][j])
	# 		# 每一列的temp
	# 		for i in range(len(board)):
	# 			if board[i][j] not in candi:
	# 				# 交集
	# 				board[i][j] =  [item for item in board[i][j] if item in temp]
	# 	# 检查矩阵
	# 	for j in range(len(board[0])):
	# 		for i in range(len(board)):
	# 			temp = deepcopy(candi)
	# 			if i % 3 == 0 and j %3 == 0:
	# 				matrix = get_matrix(board,i,j)
	# 				# 检查matrix中的元素重复
	# 				for item in matrix:
	# 					if item in candi:
	# 						temp.remove(item)
	# 				for m in range(i,i+3):
	# 					for n in range(j,j+3):
	# 						if board[m][n] not in candi:
	# 							board[m][n] =  [item for item in board[m][n] if item in temp]
	# 	# 行列和矩阵都满足，接下来选择
	# 	self.board = deepcopy(board)
	# 	# 深度优先搜索
	# 	return self.cut_one(board)

	# def isOK(self,board):
	# 	for i in range(len(board)):
	# 		for j in range(len(board[0])):
	# 			if board[i][j] not in self.candi:
	# 				return False
	# 	return True

	# def cut_one(self,boardin):
	# 	# 成功
	# 	if self.isOK(boardin):
	# 		# self.ans = board
	# 		return boardin
	# 	for i in range(len(boardin)):
	# 		for j in range(len(boardin[0])):
	# 			board = deepcopy(boardin)
	# 			# 遍历到第一个没有用过的
	# 			if board[i][j] not in self.candi:
	# 				if len(board[i][j]) == 0:
	# 					return False
	# 				board[i][j] = board[i][j][0]
	# 				# 删除本列同一候选词
	# 				for m in range(len(board)):
	# 					if board[m][j] not in self.candi:
	# 						try: board[m][j].remove(board[i][j])
	# 						except: pass
	# 				# 删除本行同一候选词
	# 				for n in range(len(board[0])):
	# 					if board[i][n] not in self.candi:
	# 						try: board[i][n].remove(board[i][j])
	# 						except: pass
	# 				# 删除本矩阵同一候选词
	# 				for m in range(i//3*3,i//3+i%3):
	# 					for n in range(j//3*3,j//3+j%3):
	# 						if not m==i and not n == j:
	# 							if board[m][n] not in self.candi:
	# 								try: board[m][n].remove(board[i][j])
	# 								except: pass
	# 				# 递归选取下一个
	# 				if self.cut_one(board):
	# 					return True
"""
        # 兄弟你太辣鸡了，用最难得方法解最简单的题目，这就是你的风格啊！！！
# @lc code=start

from copy import deepcopy
class Solution(object):
    def solveSudoku(self, board):
        self.backtrace(board,0,0)
        
    # 回溯函数
    def backtrace(self,board,row,col):
        col_back = col
        tempi = 0
        tempj = 0
        for i in range(row,len(board)):
            for j in range(col,len(board[0])):
                tempi = i
                tempj = j
                col=0
                if board[i][j] == '.':
                    # 当前位置可选
                    candi = [str(t) for t in range(1,10)]
                    # 遍历行列和矩阵删除所有可能的候选词
                    for m in range(len(board[i])):
                        try: candi.remove(board[i][m])
                        except: pass
                    for n in range(len(board)):
                        try: candi.remove(board[n][j])
                        except: pass
                    for m in range((i//3)*3,(i//3)*3+3):
                        for n in range((j//3)*3,(j//3)*3+3):
                            try: candi.remove(board[m][n])
                            except: pass
                    # 开始放置下一个位置
                    if j < 8:
                        newi = i
                        newj=j+1
                    else:
                        newi=i+1
                        newj = 0
                    if i == 8:
                        a = 8
                    # 遍历候选词
                    for item in candi:
                        # 将i,j位置可选项放入
                        board[i][j] = item
                        # 这里用return！！！！快速返回
                        if i == 8 and j == 8:
                            return True
                        if self.backtrace(board,newi,newj):
                            return True
                        # 如果运行到这了，说明不行，回溯，将赋值的位置删除!!
                        board[i][j] = '.'
                    return False
        if tempi == 8 and tempj == 8:
            return True

# @lc code=end

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# board = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6",".","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1",".",".",".","2","8","4"],["2","8","7","4","1",".","6","3","5"],["3","4","5","2","8","6","1",".","."]]
# board = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6",".","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1",".",".",".","2","8","4"],["2","8","7","4","1",".","6","3","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
# board = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],[".",".",".",".","8",".",".","7","9"]]
solu = Solution()
(solu.solveSudoku(board))
print(board)

