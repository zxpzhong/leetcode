#
# @lc app=leetcode.cn id=859 lang=python
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.02%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 37.4K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false
# 。
# 
# 
# 
# 示例 1：
# 
# 输入： A = "ab", B = "ba"
# 输出： true
# 
# 
# 示例 2：
# 
# 输入： A = "ab", B = "ab"
# 输出： false
# 
# 
# 示例 3:
# 
# 输入： A = "aa", B = "aa"
# 输出： true
# 
# 
# 示例 4：
# 
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 
# 
# 示例 5：
# 
# 输入： A = "", B = "aa"
# 输出： false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。
# 
# 
#

# @lc code=start
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # 全是小写
        # 只能交换两个字母
        # 相等返回True
        # 不相等返回False
        if not len(A) == len(B):
            return False
        if len(A) == 0 or len(B) == 0:
            return False
        ans = []
        flag = 0
        for i in range(len(A)):
            if not A[i] == B[i]:
                ans.append(i)
        if len(ans) == 2 and A[ans[0]] == B[ans[1]] and A[ans[1]] == B[ans[0]]:
            return True
        elif len(ans) == 0:
            # 全相等，如果存在重复字符则可以
            from collections import Counter
            temp = Counter(A)
            if max(temp.values())>=2:
                return True
            else:
                return False
        else:
            return False

# @lc code=end

A = "aaa"
B = "aaa"
solu = Solution()
print(solu.buddyStrings(A,B))
