'''

'''

import sys
n = list(map(int,sys.stdin.readline().strip().split()))[0]
t = list(map(int,sys.stdin.readline().strip().split()))


new_t = []
pt1 = 0
pt2 = 0
# 对于虽有的t元素，以0为固定切分，以2为分裂切分，然后统计每一段内的期望
for i in range(len(t)):
    if t[i] == 0:
        if pt2>pt1:
            new_t.append(t[pt1:pt2])
        # i+1下一个不能含i
        pt1 = i+1
        # pt2指向pt1的下一个位置
        pt2 = pt1
    else:
        pt2+=1
if pt2 > pt1:
    new_t.append(t[pt1:pt2])



# 每一段的期望值为val[i]
# 每一段期望值之和
ans = 0
for i in range(len(new_t)):
    temp = 0
    sessions = 1
    # 每个2处可能会出现0或者1，记录所有的2的位置
    idx = []
    length = len(new_t[i])
    for j in range(length):
        if new_t[i][j] == 2:
            idx.append(j)
            sessions+=1
    # 对于idx中每一个2，所有的可能为所有2位置的分裂，选出所有的加班的2，作为额外的金额增加，1个2，2个2，3个2，4个2。。全是2的所有结果之和
    # 都对导致后面所有的数随机增加(i+1)*()
    if idx:
        # 第一个
        temp += (idx[0]+1)*(length-idx[0])*(0+1)
        for t in range(1,len(idx)):
            temp += (idx[t]-idx[t-1])*(length-idx[t])*(t+1)
        
    # 最后加上全不加班的
    temp+=length-len(idx)
    ans+=temp/(sessions*1.0)
print(int(ans))






# # 递归
# def cut_one(state,number):
#     cur_sum = 0
#     if len(state) == 0:
#         return number
#     elif state[0] == 1:
#         cur_sum += cut_one(state[1:],number+1)
#     else:
#         number += cut_one(state[1:],number)
#         number += cut_one(state[1:],number+1)
    



