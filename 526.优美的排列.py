#
# @lc app=leetcode.cn id=526 lang=python
#
# [526] 优美的排列
#
# https://leetcode-cn.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (55.56%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 6.6K
# Testcase Example:  '2'
#
# 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N)
# 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
# 
# 
# 第 i 位的数字能被 i 整除
# i 能被第 i 位上的数字整除
# 
# 
# 现在给定一个整数 N，请问可以构造多少个优美的排列？
# 
# 示例1:
# 
# 
# 输入: 2
# 输出: 2
# 解释: 
# 
# 第 1 个优美的排列是 [1, 2]:
# ⁠ 第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
# ⁠ 第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
# 
# 第 2 个优美的排列是 [2, 1]:
# ⁠ 第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
# ⁠ 第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
# 
# 
# 说明:
# 
# 
# N 是一个正整数，并且不会超过15。
# 
# 
#

# @lc code=start
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        nums = [i+1 for i in range(N)]
        self.ans = 0
        # 向nums中逐一填入数字
        self.addone(1,nums)
        return self.ans

    def addone(self,i,candi):
        if len(candi) == 0:
            self.ans+=1
        for j in range(len(candi)):
            if candi[j]%i == 0 or i%candi[j] == 0:
                # 如果满足条件
                self.addone(i+1,candi[:j]+candi[j+1:])


# @lc code=end

solu = Solution()
print(solu.countArrangement(2))