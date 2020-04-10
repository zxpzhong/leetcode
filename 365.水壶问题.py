#
# @lc app=leetcode.cn id=365 lang=python
#
# [365] 水壶问题
#
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (28.29%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 62.4K
# Testcase Example:  '3\n5\n4'
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
# 
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
# 
# 你允许：
# 
# 
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 
# 
# 示例 1: (From the famous "Die Hard" example)
# 
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 
# 
# 示例 2:
# 
# 输入: x = 2, y = 6, z = 5
# 输出: False
# 
# 
#

# @lc code=start
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x+y<z:
            return False
        while y > 0:
            temp = x
            x = y
            y = temp%y
        # x为最大公约数
        if x == 0:
            return False
        if z%x == 0:
            return True
        return False

# @lc code=end

solu = Solution()
print(solu.canMeasureWater(1,1,12))