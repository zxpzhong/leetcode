#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (45.41%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    104.7K
# Total Submissions: 225.5K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:]
            return 
        if n == 0:
            return
        # 每次插入一个，nums把自身所有的数全部都往后移动一格
        # 双指针
        pt1 = 0
        pt2 = 0
        # 掐头
        i = 0
        for _ in range(len(nums2)):
            if nums2[i] < nums1[0]:
                i+=1
            else:
                break
        # 从i开始插
        nums1[:] = nums2[:i]+nums1[0:len(nums1)-i]
        pt1 = i
        pt2 = i
        while pt2 < len(nums2):
            # 如果nums1已经到底了，直接把剩下的全部复制过来
            if pt1 >= m+pt2:
                nums1[pt1:] = nums2[pt2:]
                return
            # 如果小于，则继续往后，并且总是插在最后面，这样会剩下最后一个数，最后一个数单独处理
            if nums1[pt1] <= nums2[pt2] and nums1[pt1+1] > nums2[pt2]:
                # 集体右移pt1+1 -> pt1+2
                nums1[pt1+1:] = [nums2[pt2]]+nums1[pt1+1:]
                pt2+=1
            pt1+=1
        nums1[:] = nums1[:m+n]
        # 遍历结束后，还差nums[-1]最后一个



        
# @lc code=end
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
solu = Solution()
solu.merge(nums1,m,nums2,n)
print(nums1)
