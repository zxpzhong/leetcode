import sys
n = list(map(int,sys.stdin.readline().strip().split()))[0]
v = list(map(int,sys.stdin.readline().strip().split()))
# n = 6
# v = [5,3 ,8 ,3 ,2 ,5]
dp_l = [0 for _ in range(n)]
# 向左遍历
stack = [v[0]]
for i in range(1,n):
    dp_l[i] = len(stack)
    # 更新栈
    while True:
        if stack:
            if stack[-1] <= v[i]:
                stack.pop()
            else:
                stack.append(v[i])
                break
        else:
            stack.append(v[i])
            break

dp_r = [0 for _ in range(n)]
v_inv = v[::-1]
# 向右遍历
stack = [v_inv[0]]
for i in range(1,n):
    dp_r[i] = len(stack)
    # 更新栈
    while True:
        if stack:
            if stack[-1] <= v_inv[i]:
                stack.pop()
            else:
                stack.append(v_inv[i])
                break
        else:
            stack.append(v_inv[i])
            break
# 加和
for i in range(n): print(dp_l[i]+dp_r[n-i-1]+1,end=' ')
