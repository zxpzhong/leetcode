#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (39.12%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 85.9K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#

# @lc code=start
class Solution(object):
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # 可以抽象为一个四分树搜索，这里判断的是是否存在，应该采用深度优先
        self.row = len(board)
        self.column = len(board[0])
        self.word = word
        self.board = board
        self.ans_len = len(word)
        self.ans = 0
        self.mark = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 遍历棋盘，找首
                if self.board[i][j] == word[0]:
                    self.mark[i][j] = 1
                    if self.isexistround(i,j,1):
                        return True
                    self.mark[i][j] = 0
        if self.ans > 0:
            return True
        return False

        
    def isexistround(self,i,j,target):
        # board上第ij位置的四邻域是否存在目标target,已经走过的路径在ans中

        if target == self.ans_len:
            self.ans +=1
            return True
        flag = 0
        # 左边
        if j >0 and self.board[i][j-1] == self.word[target] and self.mark[i][j-1] == 0:
            self.mark[i][j-1] = 1
            if not self.isexistround(i,j-1,target+1):
                self.mark[i][j-1] = 0
            else:
                # 终止条件这里，任意一个找到了，就直接退出，不要墨迹
                return True
        # 上面
        if i >0 and self.board[i-1][j] == self.word[target] and self.mark[i-1][j] == 0:
            self.mark[i-1][j] = 1
            if not self.isexistround(i-1,j,target+1):
                self.mark[i-1][j] = 0
            else:
                return True
        # 下面
        if i<self.row-1 and self.board[i+1][j] == self.word[target] and self.mark[i+1][j] == 0:
            self.mark[i+1][j] = 1
            if not self.isexistround(i+1,j,target+1):
                self.mark[i+1][j] = 0
            else:
                return True
        # 右边
        if j < self.column-1 and self.board[i][j+1] == self.word[target] and self.mark[i][j+1] == 0:
            self.mark[i][j+1] = 1
            if not self.isexistround(i,j+1,target+1):
                self.mark[i][j+1] = 0
            else:
                return True
        return False
        # if flag == 0:
            # 未找到满足条件，回溯
        # self.mark[i][j] = 0

    #     m = len(board)
    #     if m == 0:
    #         return False
    #     n = len(board[0])
    #     # 是否重复标志位
    #     mark = [[0 for _ in range(n)] for _ in range(m)]
    #     # 遍历棋盘格找到首位
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == word[0]:
    #                 # 将该元素标记为已使用
    #                 mark[i][j] = 1
    #                 if self.backtrack(i, j, mark, board, word[1:]) == True:
    #                     return True
    #                 else:
    #                     # 回溯
    #                     mark[i][j] = 0
    #     return False
        
        
    # def backtrack(self, i, j, mark, board, word):
    #     if len(word) == 0:
    #         return True
    #     # 搜索四个方向
    #     for direct in self.directs:
    #         cur_i = i + direct[0]
    #         cur_j = j + direct[1]
    #         # 判断是否满足边界条件
    #         if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
    #             # 如果是已经使用过的元素，忽略
    #             if mark[cur_i][cur_j] == 1:
    #                 continue
    #             # 将该元素标记为已使用
    #             mark[cur_i][cur_j] = 1
    #             if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
    #                 return True
    #             else:
    #                 # 回溯
    #                 mark[cur_i][cur_j] = 0
    #     return False
  

# @lc code=end

# board =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED"
# board = [["A","B","C","E"],
# ["S","F","E","S"],
# ["A","D","E","E"]]
# word = "ABCESEEEFS"

board = [["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]]
word = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

solu = Solution()
print(solu.exist(board,word))


