# '''题目
# 2
# 3 1
# '''


# fac = [[]for _ in range(len(nums))]
# max_len = 0
# # 计算所有数的公约数
# for i in range(len(nums)):
#     temp = 2
#     fac[i].append(1)
#     for t in range(1,nums[i]):
#         if nums[i]%t == 0:
#             fac[i].append(t)
#             temp+=1
#     fac[i].append(nums[i])
#     max_len = max(max_len,temp)

import sys
# 获取输入
n = list(map(int,sys.stdin.readline().strip().split()))[0]
nums = list(map(int,sys.stdin.readline().strip().split()))

import functools

class Get_Sub(object):
    def subset(self, nums):
        ans = 0
        # candi = [i for i in range(1,n+1)]
        self.candi = nums
        for k in range(1,len(nums)+1):
            ans+=self.add_one(0,k,1)
        return ans

    @functools.lru_cache()
    def add_one(self,pt,k,len_cur):
        # 退出条件
        ans = 0
        if len_cur == k+1:
            return 1
        for i in range(pt,len(self.candi)):
            if self.candi[i]%len_cur == 0:
                # 如果要加入，必须满足条件：len_cur在约数内
                ans+=self.add_one(i+1,k,len_cur+1)
        return ans

# 获取所有序列
get_sub = Get_Sub()
ans = get_sub.subset(nums)
print(ans%998244353)
    


# ans = len(nums)*2
# for i in range(2,max_len-1):
#     # 长度为i:2~max_len-2
#     for j in range


