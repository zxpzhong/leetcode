#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (50.99%)
# Likes:    548
# Dislikes: 0
# Total Accepted:    71.1K
# Total Submissions: 136.6K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        number_dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }

        def add_number(strlist,number):
            ans_list = []
            for i in range(len(strlist)):
                # print((number_dict[number[0]]))
                # exit()
                for j in range(len(number_dict[number])):
                    ans_list.append(strlist[i]+number_dict[number][j])
            return ans_list



        all_ans = ['']
        for i in range(len(digits)):
            all_ans = add_number(all_ans,digits[i])
        return all_ans
        
# @lc code=end
digits = '23'
solu = Solution()
print(solu.letterCombinations(digits))

