#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (39.38%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 53K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
        if prices==[]:
            return 0
        length=len(prices)
        #结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp=[ [[0,0,0],[0,0,0] ] for i in range(0,length) ]
        #第一天休息
        dp[0][0][0]=0
        #第一天买入
        dp[0][1][0]=-prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        #第一天不可能已经卖出
        dp[0][1][1]=float('-inf')
        dp[0][1][2]=float('-inf')
        for i in range(1,length):
            #未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0]=0
            #未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
            #未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
            #持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
            #持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
            #持股，卖出过2次，不可能
            dp[i][1][2]=float('-inf')
        return max(dp[length-1][0][1],dp[length-1][0][2],0)

        # ---------你个菜🐔
        # # 求出所有最大子列，然后取和最大的两个子列
        # own = [prices[i]-prices[i-1] for i in range(1,len(prices))]
        # # 子列和列表
        # ans_list = []
        # own2 = []
        # # 双指针连续正项负项合并
        # pt1 = 0
        # pt2 = 1
        # add_time = 0
        # while pt2 < len(own):
        #     if own[pt2] < 0 and own[pt1] < 0:
        #         own[pt1] += own[pt2]
        #         # pt1+=1
        #         pt2+=1
        #         add_time+=1
        #     elif own[pt2] >= 0 and own[pt1] >= 0:
        #         own[pt1] += own[pt2]
        #         pt2+=1
        #         add_time+=1
        #     else:
        #         pt1+=1
        #         own[pt1] = own[pt2]
        #         pt2+=1
        # # 去尾
        # own = own[:len(own)-add_time]
        # # 统计
        # from collections import Counter 
        # import numpy as np
        # while True:
        #     flag = 0
        #     own_np = np.array(own)
        #     counter = Counter(own_np>0)
        #     # 如果大于0的《=2个，直接加和返回
        #     if counter[True] <= 2:
        #         return sum(own_np[own_np>0])
        #     else:
        #         pass
        #     # 所有大于0的位置索引
        #     loc = np.where((own_np>0)==True)[0]
        #     # 每两个大于0检查是否可以合并
        #     i = 0
        #     while i < (loc.shape[0]-1):
        #         for t in range(i+1,loc.shape[0]):
        #             sum_val = 0
        #             max_ele = 0
        #             for j in range(loc[i],loc[t]+1):
        #                 sum_val += own[j]
        #                 max_ele = max(max_ele,own[j])
        #             if sum_val > max_ele:
        #                 # 可以合并
        #                 own[loc[i]] = sum_val
        #                 own = own[:loc[i]+1]+own[loc[t]+1:]
        #                 flag = 1
        #                 break
        #         if flag == 1:
        #             break
        #         i+=1
        #     pass
        #     if flag == 0:
        #         break
        #     # own
        # # 取出最大两个索引然后加和
        # own.sort()
        # own = own[::-1]
        # return own[0] + own[1] if own[1] > 0 else own[0]


        #-----------------------
        # 沿用前面的思路
        # get_sum = 0
        # max_own = 0
        # for i in range(len(own)):
        #     # 遍历挣钱列表，求出两个最大子列，求单个子列方法和前面是一样的
        #     if get_sum >= 0:
        #         # 只要你是正的就要一直加
        #         get_sum+=own[i]
        #     # 如果加完后小于0了，那么就重置
        #     if get_sum < 0:
        #         get_sum = 0
        #         ans_list.append(max_own)
        #         max_own = 0
        #     max_own = max(max_own,get_sum)
        # ans_list.append(max(max_own,0))
        # return sum(ans_list)


# @lc code=end
s = [6,5,4,8,6,8,7,8,9,4,5]
solu = Solution()
print(solu.maxProfit(s))