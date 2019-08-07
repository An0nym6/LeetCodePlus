# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_ = ListNode(-1)
        head_.next = head
        last = head_
        group = [head]
        for i in range(k - 1):
            if group[-1]:
                group.append(group[-1].next)
            else:
                group.append(None)
        while None not in group:
            last.next = group[-1]
            temp = group[-1].next
            for i in range(k - 1, 0, -1):
                group[i].next = group[i - 1]
            group[0].next = temp
            last = group[0]
            group = [last.next]
            for i in range(k - 1):
                if group[-1]:
                    group.append(group[-1].next)
                else:
                    group.append(None)
        return head_.next
