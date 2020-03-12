import sys 
texts = []
# for line in sys.stdin:
#     texts.append(line.split())
# K = int(texts[0])
# A = int(texts[1][0])
# X = int(texts[1][1])
# B = int(texts[1][2])
# Y = int(texts[1][3])

K = 205
A = 1
X = 92
B = 4
Y = 92

# 抽取任意多个数使得和为K的不重复集合的数量
# 排列组合问题
# 全部使用A/B，不大于K情况下的最大数量
max_A = min(X,K//A)
max_B = min(Y,K//B)
import math
ans = 0
for i in range(max_A+1):
    # 选用i个A
    if not (K-i*A) % B == 0:
        # 无法通过选用B组成长度恰好为K，跳过
        continue
    B_val = (K-i*A) // B
    if B_val > max_B:
        # 需要B的数目大于B的最大值，跳过
        continue
    # 计算组合数目,X中选i个A，Y中选B_val个B，组合数目为：C X i  * C Y B_val
    count1 = (math.factorial(X)/(math.factorial(i))/(math.factorial(X-i)))
    count2 = (math.factorial(Y)/(math.factorial(B_val))/(math.factorial(Y-B_val)))
    ans+=count1*count2
print(int(ans)%1000000007)