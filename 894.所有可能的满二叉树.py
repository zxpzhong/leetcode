#
# @lc app=leetcode.cn id=894 lang=python
#
# [894] 所有可能的满二叉树
#
# https://leetcode-cn.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (71.57%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 6.5K
# Testcase Example:  '7'
#
# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
# 
# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
# 
# 答案中每个树的每个结点都必须有 node.val=0。
# 
# 你可以按任何顺序返回树的最终列表。
# 
# 
# 
# 示例：
# 
# 输入：7
# 
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 20
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        
# @lc code=end

