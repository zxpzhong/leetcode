#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (58.07%)
# Likes:    1060
# Dislikes: 0
# Total Accepted:    127.5K
# Total Submissions: 210.2K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例:
# 
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# 
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 这是最简单的方法，但是超时了
        # max_in = 0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         val = (j-i)*min(height[i],height[j])
        #         if val > max_in:
        #             max_in = val
        # return max_in

        # 如何降低时间复杂度，变为numpy计算矩阵乘积，还是超时
        # import numpy as np
        # max_in = 0
        # min_height = np.zeros([len(height),len(height)])
        # axissub = np.zeros([len(height),len(height)])
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         min_height[i,j] = min(height[i],height[j])
        #         axissub[i,j] = j-i
        # c = np.multiply(min_height,axissub)

        # 如何降低时间复杂度，双指针
        i = 0
        j = len(height)-1
        max_area = 0
        while not j == i:
            max_area = max(max_area,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i = i + 1
            else:
                j = j - 1
        return max_area


# @lc code=end

height = [1,8,6,2,5,4,8,3,7]
solu = Solution()
print(solu.maxArea(height))