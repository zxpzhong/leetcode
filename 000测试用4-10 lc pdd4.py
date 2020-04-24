N,K = list(map(int,input().strip().split()))
string = input().strip()
nums = [int(string[i]) for i in range(N)]
from collections import Counter
count = Counter(nums)
temp = []
for key in count.keys():
    temp.append([key,count[key]])

temp.sort(key=lambda x:x[0])

leng = len(temp)
print(temp)
min_loss = 10**9
min_op = []
for i in range(leng):
    # 每次以temp[i][0]为修改基准
    # 需要从附近找K-temp[i][1]个数
    res = K-temp[i][1]
    pt = i
    loss = 0
    op = [temp[i][0]]
    left = pt-1
    right = pt+1
    while not res == 0:
        # left = pt-1
        # right = pt+1
        # 先看左边还是右边
        if left >= 0 and right < leng:
            if temp[pt][0]-temp[left][0] <= temp[right][0]-temp[pt][0]:
                # 先选左边的
                if temp[left][1] >= res:
                    loss+=res*abs(temp[pt][0]-temp[left][0])
                    op.append([temp[left][0],res])
                    res = 0
                else:
                    loss+=temp[left][1]*abs(temp[pt][0]-temp[left][0])
                    res = res-temp[left][1]
                    op.append([temp[left][0],temp[left][1]])
                left-=1
            else:
                # 先选右边的
                if temp[right][1] >= res:
                    loss+=res*abs(temp[pt][0]-temp[right][0])
                    op.append([temp[right][0],res])
                    res = 0
                else:
                    loss+=temp[right][1]*abs(temp[pt][0]-temp[right][0])
                    op.append([temp[right][0],temp[right][1]])
                    res = res-temp[right][1]
                right+=1
        elif left == -1:
            temp2 = res
            res = max(0,res-temp[right][1])
            loss+=(temp2-res)*abs(temp[pt][0]-temp[right][0])
            op.append([temp[right][0],temp2-res])
            right+=1
        elif right == leng:
            temp2 = res
            res = max(0,res-temp[left][1])
            loss+=(temp2-res)*abs(temp[pt][0]-temp[left][0])
            op.append([temp[left][0],temp2-res])
            left-=1
    if loss < min_loss:
        min_loss = loss
        min_op = [op]
    elif loss == min_loss:
        min_op.append(op)

print(min_loss)
print(min_op)


for i in range(len(min_op)):
    op = min_op[i]
    base = op[0]
    for i in range(1,len(op)):
        

