#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (51.91%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 32.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 获取链表长度
        start = head
        length = 0
        last = head
        # 获取最后一个节点
        while not start == None:
            length +=1
            last = start
            start = start.next
        
        temp = head.next
        head.next = last
        head.next.next = temp
        start = head
        for i in range(length-1):
            start = start.next
        start.next = None
        a = 1

# @lc code=end

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
solu = Solution()
solu.reorderList(a)