#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (35.72%)
# Likes:    663
# Dislikes: 0
# Total Accepted:    112.3K
# Total Submissions: 302.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 获取链表长度
        pt = head
        length = 0
        while not pt == None:
            print(pt.val)
            length += 1
            pt = pt.next
        print(length)
        # 获取正序删除元素序号
        delete_posi = length-n
        if delete_posi == 0:
            return head.next
        pt = head
        length = 0
        while not head == None:
            length += 1
            if length == delete_posi:
                head.next =  head.next.next
            else:
                head = head.next
        # exit()
        return pt


        # 网上的逆序做法
        # def reverse(head):
        #     pre = None
        #     while head:
        #         nexttemp = head.next
        #         head.next = pre
        #         pre = head
        #         head = nexttemp
        #     return pre     
        # # 逆序
        # pre = reverse(head)
        # k = 0
        # # 用0节点当成首节点
        # res = ListNode(0)
        # res.next = pre
        # while pre:
        #     # 如果n是倒数第一个，那么就是删除逆序后的第一个元素
        #     if n == 1:
        #         # res指向pre的下一个元素即可
        #         res.next = pre.next
        #         break
        #     # 链表节点计数
        #     k += 1
        #     # 在长度范围内
        #     if k < n-1:
        #         # 指向下一个节点
        #         pre = pre.next
        #         # 如果为空，返回空
        #         if pre == None: return None
        #         continue
        #     # pre指向下一个
        #     pre.next = pre.next.next
        #     break
        # return reverse(res.next)


        
# @lc code=end

# a = ListNode(1)
# a.next = ListNode(2)
# a.next.next = ListNode(3)
# a.next.next.next = ListNode(4)
# a.next.next.next.next = ListNode(5)

# n = 2

a = ListNode(1)

n = 1

solu = Solution()
ans = solu.removeNthFromEnd(a,n)
print('------')
while not ans == None:
    print(ans.val)
    ans = ans.next