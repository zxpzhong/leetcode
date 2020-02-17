#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (59.38%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    19.1K
# Total Submissions: 31.3K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def front_digui(root):
    """利用递归实现树的先序遍历"""
    if root == None:
        print('None')
        return
    print(root.val)
    front_digui(root.left)
    front_digui(root.right)
    
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 给定n，创建树的最大深度为n层
        # 每一个数的上面一定有数，其他地方都可以用None替换
        # 二叉搜索树：左小右大
        if n == 0: return []
        # 这个解法太巧妙了！！！
        def helper(start, end):
            res = []
            # 起始大于结束，无法添加新节点，只能加None
            if start > end:
                res.append(None)
            '''
            这里很巧妙就是没有终止条件
            实际上，终止条件就一个，那就是下面的循环不会进去，而是直接return
            也就是start=end+1，也就是无法分下去只剩下一个节点的时候
            '''
            # 从起始到结束遍历根节点，对于每个根节点创建
            for val in range(start, end + 1):
                # 左子树遍历
                for left in helper(start, val - 1):
                    # 右子树遍历
                    for right in helper(val + 1, end):
                        # 针对当前这个情况，先用val创建节点
                        root = TreeNode(val)
                        # 创建指向
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return helper(1, n)

# @lc code=end
solu = Solution()
ans = solu.generateTrees(3)
for item in ans:
    front_digui(item)
    print('-----')
