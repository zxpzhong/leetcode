#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (62.45%)
# Likes:    387
# Dislikes: 0
# Total Accepted:    65.1K
# Total Submissions: 102.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # start_flag = 0
        
        # pt = head.next
        # while True:
        #     if (not head == None):
        #         if (not head.next == None):
        #             # 两个两个操作
        #             next_chain = head.next.next
        #             head.next.next = head
                    
        #             head = head.next
        #             head.next.next = next_chain
        #             head = head.next.next
        #         else:
        #             break
        #     else:
        #         break
        # return pt


        # 这里有一个思想误区，题目中强调了不能单纯的改变节点内部的指
        # 而是需要实际的进行节点交换，但是你的思维不能停留在
        # 直接对原链表进行修改
        # 真正简单的方法是，新建一个链表，从头开始依次指向第二个，第一个，第二个第一个
        


        # # If the list has no node or has only one node left.
        # if not head or not head.next:
        #     return head

        # # Nodes to be swapped
        # first_node = head
        # second_node = head.next

        # # Swapping
        # first_node.next  = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # # Now the head is the second node
        # return second_node

        # 先实现一个k=2
        k = 2
        first = None
        if not head == None and not head.next == None:

            left_all = head.next.next
            first = head.next
            second = head
            first.next = second
            first.next.next = self.swapPairs(left_all)
            return first
        else:
            return head
                

# @lc code=end

a1 = ListNode(1)
a1.next = ListNode(2)
a1.next.next = ListNode(3)
a1.next.next.next = ListNode(4)

solu = Solution()
ans = solu.swapPairs(a1)
while not ans == None:
    print(ans.val)
    ans = ans.next
