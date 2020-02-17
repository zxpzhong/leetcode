#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (52.90%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    24.8K
# Total Submissions: 44.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 示例:
# 
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        min_chain = ListNode(-1)
        max_chain = ListNode(-1)
        pt1 = min_chain
        pt2 = max_chain
        # 遍历链表形成两条子链
        while not head == None:
            if head.val < x:
                pt1.next = head
                pt1 = pt1.next
            else:
                pt2.next = head
                pt2 = pt2.next
            head = head.next
        pt1.next = None
        pt2.next = None
        # 掐头
        min_chain = min_chain.next
        max_chain = max_chain.next
        if min_chain == None:
            return max_chain
        else:
            # 衔接
            pt1.next = max_chain
            return min_chain
        
# @lc code=end


head = ListNode(1)
# head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)
x = 0
solu = Solution()
ans = solu.partition(head,x)
while not ans == None:
    print(ans.val)
    ans = ans.next

