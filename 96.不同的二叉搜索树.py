#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (62.36%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    29.5K
# Total Submissions: 45.6K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用递归完成试试
    #     self.n = n
    #     self.ans = 0
    #     candi = [i for i in range(1,n+1)]
    #     for i in range(n):
    #         self.add_one(candi[i],candi[:i],candi[i+1:],0)
    #     return self.ans


    # # 每次添加一个节点，满足搜索树
    # def add_one(self,root,left,right,length):
    #     if len(left) == 0 and len(right) == 0 and length == self.n-1:
    #         # 左边、右边已经耗尽
    #         self.ans +=1
    #     else:
    #         for i in range(len(left)):
    #             # 左边还可以
    #             if left[i] < root:
    #                 self.add_one(left[i],left[:i],left[i+1:],length+1)
    #         for j in range(len(right)):
    #             if right[j] > root:
    #                 self.add_one(right[j],right[:j],right[j+1:],length+1)
    # --------------------------------上面是自己做的递归0------  
    # 自己这样做的递归，最大的问题在于，你每次对于每一个节点只添加一个，但是有可能人家是两个子节点都有值的  

        ans = [0]*(n+1)
        ans[0] = 1
        ans[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                ans[i] += ans[j-1]*ans[i-j]
        print(ans)
        return ans[n]


# @lc code=end

solu = Solution()
ans = solu.numTrees(3)
print(ans)