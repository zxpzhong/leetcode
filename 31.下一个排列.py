#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.06%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 117.8K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def partition(arr,low,high): 
            i = ( low-1 )         # 最小元素索引
            pivot = arr[high]     
        
            for j in range(low , high): 
        
                # 当前元素小于或等于 pivot 
                if   arr[j] <= pivot: 
                
                    i = i+1 
                    arr[i],arr[j] = arr[j],arr[i] 
        
            arr[i+1],arr[high] = arr[high],arr[i+1] 
            return ( i+1 ) 
  
 
        # arr[] --> 排序数组
        # low  --> 起始索引
        # high  --> 结束索引
        
        # 快速排序函数
        def quickSort(arr,low,high): 
            if low < high: 
        
                pi = partition(arr,low,high) 
        
                quickSort(arr, low, pi-1) 
                quickSort(arr, pi+1, high) 

        length = len(nums)
        if length == 1:
            return
        last = 0
        for i in reversed(range(length-1)):
            # 从后往前逆序查找，对于每一个元素，检查其后所有元素的最小值
            min_number = nums[i+1]
            min_index = i+1
            for j in range(i+1,length):
                if nums[j] < min_number and nums[j] > nums[i]:
                    min_number = nums[j]
                    min_index = j
            # 如果后面序列的最小值大于当前值，说明可以替换
            if min_number > nums[i]:
                # 记录当前替换位置
                last = i
                temp = nums[min_index]
                nums[min_index] = nums[last]
                nums[last] = temp
                # 替换后，替换位置后的序列所有元素重新排序
                quickSort(nums,last+1,length-1)
                return
        quickSort(nums,0,length-1)
            
                
        
# @lc code=end
nums = [3,2,1]

solu = Solution()
solu.nextPermutation(nums)
print(nums)

