#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.93%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    51.3K
# Total Submissions: 139.7K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        # 排序
        nums_bak = nums
        nums_bak.sort()
        print('nums_bak:',nums_bak)
        nums_bak2 = []
        # 去重
        equal_counter = 0
        for i in range(len(nums_bak)-1):
            nums_bak2.append(nums_bak[i])
            if nums_bak[i] == nums_bak[i+1]:
                equal_counter +=1
                if equal_counter >=5:
                    nums_bak2.pop()
            else:
                equal_counter = 0
        print('nums_bak2:',nums_bak2)
        print([i+1])
        nums_bak2.append(nums_bak[i+1])
        print(nums_bak2)
        nums_bak = nums_bak2

        # 遍历前两个，第三、四个元素用左右指针找到
        ans = []
        for i in range(len(nums_bak)-3):
            for j in range(i+1,len(nums_bak)-2):
                if nums_bak[i] > target and nums_bak[i] > 0:
                    break
                # if(i>0 and nums_bak[i]==nums_bak[i-1]):
                    # continue
                L = j+1
                R = len(nums_bak)-1
                while R > L:
                    if nums_bak[i] + nums_bak[j] + nums_bak[L] + nums_bak[R] > target:
                        # 大于0，R左移
                        R -= 1
                    elif nums_bak[i] + nums_bak[j] + nums_bak[L] + nums_bak[R] < target:
                        L += 1
                    else:
                        ans.append([nums_bak[i],nums_bak[j],nums_bak[L],nums_bak[R]])
                        L+=1
                        R-=1
        print('ans:',ans)
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
nums = [-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5]
target = 28
solu = Solution()
print(solu.fourSum(nums,target))

