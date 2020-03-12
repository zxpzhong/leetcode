#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (66.90%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    58.5K
# Total Submissions: 85.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # # 二分法排序
        # def partition(arr,low,high):
        #     i = ( low-1 ) # 最小元素索引
        #     pivot = arr[high]
        #     for j in range(low , high):
        #         # 当前元素小于或等于 pivot
        #         if arr[j] <= pivot:
        #             i = i+1
        #             arr[i],arr[j] = arr[j],arr[i]
        #         arr[i+1],arr[high] = arr[high],arr[i+1]
        #     return ( i+1 )
        #     # arr[] --> 排序数组
        #     # low --> 起始索引
        #     # high --> 结束索引
        #     # 快速排序函数
        # def quickSort(arr,low,high):
        #     if low < high:
        #         pi = partition(arr,low,high)
        #         quickSort(arr, low, pi-1)
        #         quickSort(arr, pi+1, high)

        # # 有序列表标准二分法查找
        # def find_index(nums,target,start):
        #     length = len(nums)
        #     if length == 1 and not nums[0] == target:
        #         return -1
        #     if nums[length//2] == target:
        #         return length//2+start
        #     ans = -1
        #     if nums[length//2] > target:
        #         start +=0
        #         ans = find_index(nums[:length//2],target,start)
        #     else:
        #         start +=length//2
        #         ans = find_index(nums[length//2:],target,start)
        #     return ans
        
        # def iteradd(nums,target,added_number):
        #     length = len(nums)
        #     # 对added_number求和
        #     added_sum = sum(added_number)
        #     if added_sum > target:
        #         return []
        #     if length == 0:
        #         return []
        #     ans = []
        #     # 出口为target-one_number在nums中
        #     if target-added_sum in nums or target-added_sum == 0:
        #         added_number.append(target-added_sum)
        #         # ans.append(added_number_bak)
        #         ans.append(added_number)
        #     for i in range(length):
        #         added_number_bak = added_number
        #         if sum(added_number_bak) < target:
        #             added_number_bak.append(nums[i])
        #             iter_ans = iteradd(nums,target,added_number_bak)
        #             if not len(iter_ans) == 0:
        #                 ans.append(iter_ans)
        #     return ans
            

        # # 先排序
        # length = len(candidates)
        # # quickSort(candidates,0,length)

        # # 递归分解数（每一个数都去找是否可以分解为更小的数，包括分解后的数）
        # ans = []
        # for i in range(length):
        #     ans.append(iteradd(candidates,target,[candidates[i]]))
        # return ans 
        
        # 3月9日重做---------------------------------
        # 回溯法，思路要清晰，头脑要清晰，不要一股脑冲上去乱做
        min_val = min(candidates)
        max_val = min(candidates)
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
        candidates = candidates[:i+1]

        # 回溯
        self.candidates = candidates
        self.ans = []
        self.cut_one(target,[],candidates)
        return self.ans

    def cut_one(self,res,candi,candidates):
        for i,item in enumerate(candidates):
            if item == res:
                self.ans.append(candi+[item])
            elif item < res:
                self.cut_one(res-item,candi+[item],candidates[i:])
            else:
                return

# @lc code=end

candidates = [2,3,5]
target = 8

solu = Solution()
ans = solu.combinationSum(candidates,target)
print(ans)

