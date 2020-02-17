#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.88%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    129.6K
# Total Submissions: 371.5K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         nums = len(strs)
#         if nums == 0:
#             return ""
#         elif nums == 1:
#             return strs[0]
#         # print(nums)
#         a = 10000
#         idx = 0
#         for i in range(nums):
#             if len(strs[i]) <= a:
#                 a = len(strs[i])
#                 idx = i
#         # 找到最短字符
#         basestr = strs[idx]
#         # print(basestr)
#         for t in range(0,len(basestr)):
#             # print(t)
#             flag = True
#             # count = 0
#             if t == 0:
#                 pass
#                 for i in range(nums):
#                     basestr2 = basestr
#                     if strs[i][:len(basestr)] == basestr:
#                         # count += 1
#                         pass
#                     else:
#                         flag = False
#                         break
                
#             else:
#                 basestr2 = basestr[:-t]
#                 # print(t,basestr2)
#                 for i in range(nums):
#                     # print(strs[i][:len(basestr)-t],basestr2)
#                     if strs[i][:len(basestr)-t] == basestr2:
#                         pass
#                         # count += 1
#                     else:
#                         flag = False
#                         break
#             if flag == True:
#                 # print('yep')
#                 return basestr2
#         return ""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        print(sz)
        print(ret)
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret

# @lc code=end
print('123')
test = ["flower","flow","flight"]
# test = ["oo","oo","oo"]
# test = [""]
s = Solution()
ans = s.longestCommonPrefix(test)
print(ans)
