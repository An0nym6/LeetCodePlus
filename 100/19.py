# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head_ = ListNode(-1)
        head_.next = head
        first = head_
        second = head_
        n += 1
        while first:
            first = first.next
            if n:
                n -= 1
            else:
                second = second.next
        if second.next == head:
            head = head.next
        second.next = second.next.next
        return head
