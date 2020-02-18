#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (50.87%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    127.2K
# Total Submissions: 243K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        # 最大子列！！！
        pre = prices[0]
        max_in = 0
        real_ans = 0
        for i in range(1,len(prices)):
            day = prices[i]-pre
            pre = prices[i]
            # 这个是精髓，子列要一直叠加，知道累价值小于0时重置
            if max_in > 0:
                max_in +=day
            else:
                max_in = day
            real_ans = max(max_in,real_ans)
        return real_ans

# @lc code=end
s = [7,1,5,3,6,4]
# s = [1,2,11,4,7]
solu = Solution()
print(solu.maxProfit(s))
