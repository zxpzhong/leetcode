#
# @lc app=leetcode.cn id=478 lang=python
#
# [478] 在圆内随机生成点
#
# https://leetcode-cn.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Medium (36.84%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 4.5K
# Testcase Example:  '["Solution", "randPoint", "randPoint", "randPoint"]\n[[1.0, 0.0, 0.0], [], [], []]'
#
# 给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。
# 
# 说明:
# 
# 
# 输入值和输出值都将是浮点数。
# 圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
# 圆周上的点也认为是在圆中。
# randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。
# 
# 
# 示例 1：
# 
# 
# 输入: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# 输出: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
# 
# 
# 示例 2：
# 
# 
# 输入: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# 输出: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# 
# 输入语法说明：
# 
# 输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有三个参数，圆的半径、圆心的 x 坐标、圆心的 y 坐标。randPoint
# 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。
# 
#

# @lc code=start
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    def randommy(self,r):
        from numpy import random
        return random.uniform(-r,r)
        
    def randPoint(self):
        
        import math
        """
        :rtype: List[float]
        """
        # r = self.randommy()*self.radius
        # theta = self.randommy()*2*math.pi
        # return [self.x_center+r*math.cos(theta),self.y_center+r*math.sin(theta)]
        x = self.radius
        y = self.radius
        while math.sqrt(x**2+y**2)>self.radius:
            x = self.randommy(self.radius)
            y = self.randommy(self.radius)
        return [x+self.x_center,y+self.y_center]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

solu = Solution(1,0,0)
print(solu.randPoint())