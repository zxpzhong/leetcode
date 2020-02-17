#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (35.42%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 39.3K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)

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
intervals = [[1,3],[6,9]]
newInterval = [2,5]
solu = Solution()
print(solu.insert(intervals, newInterval))

