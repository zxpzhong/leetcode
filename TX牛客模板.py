# '''题目
    
# '''

import sys
s = sys.stdin.readline().strip()

n = list(map(int,sys.stdin.readline().strip().split()))[0]

texts = []
for line in sys.stdin:
    texts.append(line.split())


# import sys
# import math
# mod = 10**9+7
# def ksm(n, k):
#     res = 1
#     while k :
#         if(k & 1):
#              res = (res * n) % mod
#         n = (n * n) % mod
#         k >>= 1
#     return res % mod


# n = int(sys.stdin.readline().strip())
# final = 0
# for s in range(1,n):
#     ans1 = 1
#     ans2 = 1
#     i = n
#     j = 1
#     while j <= s:
#         ans1 = (ans1 * i) % mod
#         j+=1
#         i-=1

#     i = 1
#     while i <= s:
#         i+=1
#         ans2 = (ans2 * i) % mod
#     ans2 = ksm(ans2, mod - 2)
#     ans = (((ans1 * ans2) % mod) * ksm(2, n - s)) % mod
#     final+=ans
# print(final + n)
