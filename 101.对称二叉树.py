#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (48.58%)
# Likes:    613
# Dislikes: 0
# Total Accepted:    94.4K
# Total Submissions: 188.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 如果两颗树是对称，那么层次遍历具有一定特点
        # 
        self.scan = []
        self.level_queue(root)
        pt = 0
        i = 2
        from collections import Counter 
        while True:
            # 当前位置
            queue = self.scan[pt:pt+i]
            length = len(queue)
            if not queue[:length//2] == queue[length//2:][::-1]:
                return False
            pt = pt+i
            i=i*2
            # 如果queue中有一个是None，那么下一行会减少2个
            i = i - Counter(queue)['None']*2
            if pt >= len(self.scan):
                return True

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            if not node.left == None:
                self.scan.append(node.left.val)
            else:
                self.scan.append('None')
            if not node.right == None:
                self.scan.append(node.right.val)
            else:
                self.scan.append('None')
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)
        
# @lc code=end

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(6)
# root.left.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
# root.right.right = TreeNode(4)
solu = Solution()
print(solu.isSymmetric(root))