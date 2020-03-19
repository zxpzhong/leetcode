#
# @lc app=leetcode.cn id=292 lang=python
#
# [292] Nim 游戏
#
# https://leetcode-cn.com/problems/nim-game/description/
#
# algorithms
# Easy (69.31%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 58K
# Testcase Example:  '4'
#
# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
# 
# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
# 
# 示例:
# 
# 输入: 4
# 输出: false 
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
# 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
# 
# 
#

'''
看了以下官方解答，刚开始没看懂为什么n为4的倍数对方一定获胜，就用通俗的语言写了一下n为4的倍数对方一定获胜的原因，以及n不为4的倍数我方一定获胜的原因。

石头总数S有两种情况：为4的倍数以及不为4的倍数，分别分析。

1.我方先取，每次能拿1-3个石头，如果石头数S < 4, 则我方可直接把所有的石头拿完获胜
2.如果石头数S=4，我方不能一次把石头拿完，当我方拿1-3个时，对应的还剩下3-1个，对方都可以一次拿完。对方获胜

类似的
1.有S个石头，不管我怎样取，最后的结果无外乎是S - 1， S - 2, S - 3,这时对方只要取对对应的石头，使剩下的石头数为4的倍数，我方就又会面临一个剩余石头为4的倍数的局面，直到最后一次S = 4，我方就会输。
2.而如果不是4的倍数，我则可以取对应的石头，使对方所面临的局面为剩余S为4的倍数。

作者：minerva-3
链接：https://leetcode-cn.com/problems/nim-game/solution/nwei-4de-bei-shu-dui-fang-yi-ding-huo-sheng-de-yua/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 示例反而给了提示啊，赢的目标就是刚好剩下4块石头
        # 1 2 3 4好理解，同样，如果是4的整数倍+1 +2 +3 +4也是同样的
        # 如果刚好是4的整数倍，则我不论拿多少，对方只要拿剩下的，使得仍然是4的整数倍，则对方一定赢
        # 如果不是4的整数倍，则我拿到刚好为4的整数倍，则我一定赢
        if n % 4 == 0:
            return False
        else:
            return True

# @lc code=end

