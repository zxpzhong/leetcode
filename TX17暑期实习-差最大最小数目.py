import sys 
n = list(map(int,sys.stdin.readline().strip().split()))[0]
nums = list(map(int,sys.stdin.readline().strip().split()))
# 排序
nums.sort()

min_ = sys.maxsize
min_count = 0
max_ = 0
max_count = 0



# 这个方法还是有问题，因为里面有重复数字！！！！！老弟
dp = [0 for _ in range(len(nums)-1)]
for i in range(len(nums)-1):
    dp[i] = nums[i+1]-nums[i]

# 遍历dp获得最小值数目
for i in range(len(dp))):
    if dp[i] < min_:
        min_ = dp[i]
        min_count = 0
    else:
        min_count+=1
# 最大值直接首尾相减
# 头相等数目
head = 0
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        head += 1
# 头相等数目
tail = 0
for i in range(len(nums)-1):
    if nums[len(nums)-1-i] == nums[len(nums)-2-i]:
        tail += 1
# 头尾相等数目获取到
if tail == head:
    max_count = 
else:
    max_count = tail*head


# 这个方法超时了
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         sub = abs(nums[i]-nums[j])
#         # 判断当前sub和最小值最大值差的关系
#         if sub < min_:
#             min_ = sub
#             min_count = 0
#         elif sub > max_:
#             max_ = sub
#             max_count = 0
#         if sub == min_:
#             min_count+=1
#         if sub == max_:
#             max_count+=1
# print(min_count,max_count)