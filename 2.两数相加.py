#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.74%)
# Likes:    3794
# Dislikes: 0
# Total Accepted:    305.6K
# Total Submissions: 839.3K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pt = l1
        base = 1
        x1 = 0
        while not pt == None:
            # print(pt.val)
            x1 += pt.val * base
            base = base * 10
            pt = pt.next
        pt = l2
        base = 1
        x2 = 0
        while not pt == None:
            x2 += pt.val * base
            base = base * 10
            pt = pt.next
        ans = x1 + x2
        start = ListNode(ans%10)
        pt = start
        ans = int(ans /10)
        while not ans == 0:
            pt.next = ListNode(ans%10)
            ans = int(ans /10)
            pt = pt.next
        return start
# @lc code=end
solu = Solution()
# solu
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
start = solu.addTwoNumbers(l1,l2)
while not start == None:
    print(start.val)
    start = start.next
