#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (54.33%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 62.5K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        
        self.backtrack([], nums, check)
        return self.res
        
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0


        # if len(nums) == 0:
        #     return []
        # if len(nums) == 1:
        #     return [nums]
        # nums.sort()
        # from copy import deepcopy
        # result = []
        # def add_one(current,left):
        #     # 当前字符串list从剩余的取出一个
        #     length = len(left)
        #     if length == 0:
        #         if not current in result:
        #             result.append(current)
        #     for i in range(length):
        #         left_bak = deepcopy(left)
        #         temp = current+[left_bak[i]]
        #         left_bak.pop(i)
        #         add_one(temp,left_bak)
        # add_one([],nums)

        # 弟弟行为，上面去重他不香么？
        # # for i in range(len(result)):
        # #     result[i].sort()
        # result.sort()
        # # 快慢指针去重
        # slow_pt = 0
        # fast_pt = 0
        # pre_value = 0
        # while slow_pt < len(result) and fast_pt < len(result):
        #     if pre_value == result[fast_pt]:
        #         # 相等，则快指针移动
        #         fast_pt+=1
        #     else:
        #         # 不等，则慢指针和快指针都移动
        #         result[slow_pt] = result[fast_pt]
        #         pre_value = result[slow_pt]
        #         slow_pt +=1
        #         fast_pt+=1
        #         if not (slow_pt < len(result) and fast_pt < len(result)):
        #             slow_pt = slow_pt+1
        #             break
                
        # result = result[:slow_pt]
        # return result
        
# @lc code=end
solu = Solution()
print(solu.permuteUnique([1,1]))

