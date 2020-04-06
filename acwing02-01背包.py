import sys
N,V = list(map(int,sys.stdin.readline().strip().split()))
# !!!!!!
V+=1
things = []
for line in sys.stdin:
    things.append(list(map(int,line.strip().split())))

# 动态规划
# dp[i][j] 表示 对第i件物品能用j容量达到的最大价值
dp = [[0 for _ in range(V)] for _ in range(N)]
dp[0][things[0][0]] = things[0][1]
for i in range(1,N):
    for j in range(0,V):
        # 如果什么都不选
        temp1 = dp[i-1][j]
        temp2 = 0
        # 如果选
        if 0 <= j-things[i][0] <=V:
            temp2 = max(temp2,dp[i-1][j-things[i][0]]+things[i][1])
        dp[i][j] = max(temp1,temp2)

print(max(dp[-1]))
        
        
