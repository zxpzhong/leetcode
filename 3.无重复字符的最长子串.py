#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.55%)
# Likes:    3052
# Dislikes: 0
# Total Accepted:    326.7K
# Total Submissions: 1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        all_len = len(s)

        # # 最大长度
        # max_len = 0
        # len_temp = 0
        # # 慢指针
        # for i in range(all_len):
        #     print('----------')
        #     print(s[i])
        #     # 快指针
        #     for j in range(1,all_len-i):
        #         # 如果慢指针位置和快指针位置相同
        #         print(s[i+j])
        #         if s[i+j] == s[i]:
        #             # 相同，快指针复位，慢指针+1，记录当前最长长度
        #             break
        #     len_temp = j
        #     print(len_temp)
        #     # 检查当前慢指针状态下最大长度是否为最大长度
        #     if len_temp > max_len:
        #         max_len = len_temp
        # return max_len

        # 队列思想解法
        max_length = 0
        queue = []
        for i in range(all_len):
            # 检查新的元素是否和之前所有的元素重复
            for j in range(len(queue)):
                if s[i] == queue[j]:
                    # 存在重复
                    # 记录当前最长长度，并且弹出至当前重复元素
                    current_length = len(queue)
                    if current_length > max_length:
                        max_length = current_length
                    queue = queue[j+1:]
                    break
            # 不存在重复，每次多加入一个元素进队列
            queue.append(s[i])
            # print(queue)
        current_length = len(queue)
        if current_length > max_length:
            max_length = current_length
        return len(s) if max_length==0 else max_length
                    



# @lc code=end
s = 'aucr'
# s = 'abcabcbb'
# s = 'pwwkew'
solu = Solution()
print(solu.lengthOfLongestSubstring(s))


