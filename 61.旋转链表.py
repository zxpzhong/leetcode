#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (39.10%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    41.1K
# Total Submissions: 103.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        # 先遍历获取长度，将最后一个位置重新指向头，形成环状
        # 然后让指针头在环中移动k步，最后将最后一个指向None
        pt = head
        length = 1
        while True:
            if not pt.next == None:
                pt = pt.next
                length+=1
            else:
                break
        # 向右旋转k步，就是向左旋转length-k%length步
        k = length-k%length
        # 此时的pt指向了最后一个元素，将最后一个元素的下一个指向头
        pre = pt
        pt.next = head
        # 指向头，开始移动
        pt = head
        while not k == 0:
            pre = pt
            pt = pt.next
            k-=1 
        # 移动完k步后，此时已经达到要求，还剩一步就是把上一项指向None
        pre.next = None
        return pt
        

        
# @lc code=end
head = None
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

k = 2

solu = Solution()
ans = solu.rotateRight(head,k)
while not ans == None:
    print(ans.val)
    ans = ans.next
