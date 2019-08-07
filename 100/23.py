# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        current = None
        heap = []
        mapping = {}
        for index, listNode in enumerate(lists):
            if listNode:
                heapq.heappush(heap, listNode.val)
                if listNode.val in mapping:
                    mapping[listNode.val].append(index)
                else:
                    mapping[listNode.val] = [index]
        while heap:
            val = heapq.heappop(heap)
            newNode = ListNode(val)
            if not head:
                head = newNode
            else:
                current.next = newNode
            current = newNode
            listIndex = mapping[val].pop()
            lists[listIndex] = lists[listIndex].next
            if lists[listIndex]:
                heapq.heappush(heap, lists[listIndex].val)
                if lists[listIndex].val in mapping:
                    mapping[lists[listIndex].val].append(listIndex)
                else:
                    mapping[lists[listIndex].val] = [listIndex]
        return head