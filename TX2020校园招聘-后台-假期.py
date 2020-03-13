'''题目
由于业绩优秀，公司给小Q放了 n 天的假，身为工作狂的小Q打算在在假期中工作、锻炼或者休息。
他有个奇怪的习惯：不会连续两天工作或锻炼。只有当公司营业时，小Q才能去工作，只有当健身房营业时，
小Q才能去健身，小Q一天只能干一件事。给出假期中公司，健身房的营业情况，求小Q最少需要休息几天。
第一行一个整数  表示放假天数
第二行 n 个数 每个数为0或1,第 i 个数表示公司在第 i 天是否营业
第三行 n 个数 每个数为0或1,第 i 个数表示健身房在第 i 天是否营业
（1为营业 0为不营业）
一个整数，表示小Q休息的最少天数
4
1 1 0 0
0 1 1 0

2
'''

import sys
n = list(map(int,sys.stdin.readline().strip().split()))[0]
company = list(map(int,sys.stdin.readline().strip().split()))
exer = list(map(int,sys.stdin.readline().strip().split()))
company2 = exer
assert n == len(company) == len(exer)
# 以上是公共代码

# 0休息  1 工作  2健身    第i天选择为0/1/2下的最大工作天数
dp = [[0 for i in range(n)] for _ in range(3)]
'''
注意第一天，选择休息，则工作天数=0，跟公司健身房开不开没有半毛钱关系！！！！
'''
dp[0][0] = 0
dp[1][0] = 1 if company[0] == 1 else 0
dp[2][0] = 1 if exer[0] == 1 else 0

# 开始状态转换
for i in range(1,n):
    # 不论是否开门，都可以选择休息！！！！！！！不是只有今天公司和健身房都不开门才休息
    dp[0][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
    if company[i] == 1:
        # 公司开门
        dp[1][i] = max(dp[0][i-1],dp[2][i-1]) + 1
    if exer[i] == 1:
        # 健身房开门
        dp[2][i] = max(dp[0][i-1],dp[1][i-1]) + 1
print(n-max(dp[0][-1],dp[1][-1],dp[2][-1]))




# 状态机那个图很重要！！！理解


# 以下是错误解法，妄图使用一个dp表示一天的三种选择！！！！
# dp = [0]*n
# # 初始化第一天
# dp[0] = 1 if company[0] == 1 or exer[0] == 1 else 0
# # 初始化第二天

# # 第二天全关
# if company[1] == 0 and exer[1] == 0:
#     dp[1] = dp[0]
# # 第一二天交叉开
# elif (company[1] == exer[0] == 1) or (company[0] == exer[1] == 1):
#     dp[1] = 2
# # 连续两天只有同一家开
# elif (company[1] == company[0] == 1 and exer[1]== exer[0]== 0 ) or (company[1] == company[0] == 0 and exer[1]== exer[0]== 1 ):
#     dp[1] = 1
# # 第一天不开第二天开
# elif company[0] == 0 and exer[0] == 0 and ((company[1] == 1 or exer[1] == 1)):
#     dp[1] = 1
# for i in range(2,n):
#     if exer[i] == company[i] == 1:
#         dp[i] = dp[i-1] + 1
#     elif exer[i] == company[i] == 0:
#         dp[i] = dp[i-1]
#     elif exer[i] == 1 and company[i] == 0:
#         # 健身房营业但是公司不营业
#         # if exer[i-1] == 1 and company[i-1] == 0:
#             # 前一天仍然同样情况
#         if company[i-1]== 1:
#             dp[i] = dp[i-1]+1
#         else:
#             dp[i] = max(dp[i-1],dp[i-2]+1)
#     elif exer[i] == 0 and company[i] == 1:
#         # 公司营业但是健身房不营业
#         # if exer[i-1] == 0 and company[i-1] == 1:
#             # 前一天仍然同样情况
#         if exer[i-1]== 1:
#             dp[i] = dp[i-1]+1
#         else:
#             dp[i] = max(dp[i-1],dp[i-2]+1)
# print(n-dp[-1])