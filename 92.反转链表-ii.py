#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (46.96%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 66.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 判断链表是否为空
        if head == None or head.next == None:
            return
        pt = 0
        while pt < m-1:
            head = head.next
            pt+=1

        pre = None	# 前驱节点
        cur = None	# 当前节点
        next = None	# 后继节点
        # 把链表首节点变为尾节点
        cur = head.next
        next = cur.next
        cur.next = None
        pre = cur
        cur = next
        # 使当前遍历到的节点cur指向其前驱节点
        while pt < n:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = cur.next
            cur = next
            pt+=1
        cur.next = pre
        head.next = cur

        return head
        

        # 网上答案～～～～～～～～～～～～
        # m对应节点是头结点，直接翻转
        if m == 1: return self.reverse(head, m, n)
        
        count = 1
        h = head
        while h:    #找到m前一个节点preRev
            if count == m - 1:
                preRev = h 
            h = h.next
            count += 1
        headRev = self.reverse(preRev.next, m, n)
        preRev.next = headRev 
        return head

    def reverse(self, head, m, n):
        '''
        该函数完成m-n的翻转以及翻转后与剩余链表相连两个任务
        '''
        pre, cur = None, head
        #翻转m-n链表
        for _ in range(n - m + 1):
            pre, pre.next, cur = cur, pre, cur.next
        head.next = cur #与剩余链表相连
        return pre  

        
        
# @lc code=end
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solu = Solution()

ans = solu.reverseBetween(head,2,4)
while not ans == None:
    print(ans.val)
    ans = ans.next