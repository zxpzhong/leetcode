#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (71.97%)
# Likes:    510
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 98.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        result = []
        def add_one(current,left):
            # 当前字符串list从剩余的取出一个
            length = len(left)
            if length == 0:
                result.append(current)
            for i in range(length):
                left_bak = deepcopy(left)
                temp = current+[left_bak[i]]
                left_bak.pop(i)
                add_one(temp,left_bak)
        ans = add_one([],nums)
        return result

        
# @lc code=end
nums = [1,2,3]
solu = Solution()
print(solu.permute(nums))

