'''题目
    
'''

import sys

n,m = list(map(int,sys.stdin.readline().strip().split()))

matrix = []
for line in sys.stdin:
    matrix.append(list(line.strip().split()))

# 广度优先

def step(loc,flytime_list,path):
    next_loc = []
    next_path = []
    fly_time = []
    length = len(loc)
    for i in range(length):
        # 对于每一种情况
        row,col = loc[i]
        cur_path = path[i]
        flytime = flytime_list[i]
        # 左移
        if col > 0 and not matrix[row][col-1] == '#' and not [row,col-1] in cur_path:
            next_loc.append([row,col-1])
            next_path.append(cur_path+[[row,col-1]])
            if matrix[row][col-1] == 'E':
                return len(cur_path)
            fly_time.append(flytime)
        # 右移
        if col < m-1 and not matrix[row][col+1] == '#' and not [row,col+1] in cur_path:
            next_loc.append([row,col+1])
            next_path.append(cur_path+[[row,col+1]])
            if matrix[row][col+1] == 'E':
                return len(cur_path)
            fly_time.append(flytime)
        # 上移
        if row > 0 and not matrix[row-1][col] == '#' and not [row-1,col] in cur_path:
            next_loc.append([row-1,col])
            next_path.append(cur_path+[[row-1,col]])
            if matrix[row-1][col] == 'E':
                return len(cur_path)
            fly_time.append(flytime)
        # 下移
        if row < n-1 and not matrix[row+1][col] == '#' and not [row+1,col] in cur_path:
            next_loc.append([row+1,col])
            next_path.append(cur_path+[[row+1,col]])
            if matrix[row+1][col] == 'E':
                return len(cur_path)+1
            fly_time.append(flytime)
        # 对称
        if 0 <= n-1-row <= n-1 and 0 <= m-1-col <= m-1  and not matrix[n-1-row][m-1-col] == '#' and not [n-1-row,m-1-col] in cur_path and flytime > 0:
            next_loc.append([n-1-row,m-1-col])
            next_path.append(cur_path+[[n-1-row,m-1-col]])
            if matrix[n-1-row][m-1-col] == 'E':
                return len(cur_path)
            fly_time.append(flytime-1)
    if len(next_loc) == 0:
        return -1
    return step(next_loc,fly_time,next_path)


loc = []
# 遍历得到起点位置
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 'S':
            loc = [i,j]
            break
    if loc:
        break
flytime = [5]
path = [[[i,j]]]
loc = [loc]

print(step(loc,flytime,path))


