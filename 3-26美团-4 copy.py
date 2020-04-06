N, K = map(int, input().split())
a = list(map(int, input().split()))

MOD = 998244353

for i in range(K):
    temp = []
    for j in range(len(a)):
        if j==0:
            temp.append(a[j])
        else:
            temp.append(temp[-1]+a[j])
    a = temp[:]
result = a[N-1] % MOD
print(result)