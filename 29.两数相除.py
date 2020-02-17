#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (18.61%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    32.1K
# Total Submissions: 168.4K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 
# 说明:
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        # 两者同号
        if (dividend > 0 and divisor >0) or (dividend < 0 and divisor < 0):
            flag = 1
        else:
            flag = -1
        
        max_ans = 2**31-1
        min_ans = -2**31
        # 取绝对值
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ansrange = divisor
        range_flag = 0
        # 首先确定范围
        while True:
            if dividend < ansrange:
                break
            ansrange=ansrange<<1
            range_flag +=flag

        left = ansrange
        times = range_flag
        result = 0
        # 像上面一样，这里也不能一个一个减掉
        while not times == 0:
            times -= flag
            left = left>>1
            if left <= dividend:
                result += flag << abs(times)
                dividend-=left
            
        if result > max_ans or result < min_ans:
            return max_ans
        return result


     
# @lc code=end

dividend = 28
divisor = 7
solu = Solution()
print(solu.divide(dividend,divisor))