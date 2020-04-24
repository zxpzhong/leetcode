T = int(input().strip())
# import functools
# def Cal(A,B,V):
#     dis = 0
#     for i in range(1,N+1):
#         dis+=V[i-1]*abs(A.index(i)-B.index(i))
#     return dis
# # @functools.lru_cache()
# def DFS(t,pt,B,all):
#     ans = 10**9
#     if pt == N:
#         # return loss
#         return Cal(A,all,V)
#     idx = A.index(pt+1)
#     for i in range(N):
#         if not idx == i and not (B>>i & 1):
#             # 可以将pt安装在i位置
#             B = B|(1<<i)
#             # loss_cur = V[pt]*abs(A.index(pt+1)-i)
#             all[i] = pt+1
#             ans = min(ans,DFS(t,pt+1,B,all))
#             all[i] = 0
#             B = B & ~(1<<i)
#     return ans

for t in range(T):
    N = int(input().strip())
    A = list(map(int,input().strip().split()))
    V = list(map(int,input().strip().split()))
    dp = [[10**9]*N for i in range(N)]
    # 初始状态
    for i in range(1,N):
        dp[0][i] = V[A[i]-1]*abs(i-0)
    
    for i in range(1,N):
        for j in range(N):
            if not i == j:
                dp[i][j] += dp[i-1]



