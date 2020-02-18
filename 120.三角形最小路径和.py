#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (61.92%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    39.6K
# Total Submissions: 62.2K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:return 0
        if len(triangle) == 1:return triangle[0][0]     #特例考虑

        dp = triangle

        # 初始化填充第一行第二行，这两行为特例
        # 第一行就是本身
        dp[0][0] = triangle[0][0]
        # 第二行为本身加上第一行元素
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]      #dp特例填充

        # 遍历每一行
        for idx1, ele1 in enumerate(triangle):
            # 每一行的每一个元素遍历
            for idx2, ele2 in enumerate(ele1):
                # 如果索引大于1，才进行一下操作，第一个位置的元素不处理？？
                # 是的，因为最左边的元素只能从上一行的最左边的元素过来
                if idx1 > 1:
                    # 如果行数索引大于元素在行索引并且大于1
                    if idx1 > idx2 >= 1:
                        # 这样限制下来其实就是每一行除掉两端的元素，才会有这样计算最小值的操作
                        # 对于每一行中间的元素，取当前和上一行对应两个元素更小那个的和，即为到达当前位置的最小路径
                        dp[idx1][idx2] = min(dp[idx1-1][idx2-1], dp[idx1-1][idx2]) + triangle[idx1][idx2]
                    elif idx2 == 0:
                        # 处理最左边元素，只有一条路径，所以不需要判断
                        dp[idx1][idx2] = dp[idx1-1][idx2] + triangle[idx1][idx2]
                    else:
                        # 最右边元素，也不需要判断
                        dp[idx1][idx2] = dp[idx1-1][idx2-1] + triangle[idx1][idx2]
        return min(dp[-1])

# @lc code=end

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
solu = Solution()
print(solu.minimumTotal(triangle))
