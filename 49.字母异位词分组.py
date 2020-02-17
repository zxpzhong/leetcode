#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (58.61%)
# Likes:    250
# Dislikes: 0
# Total Accepted:    46.2K
# Total Submissions: 76.6K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        from collections import Counter
        counter_list = []
        ans = []
        
        for i in range(len(strs)):
            temp = Counter(strs[i])
            if temp in counter_list:
                ans[counter_list.index(temp)].append(strs[i])
            else:
                counter_list.append(temp)
                ans.append([strs[i]])
        return ans

        
# @lc code=end

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solu = Solution()
print(solu.groupAnagrams(strs))