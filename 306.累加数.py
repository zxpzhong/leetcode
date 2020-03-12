#
# @lc app=leetcode.cn id=306 lang=python
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (31.61%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 13.5K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#

# @lc code=start
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        # if len(num)<3:
        #     return False
        # if num[0] == '0' and not num[1] == '0':
        #     return False
    
        # dp = [False for _ in range(len(num)+1)]
        # dp[0] = True
        # # s = '19991000'
        # # print(self.isOK(s))
        # for i in range(len(num)):
        #     # if dp[i] == True:
        #         for j in range(i+3,len(num)+1):
        #             temp = num[i:j]
        #             if self.isOK(temp):
        #                 dp[j] = True
        #                 if j == len(num):
        #                     return True
        # return dp[-1]

        # 递归
        if len(num)<3:
            return False
        # 找到首字符
        for i in range(3,len(num)+1):
            temp = self.isOK(num[:i])
            if not temp:
                continue
            base = 0
            l1,l2,l3 = temp
            if l1+l2+l3 == len(num):
                return True
            # 根据这个一直向后分割
            while base+l2+l3 < len(num)-1:
                sum_val = str(int(num[base+l1:base+l1+l2])+int(num[base+l1+l2:base+l1+l2+l3]))
                if num[base+l1+l2+l3:base+l1+l2+l3+len(sum_val)] == sum_val:
                    if base+l1+l2+l3+len(sum_val) == len(num):
                        return True
                    l1,l2,l3 = l2,l3,len(sum_val)
                    base+=l1
                else:
                    break
        return False

                    

    # 判断一个子串是否满足单次
    def isOK(self, instr):

        # 最后一个数的最短长度：len(instr)//3 + (1 if len(instr)%3 else 0)
        # 第二个数的最短长度len(instr)//3，最大长度len(instr)//3 + (1 if len(instr)%3==2 else 0)
        # 第一个数的最短长度1，最大长度len(instr)//3
        length1 = 1
        length2_min = 1 # maxlen(instr)//3 + (1 if len(instr)%3==2 else 0)
        length2_max = len(instr)//2
        length3_min = len(instr)//3 + (1 if len(instr)%3 else 0)
        length3_max = (len(instr)//2+len(instr)%2)
        for i in range(length3_min,length3_max+1):
            for j in range(length2_min,length2_max+1):
                if j>i:
                    break
                length1 = len(instr)-i-j
                if length1>i or j > i:
                    break
                if length1 < 0:
                    break
                try:
                    if int(instr[:length1]) == 0 or int(instr[length1:length1+j]) == 0 or int(instr[length1+j:]) == 0:
                        pass
                    if len(instr[:length1]) >1 and instr[:length1][0] == '0':
                        continue
                    if len(instr[length1:length1+j]) >1 and instr[length1:length1+j][0] == '0':
                        continue
                    if len(instr[length1+j:]) >1 and instr[length1+j:][0] == '0':
                        continue
                except:
                    break
                if (int(instr[:length1])+int(instr[length1:length1+j]) == int(instr[length1+j:])):
                    # 不相等
                    return (length1,j,len(instr)-length1-j)
                else:
                    continue
        return False
        # --------傻子做题！！！！！题目都不看清么？？


# @lc code=end
# "0235813"    false
# 011235     true
s = "211738"
solu = Solution()
print(solu.isAdditiveNumber(s))