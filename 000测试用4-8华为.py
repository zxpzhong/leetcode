matrix = []
for _ in range(9):
    temp = input()
    temp = temp[1:-1]
    matrix.append(list(map(int,temp.strip().split(','))))


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
                if board[i][j] == 0:
                    # 当前位置可选
                    candi = [t for t in range(1,10)]
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
                        board[i][j] = 0
                    return False
        if tempi == 8 and tempj == 8:
            return True

solu = Solution()
solu.solveSudoku(matrix)
for item in matrix:
    ans = '{'
    for item2 in item:
        ans+=str(item2)+','
    # ans+='}'
    print(ans[:-1]+"}")

