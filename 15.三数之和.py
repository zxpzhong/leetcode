#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.05%)
# Likes:    1724
# Dislikes: 0
# Total Accepted:    145.9K
# Total Submissions: 579.7K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import copy
        # # 简单版本
        # nums_bak = nums
        # nums_bak.sort()
        # nums_bak2 = []
        # ans = []
        # if len(nums) < 3:
        #     return []

        # # 连续三个去重，最多只能留下两个重复,0除外，可以保留三个
        # # equal_counter = 0
        # # for i in range(len(nums_bak)-1):
        # #     nums_bak2.append(nums_bak[i])
        # #     if nums_bak[i] == nums_bak[i+1]:
        # #         equal_counter +=1
        # #         if equal_counter >=2 and not nums_bak[i] == 0:
        # #             nums_bak2.pop()
        # #     else:
        # #         equal_counter = 0
        # # nums_bak2.append(nums_bak[i+1])
        # # print(nums_bak2)

        # nums_bak2 = nums_bak
        # if len(nums_bak2) < 3 and nums_bak2[0] == 0:
        #     return [[0,0,0]]

        # # i_first = 0
        # j_first = 0
        # t_first = 0
        # for i in range(len(nums_bak2)):
        #     nums_bak = copy.deepcopy(nums_bak2)
        #     nums_bak.pop(i)
        #     j_first = 0
        #     if i > 0 and nums_bak2[i] == nums_bak2[i-1]:
        #         # i = i + 1
        #         continue
            
        #     for j in range(i+1,len(nums_bak2)):
        #         nums_bak3 = copy.deepcopy(nums_bak)
        #         nums_bak3.pop(j-1)
        #         t_first = 0
        #         if j > 0 and nums_bak2[j] == nums_bak2[j-1]:
        #             if j_first == 1:
        #                 # j = j + 1
        #                 continue
        #             else:
        #                 j_first = 1
                    
        #         # for t in range(j+1,len(nums_bak2)):
        #         #     if t > 0 and nums_bak2[t] == nums_bak2[t-1]:
        #         #         if t_first == 1:
        #         #             # j = j + 1
        #         #             continue
        #         #         else:
        #         #             t_first = 1
        #         if -(nums_bak2[i] + nums_bak2[j]) in nums_bak3:
        #             # if nums_bak2
        #             # if nums_bak2[i] + nums_bak2[j] + nums_bak2[t] == 0:
        #             ans.append([nums_bak2[i] ,nums_bak2[j] ,-(nums_bak2[i] + nums_bak2[j])])
        # print(len(ans))
        # if len(ans) < 2:
        #     return ans
        # # 结果去重
        # ans2 = []
        # for i in range(len(ans)):
        #     ans[i].sort()
        # ans.sort()
        # for i in range(len(ans)-1):
        #     if not ans[i] == ans[i+1]:
        #         ans2.append(ans[i])
        # ans2.append(ans[i+1])
        # return ans2

        # 参考网上解法，确实比自己的想法优化了很多

        if len(nums) < 3:
            return []

        nums_bak = nums
        nums_bak.sort()
        import copy
        nums_bak2 = []
        # 连续三个去重，最多只能留下两个重复,0除外，可以保留三个
        equal_counter = 0
        for i in range(len(nums_bak)-1):
            nums_bak2.append(nums_bak[i])
            if nums_bak[i] == nums_bak[i+1]:
                equal_counter +=1
                if equal_counter >=2 and not nums_bak[i] == 0:
                    nums_bak2.pop()
                elif equal_counter >=3:
                    nums_bak2.pop()
            else:
                equal_counter = 0
        nums_bak2.append(nums_bak[i+1])
        print(nums_bak2)
        nums_bak = nums_bak2

        ans = []
        for i in range(len(nums_bak)-2):
            if nums_bak[i] > 0:
                break
            if(i>0 and nums_bak[i]==nums_bak[i-1]):
                continue
            L = i+1
            R = len(nums_bak)-1
            while R > L:
                if nums_bak[i] + nums_bak[L] + nums_bak[R] > 0:
                    # 大于0，R左移
                    R -= 1
                elif nums_bak[i] + nums_bak[L] + nums_bak[R] < 0:
                    L += 1
                else:
                    ans.append([nums_bak[i],nums_bak[L],nums_bak[R]])
                    L+=1
                    R-=1
        
        print(ans)
        if len(ans) < 2:
            return ans
        # 结果去重
        ans2 = []
        for i in range(len(ans)):
            ans[i].sort()
        ans.sort()
        for i in range(len(ans)-1):
            if not ans[i] == ans[i+1]:
                ans2.append(ans[i])
        ans2.append(ans[i+1])
        return ans2



# @lc code=end

solu = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
# nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
# nums = [0,1,1]
lst = solu.threeSum(nums)
print(lst)