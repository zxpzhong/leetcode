'''
1 2 0 
0 3 4
0 6 5

1 2 3
0 0 4
0 6 0
'''
import sys
import functools
matrix = []
for line in sys.stdin:
    # 读取矩阵每一行
    matrix.append(list(map(int,line.strip().split())))
pass
if matrix[0][0] == 0:
    print(-1)
    exit()

# 最大怪兽
nums = []
for item in matrix:
    for i in item:
        if i > 1:
            nums.append(i)
nums.sort()

# trace = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
# trace[0][0] = 1
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if 

# @functools.lru_cache()
# 暴力递归LRU

# # 当前位置list，已经消灭的怪兽list
# @functools.lru_cache()
def go(i,j,kill,way):
    # 退出条件
    # 每次只走一步，从loc位置开始
    # 左
    ans1 = -1
    ans2 = -1
    ans3 = -1
    ans4 = -1
    if len(way) == len(matrix)*len(matrix[0]):
        # 无路可走
        return -1
    # 上
    if i > 0:
        if matrix[i-1][j] > 0 and [i-1,j] not in way:
            if matrix[i-1][j] == 1:
                go(i-1,j,kill,way+[[i-1,j]])
            elif nums[kill] == matrix[i-1][j]:
                if kill+1 == len(nums):
                    # 全部杀完
                    return len(way)
                ans1 = go(i-1,j,kill+1,way+[[i-1,j]])
                if ans1 > 0:
                    return ans1
    # 下
    if i < len(matrix[0])-1:
        if matrix[i+1][j] > 0 and [i+1,j] not in way:
            if matrix[i-1][j] == 1:
                go(i+1,j,kill,way+[[i+1,j]])
            elif nums[kill] == matrix[i+1][j]:
                if kill+1 == len(nums):
                    # 全部杀完
                    return len(way)
                ans2 = go(i+1,j,kill+1,way+[[i+1,j]])
                if ans2 > 0:
                    return ans2
    # 左
    if j > 0:
        if matrix[i][j-1] > 0 and [i,j-1] not in way:
            if matrix[i][j-1] == 1:
                go(i,j-1,kill,way+[[i,j-1]])
            elif nums[kill] == matrix[i][j-1]:
                if kill+1 == len(nums):
                    # 全部杀完
                    return len(way)
                ans3 = go(i,j-1,kill+1,way+[[i,j-1]])
                if ans3 > 0:
                    return ans3
    # 右
    if j< len(matrix)-1:
        if matrix[i][j+1] > 0 and [i,j+1] not in way:
            if matrix[i][j+1] == 1:
                go(i,j+1,kill,way+[[i,j+1]])
            elif nums[kill] == matrix[i][j+1]:
                if kill+1 == len(nums):
                    # 全部杀完
                    return len(way)
                ans4 = go(i,j+1,kill+1,way+[[i,j+1]])
                if ans4 > 0:
                    return ans4
    # 如果运行到这，运行结束
    # 四个方向中步数最小的
    # temp = min(max(ans1,0),max(ans2,0),max(0,ans3),max(0,ans4))
    return -1

ans = go(0,0,0,[[0,0]])
if ans == -1:
    print(-1)
else:
    print(ans+1)
