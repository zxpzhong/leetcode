'''题目
游戏里面有很多各式各样的任务，其中有一种任务玩家只能做一次，这类任务一共有1024个，任务ID范围[1,1024]。请用32个unsigned int类型来记录着1024个任务是否已经完成。初始状态都是未完成。 输入两个参数，都是任务ID，需要设置第一个ID的任务为已经完成；并检查第二个ID的任务是否已经完成。 输出一个参数，如果第二个ID的任务已经完成输出1，如果未完成输出0。如果第一或第二个ID不在[1,1024]范围，则输出-1。
输入包括一行,两个整数表示人物ID.
输出是否完成

1024 1024

1
'''


# 这道题就考一个移位，>>1python也可以移位
import sys
s = sys.stdin.readline().strip()
# 。。。。


# 链接：https://www.nowcoder.com/questionTerminal/2f45f0ef94724e06a4173c91ef60781c
# 来源：牛客网

import sys
t1, t2 = list(map(int, input().split()))
task = [0] * 32
if t1 in range(1, 1025) and t2 in range(1, 1025):
    index1 = int((t1-1)/32)
    index2 = (t1-1)%32
    if not task[index1] & (1<<index2): 
        task[index1] = task[index1] + 1<<index2
    index1 = int((t2-1)/32)
    index2 = (t2-1)%32
    if task[index1]&(1<<index2):
        print(1)
    else:
        print(0)
else:
    print(-1)



'''
3、4题都及其简单，不再这里单列！！！
第四题注意-1//2 = -2而不是-1，余数永远是正的！！！记住
'''