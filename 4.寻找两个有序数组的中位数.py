#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.00%)
# Likes:    2056
# Dislikes: 0
# Total Accepted:    134.2K
# Total Submissions: 366.6K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sum_list = nums1 + nums2
        sum_list.sort()
        all_len = len(sum_list)
        # 奇数
        if all_len % 2 == 1:
            return sum_list[int((all_len-1)/2)]
        else:
            print(sum_list[int(all_len/2)],sum_list[int(all_len/2)-1])
            return (sum_list[int(all_len/2)] + sum_list[int(all_len/2)-1])/2.0
        
      
# @lc code=end
solu = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(solu.findMedianSortedArrays(nums1,nums2))

