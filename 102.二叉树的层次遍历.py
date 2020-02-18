#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (58.95%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    78.2K
# Total Submissions: 128.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.ans = []
        self.scan = []
        self.level_queue(root)
        pt = 0
        i = 2
        from collections import Counter 
        while True:
            # 当前位置
            queue = self.scan[pt:pt+i]
            pt = pt+i
            i=i*2
            # 如果queue中有一个是None，那么下一行会减少2个
            i = i - Counter(queue)['None']*2
            try:
                while True:
                    queue.remove('None')
            except:
                pass
            if len(queue) > 0:
                self.ans.append(queue)
            if pt >= len(self.scan):
                break
        self.ans.insert(0,[root.val])
        return self.ans
    
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

