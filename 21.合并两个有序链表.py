#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (57.48%)
# Likes:    821
# Dislikes: 0
# Total Accepted:    169.4K
# Total Submissions: 286.2K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        pt = ans
        while not (l1 == None and l2 == None):
            if l1 == None:
                ans.next = ListNode(l2.val)
                l2 = l2.next
                ans = ans.next
            elif l2 == None:
                ans.next = ListNode(l1.val)
                l1 = l1.next
                ans = ans.next
            elif l1.val >= l2.val:
                ans.next = ListNode(l2.val)
                l2 = l2.next
                ans = ans.next
            elif l1.val < l2.val:
                ans.next = ListNode(l1.val)
                l1 = l1.next
                ans = ans.next
        return pt.next

        
# @lc code=end

solu = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
ans = solu.mergeTwoLists(l1,l2)
while not ans == None:
    print(ans.val)
    ans = ans.next
