#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (38.57%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    49.3K
# Total Submissions: 123.2K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 对于左区间排序后的列表

        def merge_one(intervals):
            length = len(intervals)
            i = 0
            # 这里注意，每次调用while  if，表达式两边的式子都会重新计算一遍，len(intervals)会随着intervals的长度改变而改变
            while i < len(intervals)-1:
                if intervals[i][1] >= intervals[i+1][0]:
                    # 存在重叠区间
                    if intervals[i+1][1] >= intervals[i][1]:
                        # 取左右两端
                        intervals[i][1] = intervals[i+1][1]
                    else:
                        # 取第一节区间
                        # intervals[i+1][0] = intervals[i][0]
                        pass
                    intervals.pop(i+1)
                else:
                    i+=1
                    # return intervals
            return intervals
        # 按首排序
        import numpy
        import copy
        index = numpy.argsort([intervals[i][0] for i in range(len(intervals))])
        # 获取区间排序index            # 按照index对所有区间重排序
        intervals2 = []
        for i in range(len(intervals)):
            intervals2.append(intervals[index[i]])
        intervals = intervals2
        while True:
            pre = copy.deepcopy(intervals)
            if len(intervals) < 2:
                return intervals
            intervals = merge_one(intervals)
            if pre == intervals:
                return intervals

# @lc code=end
intervals = [[1,4],[0,2],[3,5]]
solu = Solution()
print(solu.merge(intervals))

