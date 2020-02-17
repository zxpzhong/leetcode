#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (18.21%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    101.7K
# Total Submissions: 538K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 
# 
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 
# 说明：
# 
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX
# (2^31 − 1) 或 INT_MIN (−2^31) 。
# 
# 示例 1:
# 
# 输入: "42"
# 输出: 42
# 
# 
# 示例 2:
# 
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 
# 
# 示例 3:
# 
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 
# 
# 示例 4:
# 
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
# 
# 示例 5:
# 
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
# 因此返回 INT_MIN (−2^31) 。
# 
# 
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        # 正则一句话答案
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)

        # max_ans = 2147483648-1
        # min_ans = -2147483648
        # if len(str) == 0 :
        #     return 0
        # first_flag = 0
        # extra_str = str
        # # 字符预处理，空格分割后，找到第一个非空字符
        # strlist = extra_str.split(' ')
        # print('strlist:',strlist)
        # for i in range(len(strlist)):
        #     if strlist[i] == '':
        #         pass
        #     else:
        #         break
        # extra_str = strlist[i]
        # print('----',extra_str)
        # extra_str = extra_str + ' '
        # for i in range(len(extra_str)):
        #     # 负号只能出现在第一个位置
        #     if (extra_str[i] == '-' or extra_str[i] == '+')and first_flag == 0:
        #         # i = i+1
        #         first_flag = 1
        #         pass
        #     elif extra_str[i] == ' ' and first_flag == 0:
        #         # i = i+1
        #         pass
        #     elif  (extra_str[i] >='0' and extra_str[i] <= '9'):
        #         # print(extra_str[i])
        #         # i = i+1
        #         first_flag = 1
        #         pass
        #     else:
        #         break
        # # extra_str.strip()
        # # print(i)
        # if i == 0:
        #     return 0
        # if i == 1 and (extra_str[0] == '-' or extra_str[0] == '+' or extra_str[0] == ' '):
        #     return 0
        # # for j in range(i):
        # print(extra_str[:i])
        # return min(max(min_ans,int(extra_str[:i])),max_ans)



# @lc code=end
solu = Solution()
print(solu.myAtoi('42'))
