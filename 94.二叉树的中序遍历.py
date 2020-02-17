#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (68.15%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 144K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     self.ans = []
    #     self.add_one(root)
    #     return self.ans
    # def add_one(self,root):
    #     if not root == None:
    #         self.add_one(root.left)
    #         self.ans.append(root.val)
    #         self.add_one(root.right)

        # 用遍历的方法做，而不用迭代算法
        # 中序遍历，左中右
        # 遍历整棵树，然后用列表记录

        # 中序遍历结果
        ans = []
        # 根节点堆栈
        root_list = []
        
        while not root == None:
            # 保留根节点
            if (not root.left == None) and (not root.right == None):
                # 这种节点需要回溯
                root_list.append(root)

            if not root.left == None:
                # 左边节点不为空，则左边继续
                root = root.left
            else:
                # 如果为空，则加入中间根节点（列表中的节点）
                ans.append(root.val)
                if not root.right == None:
                    # 左边完了才是右边
                    root = root.right
                else:
                    # 如果右边节点也为空，说明该节点已经是叶子节点，需要上到上一个
                    try:
                        root = root_list.pop()
                    except:
                        break
        return ans


        
# @lc code=end

node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

solu = Solution()
print(solu.inorderTraversal(node))

