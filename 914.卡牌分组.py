#
# @lc app=leetcode.cn id=914 lang=python
#
# [914] 卡牌分组
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (31.46%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 29.2K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
# 
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 
# 
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 
# 
# 仅当你可选的 X >= 2 时返回 true。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 
# 
# 示例 2：
# 
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 3：
# 
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 4：
# 
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 
# 
# 示例 5：
# 
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
# 
# 
# 
# 提示：
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def isOK(val1,val2):
            # val1,val2是否有大于2的最大公约数
            for i in range(2,min(val1,val2)+1):
                if val1%i == 0 and val2 %i == 0:
                    return True
            return False
        # 分组可以打乱顺序
        # 每一组都有X张牌,X自选，X>=2
        if len(deck) <2:
            return False
        from collections import Counter
        count = Counter(deck)
        values = list(set(count.values()))
        # count中的所有值是否存在大于2的最大最大公约数：
        for i in range(2,min(values)+1):
            j = 0
            for item in (values):
                if not item%i == 0:
                    break
                j+=1
            if j == len(values):
                return True
        return False

# @lc code=end

deck = [1,1,1,2,2,2,3,3]
solu = Solution()
print(solu.hasGroupsSizeX(deck))