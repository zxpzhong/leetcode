# '''题目
# 2
# 3 1
# '''

import sys
# 获取输入
N,p,q = list(map(int,sys.stdin.readline().strip().split()))
A = list(map(int,sys.stdin.readline().strip().split()))

probo = (p*1.0)/(1.0*q)

ans = 0
# 每种情况的平均得分总和
for i in range(1,N+1):
    ans+= (((1-probo)**min(2,N-i)) * ((probo)**i) *sum(A[:i]))/(1.0*i)
print(ans*N)

