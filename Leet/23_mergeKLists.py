import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0  # Unique counter to avoid comparison of ListNode objects

        # Initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1

        dummy = ListNode()
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
