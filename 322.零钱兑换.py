#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (35.70%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    42K
# Total Submissions: 111.6K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 哈哈哪有这么简单，想P吃
        # 排序逆序
        # coins.sort()
        # coins = coins[::-1]
        # ans = 0
        # for i in range(len(coins)):
        #     temp = amount//coins[i] 
        #     ans+=temp
        #     amount = amount-temp*coins[i]
        # if amount == 0:
        #     return ans
        # else:
        #     return -1
        # if amount == 0:
        #     return 0
        # self.coins = coins
        # self.min_coin = min(coins)
        # return self.addone([amount],0)

    # # 广度优先遍历，超时
    # def addone(self,amount,count):
    #     amounts = []
    #     for item in amount:
    #         for coin in self.coins:
    #             if item-coin == 0:
    #                 return count+1
    #             elif item-coin >= self.min_coin:
    #                 amounts.append(item-coin)
    #     if len(amounts) == 0:
    #         return -1
    #     return self.addone(amounts,count+1)

        # DP方法
        # dp[n] = for i in coints : min(dp[m-coin[i]]) +1
        
        if amount == 0:
            return 0
        dp = [-1]*(amount+1)
        coins2 = []
        for i in range(len(coins)):
            if coins[i] <= amount:
                coins2.append(coins[i])
        if len(coins2) == 0:
            return -1
        # 赋初值
        for i in range(len(coins2)):
            dp[coins2[i]] = 1
        mincoin = min(coins2)
        for i in range(mincoin,amount+1):
            temp = 2147483647
            if not dp[i] == 1:
                # 这个地方啊兄弟，怎么会蠢到遍历所有的值呢，应该是遍历硬币！！
                # for j in range(mincoin,i):
                for j in range(len(coins2)):
                    if coins2[j] > i:
                        continue
                    # 从最小面值到i
                    if not (dp[coins2[j]]== -1 or dp[i-coins2[j]] == -1):
                        temp = min(temp,dp[coins2[j]]+dp[i-coins2[j]])
                dp[i] = temp
        return dp[-1] if not dp[-1] == 2147483647 else -1
        
        # 网上的记忆回溯法
        # memo={0:0}
        # def helper(n):   
        #     if(n in memo):
        #         return memo[n]
        #     res=float("inf")
        #     for coin in coins:
        #         if(n>=coin):
        #             res=min(res,helper(n-coin)+1)
        #     memo[n]=res
        #     return res
        # temp = helper(amount)
        # return  temp if(temp!=float("inf")) else -1


        # 网上dp
        # dp=[float("inf")]*(amount+1)
        # dp[0]=0
        # for i in range(1,amount+1):
        #     for coin in coins:
        #         if(i>=coin):
        #             dp[i]=min(dp[i],dp[i-coin]+1)
        # return dp[-1] if(dp[-1]!=float("inf")) else -1

# @lc code=end

coins = [102,220,186,465,336,107,387,418]
amount = 495
solu = Solution()
print(solu.coinChange(coins,amount))
