# n,M = list(map(int,input().strip().split()))
# nums = list(map(int,input().strip().split()))

# def lowbit(x):
#     return  x&(-x)

# # 构建树状数组
# Tree = [0]*n

# def add(p,v):
#     while p <= n:
#         Tree[p-1] += v
#         p += lowbit(p)

# def sum_(p):
#     ans =0
#     while p>0:
#         ans += Tree[p-1]
#         p -= lowbit(p)
#     return ans


# for i in range(1,n+1):
#     add(i,nums[i-1])
# ans = 0
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         temp1 = sum_(j)
#         temp2 = sum_(i-1)
#         temp = temp1-temp2
#         if (temp) % M == 0:
#             ans+=1
# print(ans)


n,m = list(map(int,input().strip().split()))
A = list(map(int,input().strip().split()))

from collections import defaultdict

s = defaultdict(int)
sum = 0
ans = 0
s[0] = 1
for i in range(n):
    sum = (sum+A[i])%m
    ans+= s[sum]
    s[sum]+=1

print(ans)