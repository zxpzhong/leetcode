n = int(input().strip())
A = list(map(int,input().strip().split()))
if n == 1:
    print(-1)
    exit()
if n == 2:
    print(A[1]-A[0])
    exit()
sub = [0]*(n-1)
# 构建差分数组
for i in range(n-1):
    sub[i] = A[i+1]-A[i]

def gcd(x,y):
    return x if y == 0 else gcd(y,x%y)
a = sub[0]
for i in range(1,n-1):
    b = sub[i]
    b = gcd(a,b)
    a = b
if b >= 1:
    print(b)
else:
    print(-1)


# candi = {}
# # 欧几里得算法，所有的求交集
# for i in range(n-1):
#     temp = sub[i]
#     if i == 0:
#         # 初始化candi
#         s  = 2
#         while temp > 1:
#             time = 0
#             while temp%s == 0:
#                 temp/=s
#                 time +=1
#             if time >= 1:
#                 candi[s] = time
#             s+=1
#         if temp > 0:
#             candi[temp] = 1
#     else:
#         # 初始化candi
#         s  = 2
#         while temp > 1:
#             time = 0
#             while temp%s == 0:
#                 temp/=s
#                 time +=1
#             if time >= 1 and s in candi:
#                 candi[s] = min(candi[s],time)
#             s+=1
#         if temp > 0 and temp in candi:
#             candi[temp] = 1
# ans = 1
# for key in candi.keys():
#     ans*= qmi(key,candi[key])
# if ans == 1:
#     print(-1)
# else:
#     print(int(ans))