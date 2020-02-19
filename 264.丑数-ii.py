#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (47.44%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 33.8K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n=n+1
        ans = [1]*n
        pt2 = 0
        pt3 = 0
        pt5 = 0
        for i in range(1,n):
            temp = [ans[pt2]*2,ans[pt3]*3,ans[pt5]*5]
            min_val = min(temp)
            ans[i] = min_val
            # index = temp.index(min(temp))
            if temp[0] == min_val:
                pt2+=1
            if temp[1] == min_val:
                pt3+=1
            if temp[2] == min_val:
                pt5+=1
        return ans[-1]

        
# @lc code=end

solu = Solution()
print(solu.nthUglyNumber(10))