#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (47.61%)
# Likes:    461
# Dislikes: 0
# Total Accepted:    68.4K
# Total Submissions: 141.1K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # ans = ListNode(0)
        # pt = ans
        # while not (l1 == None and l2 == None):
        #     if l1 == None:
        #         ans.next = ListNode(l2.val)
        #         l2 = l2.next
        #         ans = ans.next
        #     elif l2 == None:
        #         ans.next = ListNode(l1.val)
        #         l1 = l1.next
        #         ans = ans.next
        #     elif l1.val >= l2.val:
        #         ans.next = ListNode(l2.val)
        #         l2 = l2.next
        #         ans = ans.next
        #     elif l1.val < l2.val:
        #         ans.next = ListNode(l1.val)
        #         l1 = l1.next
        #         ans = ans.next
        # return pt.next

        # 1.0 暴力法 获取所有列表所有元素
        all_value = []
        for item in lists:
            while not item == None:
                all_value.append(item.val)
                item = item.next
        # 列表快排
        all_value.sort()
        # 直接输出
        a = ListNode(0)
        pt = a
        for item in all_value:
            a.next = ListNode(item)
            a = a.next
        return pt.next
        
# @lc code=end
chain_list = []
a1 = ListNode(1)
a1.next = ListNode(4)
a1.next.next = ListNode(5)
chain_list.append(a1)

a1 = ListNode(1)
a1.next = ListNode(3)
a1.next.next = ListNode(4)
chain_list.append(a1)

a1 = ListNode(2)
a1.next = ListNode(6)
chain_list.append(a1)

solu = Solution()
ans = solu.mergeKLists(chain_list)
while not ans == None:
    print(ans.val)
    ans = ans.next

