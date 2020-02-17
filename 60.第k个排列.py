#
# @lc app=leetcode.cn id=60 lang=python
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (46.99%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 45K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
# 
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

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 从第一个到第K个迭代的做法，超时，因为这种方法包含了含有重复元素的情况
        # nums = [i for i in range(1,n+1)]
        # for i in range(k-1):    
        #     self.nextPermutation(nums)
        # ans = ''
        # for i in range(n):
        #     ans+= str(nums[i]) 
        # return ans

        # 题目中是明确说明了没有重复元素
        k = k-1
        def get_current_num(candidate,n,k):
            # candidate为有序数组
            return k//math.factorial(n-1)
        # 生成候选数字
        nums = [i for i in range(1,n+1)]
        print(nums)
        import math
        ans = ''
        while not n == 0:
            index = get_current_num(nums,n,k)
            ans += str(nums[index])
            nums.pop(index)
            k = k%math.factorial(n-1)
            n-=1
        return ans




        
# @lc code=end
n = 3
k = 2

solu = Solution()
print(solu.getPermutation(n,k))

