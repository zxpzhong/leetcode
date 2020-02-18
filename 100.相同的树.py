#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (54.98%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    61.9K
# Total Submissions: 109.5K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 完全相同，则任意方法遍历结果相同
        return self.scan(p,q)

    def scan(self,root1,root2):
        if root1 == None or root2 == None:
            if not root1 == root2:
                return False
            else:
                return True
        elif not root1.val == root2.val:
            return False
        if not self.scan(root1.left,root2.left):
            return False
        if not self.scan(root1.right,root2.right):
            return False
        return True
        
# @lc code=end

