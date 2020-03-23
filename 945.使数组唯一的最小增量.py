#
# @lc app=leetcode.cn id=945 lang=python
#
# [945] 使数组唯一的最小增量
#
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (40.80%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 31.8K
# Testcase Example:  '[1,2,2]'
#
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
# 
# 返回使 A 中的每个值都是唯一的最少操作次数。
# 
# 示例 1:
# 
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 
# 示例 2:
# 
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
#

# @lc code=start
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # 哈希做
        # haspmap = []
        # ans = 0
        # for i in range(len(A)):
        #     while A[i] in haspmap:
        #         # 如果哈稀表中已经有了
        #         A[i]+=1
        #         ans+=1
        #     haspmap.append(A[i])
        # return ans

        # 排序
        # A.sort()
        # from collections import Counter
        # # 获得counter
        # count = Counter(A)

        # # 去重
        # B = [set(A)]
        # # 把counter中重复的

        # # for key,value in count.items():

        # # 双指针
        # # 最小指针 = 0
        # for i in range(len(A)):
        #     pt = A[i]

        # 排序
        A.sort()
        A.append(40000*2)
        ducli_stack = []
        ans = 0
        for i in range(1,len(A)):
            # 如果重复后，直接到最大值
            if A[i] == A[i-1]:
                # 重复
                ducli_stack.append(A[i])
            else:
                # 如果不重复的话，可以补多少个元素
                # 从队列首部取元素
                # 可以多加入A[i]-A[i-1]-1个元素
                for t in range(A[i-1]+1,A[i]):
                    if ducli_stack:
                        # 如果待补充的队列不为空，则弹出一个
                        ans += t - ducli_stack[0]
                        ducli_stack.pop(0)
                    else:
                        break
        return ans



# @lc code=end
solu = Solution()
print(solu.minIncrementForUnique([1,2,2]))
