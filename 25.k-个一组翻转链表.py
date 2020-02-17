#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (54.60%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 61.9K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 示例 :
# 
# 给定这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 说明 :
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 竟然是卡在一个逆序上面
        def reverse(head,left_all,N):
            pre = left_all

            for i in range(N):
                nexttemp = head.next
                head.next = pre
                pre = head
                head = nexttemp
            return pre  

        # 先实现一个k=2

        # 判断接下来的N个节点是否为空
        def nextNisempty(head,N):
            # Nlist = []
            for i in range(N):
                if head == None:
                    return True,None
                # 记录K区间内的所有节点
                # Nlist.append(head)
                head = head.next
            left_all = head
            return False,left_all


        first = None

        isempty,left_all = nextNisempty(head,k)
        if not isempty ==True:
            pt = reverse(head,self.reverseKGroup(left_all,k),k)
            # 最后一次交换比较特殊，首节点指向剩余所有的
            return pt
        else:
            return head
        
            
# @lc code=end
a1 = ListNode(1)
a1.next = ListNode(2)
a1.next.next = ListNode(3)
a1.next.next.next = ListNode(4)
a1.next.next.next.next = ListNode(5)

k = 3


solu = Solution()
ans = solu.reverseKGroup(a1,k)
while not ans == None:
    print(ans.val)
    ans = ans.next

