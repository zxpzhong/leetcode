import sys 
def info(str):
    if True:
        print(str)
# for line in sys.stdin:
    # N = int(line.split()[0])
    # M = int(line.split()[1])
N=1 
M=12345
info(M)
info(N)
def isOK(first):
    # 吃掉的计数器
    eat_all = 0
    # 当天可以吃掉的最多
    max_day = first
    for i in range(N):
        eat_all+=max_day
        max_day = max_day//2 + (1 if max_day%2 else 0)
        info('eat_all: '+str(eat_all)+' max_day: '+str(max_day))
    if eat_all <= M:
        return True
    else:
        return False
# 二分法，类似二分排序
# 第一天吃的
min_first = 1
max_first = M
max_ = 0
first = 0
while max_first-min_first >1:
    # 取二分中点
    first = (max_first+min_first)//2
    if isOK(first):
        info('first :' + str(first) + " yes")
        # 吃得掉
        max_ = max(max_,first)
        min_first = first
    else:
        info('first :' + str(first) + " no")
        # 吃不掉
        max_first = first
if isOK(max_+1):
    print(max_+1)
else:
    print(max_)
    