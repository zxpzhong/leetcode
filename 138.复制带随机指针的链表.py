#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (37.72%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 46.9K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的 深拷贝。 
# 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 示例 4：
# 
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
# 
# 
# 
# 
# 提示：
# 
# 
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。
# 
# 
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # start = Node(head.val,None,None)
        # start.next = Node(head.next.val)
        # # start.random = Node(head.random.val)
        # start.random = head.random
        # pt = head.next
        # pt_ans = start.next
        if head == None:
            return None

        flag = 0
        pt = Node(head.val,None,head.random)
        start = pt
        ori_head = head
        random_list = []
        while not ori_head == None:
            pt.val = ori_head.val
            ori_head = ori_head.next
            if not ori_head == None:
                pt.next = Node(0)
                pt = pt.next
        # 链表复制完毕，进行随机指针的赋值
        ori_head = head
        pt = start
        while not ori_head == None:
            # 遍历查看是指向哪个节点
            orihead2 = head
            randomidx = 0
            while not orihead2 == None:
                if ori_head.random == orihead2:
                    break
                randomidx+=1
                orihead2 = orihead2.next
            anshead2 = start
            while randomidx > 0:
                anshead2 = anshead2.next
                randomidx-=1
            pt.random = anshead2
            pt = pt.next
            ori_head = ori_head.next
        return start

# @lc code=end

