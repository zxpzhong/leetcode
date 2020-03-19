#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.89%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 131.3K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
import functools
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 给定一个字符串，把该字符串拆分成多个部分，其中每个部分的值在1-26之间
    #     self.ans = 0
    #     self.split_one(s)
    #     return self.ans
    # # @functools.lru_cache()
    # def split_one(self,cur_str):
    #     length = len(cur_str)
    #     if length == 0:
    #         # 分解完毕
    #         self.ans+=1
    #         return
    #     if not cur_str[0] == '0':
    #         self.split_one(cur_str[1:])
    #         if length >= 2 and int(cur_str[:2]) <= 26:
    #             # 两位也可以拿出来解释
    #             self.split_one(cur_str[2:])
    #     # 如果第一位等于0或者是前两位不小于26，则不会继续分解


    # 尝试加入LRU cache来让原来超时的解法通过
        self.ans = 0
        self.split_one(s)
        return self.split_one(s)
    @functools.lru_cache()
    def split_one(self,cur_str):
        length = len(cur_str)
        ans = 0
        if length == 0:
            # 分解完毕
            # self.ans+=1
            return 1
        if not cur_str[0] == '0':
            ans+=self.split_one(cur_str[1:])
            if length >= 2 and int(cur_str[:2]) <= 26:
                # 两位也可以拿出来解释
                ans+=self.split_one(cur_str[2:])
        return ans
        # 如果第一位等于0或者是前两位不小于26，则不会继续分解


        # # 无脑递归超时
        # length = len(s)
        # # 上次结果
        # pre = 1
        # # 当前结果
        # cur = 1
        # if s[0] == '0':
        #     return 0
        # ans = 0
        # for i in range(1,length):
        #     temp = cur * (1 if not s[i] == '0' else 0) + pre * (1 if 9<int(s[i-1:i+1]) <= 26 else 0)
        #     pre = cur
        #     cur = temp
        # return cur


# @lc code=end

solu = Solution()
print(solu.numDecodings('226'))