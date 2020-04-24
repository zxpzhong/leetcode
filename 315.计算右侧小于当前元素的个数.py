#
# @lc app=leetcode.cn id=315 lang=python
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (37.69%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 37.6K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 示例:
# 
# 输入: [5,2,6,1]
# 输出: [2,1,1,0] 
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 
# 
#

# @lc code=start
import heapq
import numpy
import numpy as np
# 构建树状数组
def lowbit(x):
    return x&(-x)

from operator import itemgetter
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def add(p,v):
            while p <= N:
                Tree[p-1] += v
                p += lowbit(p)

        def sum_(p):
            ans =0
            while p>0:
                ans += Tree[p-1]
                p -= lowbit(p)
            return ans
        N = len(nums)
        # 排序索引
        nums = numpy.array(nums)
        # 
        idx = [index for index, value in sorted(enumerate(nums), key=itemgetter(1))]
        # print(idx_)
        # idx = numpy.argsort(nums,kind='mergesort')
        idx_ = [0]*N
        for i in range(N):
            idx_[idx[i]] = i
        print(idx)
        ans = [0]*N
        Tree = [0]*N
        # 从后先前遍历数组
        for i in range(N-1,-1,-1):
            loc = idx_[i]
            # print(loc)
            ans[i] = sum_(loc)
            add(loc+1,1)
        return ans

# @lc code=end
# nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
nums = [5,2,6,1]
solu = Solution()
print(solu.countSmaller(nums))