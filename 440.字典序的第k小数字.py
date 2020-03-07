#
# @lc app=leetcode.cn id=440 lang=python
#
# [440] 字典序的第K小数字
#
# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (29.19%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 8.5K
# Testcase Example:  '13\n2'
#
# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
# 
# 注意：1 ≤ k ≤ n ≤ 10^9。
# 
# 示例 :
# 
# 
# 输入:
# n: 13   k: 2
# 
# 输出:
# 10
# 
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
# 
# 
#

# @lc code=start
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #----------超内存
        # 先对1-n数字进行字典序排序
        # candi = [str(i+1) for i in range(n)]
        # candi.sort()
        # return candi[k-1]
        
    #     ans = ''
    #     new_n = k
    #     while not n<10:
    #         # 获取到打头数字，继续分解
    #         start,count = self.get_start(n,k)
    #         ans+=str(start)
    #         # 第二波分解
    #         new_n = 0
    #         head = self.is_n_start(n)
    #         if head == start:
    #             new_n = n
    #         elif head>start:
    #             new_n = int(str(start)+str(new_n)[1:])
    #         else:
    #             new_n = (n//head//10)*(start+1)-1
    #         # start2 = self.get_start(new_n,k-count-2)
    #         n = new_n
    #         if k-count == 1:
    #             return int(ans)
    #         elif k-count == 2:
    #             return int(ans+'0')
    #         k = k-count-2

    #     ans+=str(new_n)
    #     return int(ans)


    # def get_start(self,n,k):
    #     number = 0
    #     count = [0]*9
    #     return_flag = 0
    #     for j in range(1,10):
    #         for i in range(1,n+1):
    #             if self.is_n_start(i) == j:
    #                 number+=1
    #                 count[j-1]+=1
    #                 if number == k:
    #                     return_flag = 1
    #         if return_flag == 1:
    #             return j,sum(count[:j])
                        


    # def front_digui(self, root):
    #     """利用递归实现树的先序遍历"""
    #     if root == None:
    #         return
    #     print(root.val)
    #     self.front_digui(root.left)
    #     self.front_digui(root.right)
    #     x = 1
    #     count = 1
    #     while count < k:
    #         x = self.generate_next(n,x)
    #         count += 1
    #         print(x)
    #     return x

    # def is_n_start(self,x):
    #     if (x >= 100000000):
    #         return x//100000000
    #     if (x >= 10000000):
    #         return x//10000000
    #     if (x >= 1000000):
    #         return x//1000000
    #     if (x >= 100000):
    #         return x//100000
    #     if (x >= 10000):
    #         return x//10000
    #     if (x >= 1000):
    #         return x//1000
    #     if (x >= 100):
    #         return x//100
    #     if (x >= 10):
    #         return x//10
    #     return x  
    # def max_zero(self,x):
    #     if (x % 100000000 == 0):
    #         return x//100000000
    #     if (x % 10000000 == 0):
    #         return x//10000000
    #     if (x % 1000000 == 0):
    #         return x//1000000
    #     if (x % 100000 == 0):
    #         return x//100000
    #     if (x % 10000 == 0):
    #         return x//10000
    #     if (x % 1000 == 0):
    #         return x//1000
    #     if (x % 100 == 0):
    #         return x//100
    #     if (x % 10 == 0):
    #         return x//10
    #     return x

    # def generate_next(self,x,cur):
    #     # 后面+0
    #     if cur*10<=x:
    #         return cur*10
    #     # +1
    #     if cur%10 <= 8:
    #         if cur + 1 <= x:
    #             return cur+1
    #         else:
    #             # cur = self.is_n_start(cur)+1
    #             cur = 
    #             return cur
    #     # 去0
    #     if cur%10 == 9:
    #         cur = cur+1
    #         return self.max_zero(cur)
    # def findKthNumber(n,k):

        i = 1
        p = 1
        while p < k:
            cnt = self.get_count(i,n)
            # 根节点+该子树节点大于k，说明要的节点在该子树内，根节点往子树移动
            if p+cnt > k:
                i = i * 10
                p = p + 1
            # 如果<k，说明节点在其他子树内，调整下级子树，遍历节点总数加上上次遍历的子树
            else:
                i = i + 1
                p = p + cnt
        return i

    # 可以理解成一个十叉树
    def get_count(self,i,n):
        # 节点统计
        cnt = 0
        # 
        a = i

        b = i+1
        # a
        while a <= n:
            # 统计<n且首尾a的个数
            cnt += min((n+1), b) - a
            a*=10
            b*=10
        return cnt     
# @lc code=end

n = 100
k = 10
solu = Solution()
print(solu.findKthNumber(n,k))