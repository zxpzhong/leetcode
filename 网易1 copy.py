T = int(input().strip())

def count(pt):
    for i in range(len(status[pt-1])):
        if not status[pt-1][i] in pool:
            pool.append(status[pt-1][i])
            count(status[pt-1][i])

for _ in range(T):
    # 正整数个数N，操作数M
    N,M = list(map(int,input().strip().split()))
    # 双向链表储存状态
    status = [[] for i in range(1,N+1)]
    for t in range(1,M+1):
        temp  = list(map(int,input().strip().split()))
        if len(temp) == 3:
            op,num1,num2 = temp
        else:
            op,num = temp
        
        if op == 1:
            # 绑定两个集合num1,num2
            # 互指
            if num2 not in status[num1-1]:
                status[num1-1].append(num2)
            if num1 not in status[num2-1]:
                status[num2-1].append(num1)
        elif op == 2:
            # status[num-1] = N+t
            # 删除
            ptnums = len(status[num-1])
            for i in range(ptnums):
                # 遍历指向节点，删除所有的逆向节点
                status[status[num-1][i]-1].remove(num)
            # 删除自己指向
            status[num-1] = []
        else:
            pool = [num]
            count(num)
            print(len(pool))

