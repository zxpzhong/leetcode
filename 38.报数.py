#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (52.68%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    69.8K
# Total Submissions: 128.6K
# Testcase Example:  '1'
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 
# 注意：整数序列中的每一项将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似
# "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
# 
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def get_next(item):
            # 快慢指针
            slow_pt = 0
            fast_pt = 1
            out_str = ''
            while fast_pt <= len(item):
                if fast_pt == len(item):
                    # 快指针到达最后一位时停止
                    # 如果不想等，则慢指针移动至慢指针位置，快指针再向前移动一位
                    out_str+=(str(fast_pt-slow_pt)+item[slow_pt])
                    slow_pt = fast_pt
                    fast_pt += 1
                    continue
                elif item[slow_pt] == item[fast_pt] :
                    # 如果相等，则快指针继续移动
                    fast_pt += 1
                    continue
                # 如果不想等，则慢指针移动至慢指针位置，快指针再向前移动一位
                out_str+=(str(fast_pt-slow_pt)+item[slow_pt])
                slow_pt = fast_pt
                fast_pt += 1
            return out_str
        init = '1'
        for i in range(n-1):
            init = get_next(init)
        return init
            
            
            
        
# @lc code=end
n = 4

solu = Solution()
print(solu.countAndSay(n))

