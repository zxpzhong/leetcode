T = int(input().strip())
for _ in range(T):
    # 正整数个数N，操作数M
    N,M = list(map(int,input().strip().split()))
    # 储存状态
    status = [i for i in range(1,N+1)]
    for t in range(1,M+1):
        temp  = list(map(int,input().strip().split()))
        if len(temp) == 3:
            op,num1,num2 = temp
        else:
            op,num = temp
        
        if op == 1:
            # 绑定两个集合num1,num2
            set1 = status[num1-1]
            set2 = status[num2-1]
            if set1 == set2:
                continue
            for i in range(N):
                if status[i] == set2:
                    status[i] = set1
        elif op == 2:
            status[num-1] = N+t
        else:
            set1 = status[num-1]
            count = 0
            for i in range(N):
                if status[i] == set1:
                    count+=1
            print(count)

