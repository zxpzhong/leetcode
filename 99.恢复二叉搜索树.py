#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (54.00%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 19.4K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
# 
# 请在不改变其结构的情况下，恢复这棵树。
# 
# 示例 1:
# 
# 输入: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# 输出: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# 输出: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 进阶:
# 
# 
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 回复两个被错误交换的节点
        # 因为是二叉搜索树，所以被交换后，一定是处于两个分支，一定不满足验证要求
        # 找到不符合验证要求的两个节点，然后交换
        # 验证二叉搜索树

        # 不满足节点记录：
        self.invalid = []
        
        if root == None:
            return True
        return self.all(root,-2147483648-1,2147483647+1)
        
    def all(self,root,min_val,max_val):
        if not root.left == None:
            if not (root.left.val < root.val and root.left.val > min_val):
                # 左子树不合格
                return False
                self.invalid.append([root.left,root.left.val])
            else:
                if not self.all(root.left,min_val,root.val):
                    return False
        if not root.right == None:
            if not (root.right.val > root.val and root.right.val < max_val):
                # 不合格
                return False
            else:  
                if not self.all(root.right,root.val,max_val):
                    return False
        return True
        
# @lc code=end

