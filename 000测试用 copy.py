N = int(input())
P = list(map(float,input().strip().split()))
A = list(map(float,input().strip().split()))

# DP，表示第i颗子弹的最高分
# 
dp = [[0,0] for _ in range(N)]
dp[0][0] = P[0]*A[0]
dp[0][1] = P[0]
for i in range(1,N):
    dp[i][0] = A[i]*P[i]
    dp[i][1] = P[i]
    for j in range(i):
        val = dp[j][0]+dp[j][1]*P[i-1-j]*A[i-1-j]
        if val>dp[i][0]:
            dp[i][0] = val
            dp[i][1] = dp[j][1]*P[i-1-j]

print("%.2f"%dp[-1][0])



'''
4
0.9 0.90 0.90 0.90
20 10 60 40
61.90
'''