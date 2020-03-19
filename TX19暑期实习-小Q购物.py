'''
小Q去商场购物，经常会遇到找零的问题。

小Q现在手上有n种不同面值的硬币，每种面值的硬币都有无限多个。

为了方便购物，小Q希望带尽量少的硬币，并且要能组合出1到m之间（包含1和m）的所有面值。

输入格式
第一行包含两个整数m和n。

接下来n行，每行一个整数，第 i+1 行的整数表示第 i 种硬币的面值。

输出格式
输出一个整数，表示最少需要携带的硬币数量。

如果无解，则输出-1。

数据范围
1≤n≤100,
1≤m≤109，
1≤硬币面值≤109
输入样例：
20 4
1
2
5
10
输出样例：
5

https://www.acwing.com/problem/content/603/

'''


# import sys
# m,n = list(map(int,sys.stdin.readline().strip().split()))
# money = []
# for line in sys.stdin:
#     money.append(int(line.strip().split()[0]))

# # 动态规划dp[i] = 1 if i in money else = min(dp[i-1]+dp[1], dp[i-2]+d[2])
# if not min(money) == 1:
#     print(-1)
#     exit()
# dp = [i+1 for i in range(m)]
# dp_s = ['' for i in range(m)]
# dp_s[0] = [1]
# for i in range(1,m):
#     if i+1 in money:
#         # 如果恰好有，则
#         dp[i] = 1
#         dp_s[i] = [i+1]
#     else:
#         for j in range(0,(i+1)//2+1):
#             dp[i] = min(dp[i],dp[j]+dp[i-1-j])
#             if dp[i] == dp[j]+dp[i-1-j]:
#                 dp_s[i] = dp_s[j]+dp_s[i-1-j]

# print(max(dp))




import sys
m,n = list(map(int,sys.stdin.readline().strip().split()))
money = []
for line in sys.stdin:
    money.append(int(line.strip().split()[0]))
if not money[0] == 1:
    print(-1)
    exit()

area = 0
pt = 1
ans = 0
money_pt = 0
while pt <= m:
    # 组合出1,2,3,4...m
    if pt in money:
        # 如果money中有pt这个数，那么肯定使用这个数
        ans+=1
        area += pt
    # else:
        # pt不在money中了，需要额外加旧硬币组合
        # pt += 
        
print(ans)