#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (45.00%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    88.9K
# Total Submissions: 191.8K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# 
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# string convert(string s, int numRows);
# 
# 示例 1:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 
# 
# 示例 2:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # # 所有字符长度
        all_len = len(s)
        if all_len <=1:
            return s
        if numRows <=1:
            return s
        # # 先产生新顺序的列表
        # new_list = [1]*(all_len+(all_len-numRows) % (2*numRows-2)+all_len*2+(2*numRows-2)*2)

        # new_str = []
        # i = 0
        # # 写入初始位置
        # while True:
        #     new_number = (2*numRows-2)*(i)
        #     # 检查字符长度
        #     # print(new_number)
        #     if new_number >=0 and new_number < len(new_list): 
        #         # 将新的顺序写入列表
        #         new_list[new_number] = 0
        #         # print(s[new_number])
        #         if new_number < all_len:
        #             new_str.append(s[new_number])
        #         else:
        #             break
        #     else:
        #         break
        #     i = i + 1
        # # 以基准位置为基础继续写入,停止条件为两字符串长度相等
        # while len(new_str) < all_len:
        #     # 每一次都要遍历标识位列表
        #     lr_flag = 0
        #     for i in range(len(new_list)-1):
        #         # 找到一个写入过的
        #         new_number = 0
        #         if new_list[i] == 0 and new_list[i+1] == 1 and lr_flag == 0:
        #             lr_flag = 1
        #             new_number = i + 1
        #         elif new_list[i] == 1 and new_list[i+1] == 0 and lr_flag == 1:
        #             new_number = i
        #             lr_flag = 0
        #         # 检查字符长度
        #         if new_number >0 : 
        #             # 将新的顺序写入列表
        #             new_list[new_number] = 0
        #             if new_number < all_len:
        #                 new_str.append(s[new_number])
        # return "".join(new_str)


        # 参考网上解法
        all_list = []
        for i in range(numRows):
            all_list.append([])
        pt = 0
        for i in range(len(s)):
            all_list[pt].append(s[i])
            if pt == 0:
                lr  = 0
            elif pt == numRows-1:
                lr = 1
            if lr == 0:
                pt +=1
            else:
                pt -=1
        ans = []
        for i in range(numRows):
            ans +=all_list[i]
        return "".join(ans)

        
# @lc code=end

s = "PAYPALISHIRING"
numRows = 3
solu = Solution()
print(solu.convert(s,numRows))