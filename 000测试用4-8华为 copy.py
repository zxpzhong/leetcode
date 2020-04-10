import sys
while True:
    A,B = list(map(int,input().strip().split()))
    if A == 0 and B == 0:
        break
    mod = 10**9+7
    def qmi(s,p):
        temp = 1
        while p > 0:
            if p&1 : temp=(temp)*(s)
            s=(s*s)%mod
            p = p>>1
        return temp%mod

    def sum_(s,c):
        ans = 0
        if c == 0: return 1
        elif c % 2 == 0: ans+= (s*sum_(s,c-1)+1)%mod
        else:
            ans+=  (1+qmi(s,c//2+1))*(sum_(s,c//2))
        return ans%mod

    # print((sum_(15,100)-1)%mod)
    print((sum_(A,B)-1)%mod)
    # print(ans%mod)
    