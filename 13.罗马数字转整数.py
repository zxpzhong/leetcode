#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = ['I','V','X','L','C','D','M']
        num_list = [1,5,10,50,100,500,1000]
        num = 0
        # for i in range(len(str_list)):
        #     idx = [j for j in range(len(s)) if s[j] == str_list[i]]
        #     for t in range(len(idx)):
        #         # 如果存在相减
        #         if idx[t] != idx[t+1]
        #     num += len(idx) * num_list[i]
        i = 0
        while i < (len(s)-1):
            if str_list.index(s[i]) >= str_list.index(s[i+1]):
                num += num_list[str_list.index(s[i])]
                i = i+1
            else:
                num = num - num_list[str_list.index(s[i])]\
                    + num_list[str_list.index(s[i+1])]
                i = i+2
        if i == len(s)-1:
            num += num_list[str_list.index(s[-1])]
        return num
# @lc code=end
