'''
小Q打算穿越怪兽谷，他不会打怪，但是他有钱。

他知道，只要给怪兽一定的金币，怪兽就会一直护送着他出谷。

在谷中，他会依次遇见N只怪兽，每只怪兽都有自己的武力值和要“贿赂”它所需的金币数。

如果小Q没有“贿赂”某只怪兽，而这只怪兽“武力值”又大于护送他的怪兽武力之和，这只怪兽就会攻击他。

小Q想知道，要想成功穿越怪兽谷而不被攻击，他最少要准备多少金币。

输入格式
第一行包含整数N，表示怪兽的数量。

第二行包含N个整数d1,d2,…,dn，表示每只怪兽的武力值。

第三行包含N个整数p1,p2,…,pn，表示收买N只怪兽所需的金币数。

输出格式
输出一个整数，表示所需最小金币数。

数据范围
1≤N≤50,
1≤di≤1012,
1≤pi≤2
输入样例1：
3
8 5 10
1 1 2
输出样例1：
2
输入样例2：
4
1 2 4 8
1 2 1 2
输出样例2：
6
https://www.acwing.com/problem/content/605/

'''

# 递归超时
# ans = []

# # 自己构建缓存
# cache = {}

# # 递归
# def meetone(f_sum,m_sum,f_left,money_left):
#     label = str(f_sum)+str(f_left)+str(money_left)
#     if label in cache:
#         return cache[label]
#     if len(f_left) == 0:
#         if label not in cache:
#             cache[label] = m_sum
#         return m_sum
#     else:
#         # 两种操作，买或者不买，暴力递归
#         # 买
#         temp1 = meetone(f_sum+f_left[0],m_sum+money_left[0],f_left[1:],money_left[1:])
#         # 不买
#         temp2 = temp1
#         if f_sum >= f_left[0]:
#             temp2 =  meetone(f_sum,m_sum,f_left[1:],money_left[1:])
#         temp = min(temp1,temp2)
#         if label not in cache:
#             cache[label] = temp
#         return temp

# ans = meetone(0,0,force,money)
# print((ans))




# 3-17 Accepted
import sys
N = list(map(int,sys.stdin.readline().strip().split()))[0]
force = list(map(int,sys.stdin.readline().strip().split()))
money = list(map(int,sys.stdin.readline().strip().split()))

# 动态规划,dp[i][j]第i个怪兽花掉第j个金币的最大攻击力
# 最终结果为dp[-1]符合条件的最小j
dp = [[-1 for _ in range(2*len(force)+1)] for _ in range(len(force))]
# 初始条件
# 第一关你不得不买！！！
# dp[0][0] = 0
dp[0][money[0]] = force[0]
for i in range(len(force)):
    # 到第i步花的最多钱为2*i
    for j in range(1,2*(i+1)+1):
        if j>=money[i] and not dp[i-1][j-money[i]] == -1:
            # 保证索引合法以及前一个状态合法
            dp[i][j]=dp[i-1][j-money[i]]+force[i]
        if not dp[i-1][j]==-1 and dp[i-1][j]>=force[i]:
            dp[i][j]=max(dp[i][j],dp[i-1][j])
# 不为-1的最小值
ans = -1
for i in range(len(dp[-1])):
    if not dp[-1][i] == -1:
        print(i)
        break
