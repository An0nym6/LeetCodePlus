# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_ = ListNode(-1)
        head_.next = head
        last = head_
        first = head
        if first:
            second = head.next
        else:
            second = None
        while first and second:
            last.next = second
            temp = second.next
            second.next = first
            first.next = temp
            last = first
            first = last.next
            if first:
                second = first.next
            else:
                break
        return head_.next
