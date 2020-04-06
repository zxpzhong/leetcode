# import sys
# N,V = list(map(int,sys.stdin.readline().strip().split()))
# texts = []
# for line in sys.stdin:
#     texts.append(list(map(int,line.strip().split())))
# ans = 0

# dp = [[0 for _ in range(V+1)] for _ in range(N)]
# for j in range(1,V+1):
#     dp[0][j] = j//texts[0][0]*texts[0][1]
# for i in range(1,N):
#     for j in range(1,V+1):
#         # 不买的话
#         temp1 = dp[i-1][j]
#         # 买的话，还要额外考虑买几件？
#         # j元可以购买texts[i][0]的数目为 j//texts[i][0]
#         temp2 = 0
#         for t in range(1,min(j//texts[i][0],texts[i][2])+1):
#             temp2 = max(temp2,dp[i-1][j-texts[i][0]*t]+texts[i][1]*t)
#         dp[i][j] = max(temp1,temp2)
# print(max(dp[-1]))
        
        

import collections
if __name__ == '__main__':
    goods = collections.namedtuple('good', ['v', 'w'])
    N, V = map(int, input().split())
    Goods = []
    dp = [0] * (V + 1)

    for i in range(N):
        # 体积价值数量
        v, w, s = map(int, input().split())
        k = 1
        # 小于数量限制
        while k <= s:
            # 
            s -= k
            Goods.append(goods._make([v*k, w*k]))
            k *= 2
        if s > 0: Goods.append(goods._make([v*s, w*s]))

    for good in Goods:
        for j in range(V, good.v - 1, -1):
            dp[j] = max(dp[j], dp[j - good.v] + good.w)

    print(dp[V])