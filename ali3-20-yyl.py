'''题目
    
1 1 1 2 2 2 2 2 1 1
3

1 1 2 2 2 2 2 2 1 1
4

2 2 2 2 2 2 2 2 2 2
4

2 1 2 0 2 0 2 1 2 0
7

4 4 4 4 4 4 4 4 4 4

4 4 0 4 4 0 4 4 0 4
10

1 2 2 2 1 0 0 0 0 0

2 2 2 1 1 0 0 0 0 0
'''

import sys
cards = list(map(int,sys.stdin.readline().strip().split()))

# 广度优先

def cut_one(left,time):
    # left为剩余牌数
    # time为当前次数
    next_left = []
    
    for item in left:
        # 找到出牌的第一手
        for i,t in enumerate(item):
            if not t == 0:
                break
        # 对于每一手牌
        # 3. 出顺子
        # for i in range(6):
        if i < 6:
            if item[i] > 0 and item[i+1] > 0 and item[i+2] > 0 and item[i+3] > 0 and item[i+4] > 0 :
                next_left.append(item[:i]+[item[i]-1]+[item[i+1]-1]+[item[i+2]-1]+[item[i+3]-1]+[item[i+4]-1]+item[i+5:])
                if sum(next_left[-1]) == 0:
                    return time+1
        # 4. 出连对
        # for i in range(8):
        if i < 8:
            if item[i] >= 2 and item[i+1] >= 2 and item[i+2] >= 2:
                next_left.append(item[:i]+[item[i]-2]+[item[i+1]-2]+[item[i+2]-2]+item[i+3:])
                if sum(next_left[-1]) == 0:
                    return time+1
        # 2. 出对子
        # for i in range(9):
        if item[i] >= 2:
            next_left.append(item[:i]+[item[i]-2]+item[i+1:])
            if sum(next_left[-1]) == 0:
                return time+1
            
        # 1. 出单牌：
        # for i in range(10):
        if item[i] > 0:
            next_left.append(item[:i]+[item[i]-1]+item[i+1:])
            if sum(next_left[-1]) == 0:
                return time+1
    # 结束判断
    return cut_one(next_left,time+1)

if sum(cards) == 0:
    print(0)
else:
    print(cut_one([cards],0))

