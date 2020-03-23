import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    mystrs = []
    for _ in range(n):
        mystrs.append(sys.stdin.readline().strip())

    mystrs.sort(key = lambda x:x[0])
    
    dp = [len(mystrs[i]) for i in range(len(mystrs))]
    for i in range(1, len(dp)):
        for j in range(i):
            if mystrs[i][0] >= mystrs[j][-1]:
                dp[i] = max(dp[i], dp[j]+len(mystrs[i]))
    result = max(dp)
    print(result)