# #coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys

# for line in sys.stdin:
#     m,n = list(map(int,line.strip().split()))
#     print(m+n)
'''
'''


#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys

# line = sys.stdin.readline().strip()
# candi = []
# for i in range(len(line)):
#     if line[i] not in candi:
#         candi.append(line[i])
#         print(line[i],end='')


'''
'''

# 192.168.1.1 192.168.1.2 255.255.255.0
# 192.168.1.1 192.168.2.1 255.255.255.0
# import sys

# addr1,addr2,mask = sys.stdin.readline().strip().split()
# # 得到字符串

# # 分割
# addr1 = list(map(int,addr1.split('.')))
# addr2 = list(map(int,addr2.split('.')))
# mask = list(map(int,mask.split('.')))
# # 按位与
# ans = ''
# for i in range(4):
#     addr1[i] = addr1[i] & mask[i]
#     addr2[i] = addr2[i] & mask[i]
#     ans+=str(addr1[i])+'.'
# if addr1 == addr2:
#     print(1,end = ' ')
# else:
#     print(0,end = ' ')
# print(ans[:-1])


'''
最大正方形矩形
3
1 1 0
1 1 1
1 1 0

3
1 1 0
1 0 1
1 1 0

4
0 1 1 1
1 0 1 1
1 1 1 1
1 1 1 0

3
0 1 1 1 1
1 0 1 1 1
1 1 1 1 1
1 1 1 0 1

1
1 1 1 1 1 1

8
1 0 1 0 1 1 1 1 1 1
0 0 0 0 0 0 0 1 1 1
1 0 1 0 1 1 0 1 1 1
0 0 0 0 1 1 1 1 1 1
1 0 1 0 1 1 1 1 1 1
0 0 0 0 0 0 1 1 0 1
1 0 1 0 1 1 1 1 1 1
0 0 0 0 1 1 0 0 0 1
'''

# import sys

# lines = int(sys.stdin.readline().strip())
# matrix = []
# for line in sys.stdin:
#     # 读取矩阵每一行
#     matrix.append(list(map(int,line.strip().split())))
# pass

# def ans(i,j):
#     ans = 1
#     temp = 1
#     while i+temp < len(matrix) and j+temp < len(matrix[0]):
#         for t in range(temp):
#             if not matrix[i][j+t+1] == 1:
#                 flag = 1
#                 break
#         for t in range(temp):
#             if not matrix[i+t+1][j] == 1:
#                 flag = 1
#                 break
#         if flag == 1:
#             return temp
        



# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         # 对于每个元素都遍历
#         matrix







import sys

lines = int(sys.stdin.readline().strip())
matrix = []
for line in sys.stdin:
    # 读取矩阵每一行
    matrix.append(list(map(int,line.strip().split())))
pass
# 动态规划：if M[i,j] == 1  -> dp[i,j] = dp[i-1][j-1]+1
# else -> dp[i,j] = max(dp[i-1,j],dp[i][j-1])
dp = [[0 for _ in range(len(matrix[0]))]for _ in range(lines)]
# 初始条件
# 列初始
for i in range(len(matrix)):
    dp[i][0] = matrix[i][0]
# 列初始
for i in range(len(matrix[0])):
    dp[0][i] = matrix[0][i]

for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i][j] == 1:
            # 检查行列
            # matrix[i-1][j] == 1 and matrix[i][j-1] == 1
            temp = dp[i-1][j-1]
            flag = 0
            for t in range(temp):
                if not matrix[i][j-t-1] == 1:
                    flag = 1
                    break
            for t in range(temp):
                if not matrix[i-t-1][j] == 1:
                    flag = 1
                    break
            # dp[i][j] = max(dp[i-1][j],dp[i][j-1])+1
            if flag == 1:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                # dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+1
        else:
            # dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            dp[i][j] = 0

# 扫描最大值
ans = 0
for item in dp:
    for i in item:
        ans = max(ans,i)
print(ans**2)




