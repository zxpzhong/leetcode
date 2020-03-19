#
# @lc app=leetcode.cn id=295 lang=python
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (39.45%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 27.1K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#

# @lc code=start
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 找到i位置可以变为二分查找
        self.length += 1
        for i in range(len(self.heap)):
            # 遍历堆大小，找到位置，然后插入
            if self.heap[i] > num:
                # 递增排列
                self.heap.insert(i,num)
                # self.heap = self.heap[:i]+[num]+self.heap[i:]
                return
        self.heap.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length % 2 == 0:
            # 长度为偶数
            return (self.heap[(self.length-1)//2]+self.heap[self.length//2])/2.0
        else:
            return self.heap[self.length//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

solu = MedianFinder()
solu.addNum(-1)
print(solu.findMedian())
solu.addNum(-2)
print(solu.findMedian())
solu.addNum(-3)
print(solu.findMedian())
solu.addNum(-4)
print(solu.findMedian())
solu.addNum(-5)
print(solu.findMedian())