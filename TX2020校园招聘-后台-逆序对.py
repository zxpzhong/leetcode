import sys
n = list(map(int,sys.stdin.readline().strip().split()))[0]
nums = list(map(int,sys.stdin.readline().strip().split()))
m = list(map(int,sys.stdin.readline().strip().split()))[0]
op = list(map(int,sys.stdin.readline().strip().split()))
# print(n)
# print(nums)
# print(n)
# print(op)
assert 2**n == len(nums) and m == len(op)

for t in range(m):
    # 1.0 翻转
    pt = 0
    while (pt + 2**op[t]) <= 2**n:
        nums[pt:pt+2**op[t]] = nums[pt:pt+2**op[t]][::-1]
        pt+=2**op[t]
    # 2.0 计算逆序对数目
    dp = [0]*(2**n)
    for i in range(1,2**n):
        for j in range(i-1,-1,-1):
            if nums[j] > nums[i]:
                dp[i] = dp[j]+1
                break
    # 2.1 dp中每个元素的值表示，前面有多少个数是逆序的，每个数都可以组成一个逆序对
    print(sum(dp))