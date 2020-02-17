#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.64%)
# Likes:    408
# Dislikes: 0
# Total Accepted:    68.1K
# Total Submissions: 235.5K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
# 
#


#coding=utf-8

class Node(object):
    """节点类"""
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, val):
        """为树添加节点"""
        node = Node(val)
        if self.root.val == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.val)
        self.front_digui(root.left)
        self.front_digui(root.right)


    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.left)
        print(root.val)
        self.middle_digui(root.right)


    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        print(root.val)


    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right                  #开始查看它的右子树


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.val)
            node = node.right                  #开始查看它的右子树


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().val)


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 验证二叉搜索树
        if root == None:
            return True
        return self.all(root,-2147483648-1,2147483647+1)
        
    def all(self,root,min_val,max_val):
        if not root.left == None:
            if not (root.left.val < root.val and root.left.val > min_val):
                # 不合格
                return False
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

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(3)
# root.right = TreeNode(3)


# 这TM测试用例，是人干的事么
# vals = [-2147483648,None,2147483647]

root = TreeNode(-2147483648)
# root.left = TreeNode(1)
root.right = TreeNode(2147483647)


# tree = Tree()          #新建一个树对象
# for val in vals:                  
#     tree.add(val)           #逐个添加树的节点
solu = Solution()
print(solu.isValidBST(root))