# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = None
        last = head
        while l1 or l2 or carry:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            sumVal = val1 + val2 + carry
            carry = sumVal / 10
            current = ListNode(sumVal % 10)
            if head == None:
                head = current
            else:
                last.next = current
            last = current
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        current = None
        return head
