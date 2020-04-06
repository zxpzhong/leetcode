'''
给定一个100层的阶梯，阶梯间的高度差是递增的（e.g. 第一层和第二层之间间隔1,
 第二层和第三层间隔2, 以此类推）。同时给定一种玻璃球，
 这种玻璃球在层级之间掉落时有一定的承受度，如果高度差大于其承受范围的话，
 玻璃球就会碎掉，如果小于承受范围的话，就安全无事。
 现在我们的目标就是找到阶梯上的临界层k（其定义为k-1层->k层玻璃球是安全的，
 k层->k+1层玻璃球会碎）。

---
 现在给出几个定义：
1. 尝试（try）：从任意一层m，往相邻一层m+1，做一次掉落实验，称为一次尝试。

2. 策略（solution）：具体的尝试步骤构成一个策略

3. 策略的尝试次数上界（最坏情况下的尝试次数）：给定任何一个策略，
都会有一种k的情况（最坏情况），会使得需要用最多的尝试次数才能将临界层找到，
这个最多的尝试次数称为该策略的尝试次数上界

4. 策略之间的优劣：尝试次数上界越小越优
---

最终的问题：给定2个一模一样的玻璃球，在保证找到临界层的情况下，给出最优策略。

'''

import math
from matplotlib import pyplot

# # def cal_combination(i,n):
# #     return math.factorial(n)//(math.factorial(2)*math.factorial(n-2))

# # def cal_val(n):
# #     temp = 
# #     for i in range(2,n+1):
# #         # temp += cal_combination(i,n)/(2**i)
# #         temp += 1/(2**i)
# #     # temp = temp/(0.25*n)
# #     return temp
# pro = []
# for i in range(2,100):
#     pro.append(1/(2**i))
# print(pro)
# pyplot.plot(pro)
# pyplot.show()


import random
from collections import Counter
ans = []
for _ in range(1000):
    times = 0
    count = 0
    while not times == 2:
        count+=1
        temp = random.randint(0,1)
        if temp == 0:
            times = 0
        else:
            times+=1
    ans.append(count)
temp = 0
for item in ans:
    temp+=item
print(temp/len(ans))

