#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (71.02%)
# Likes:    456
# Dislikes: 0
# Total Accepted:    124.5K
# Total Submissions: 172.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 找最大深度，直接层次遍历最后一层就是最大层啊
        if root == None:
            return 0
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

        return len(self.ans)
    
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

