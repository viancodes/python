# Approach:
# 1. Single pass through the sorted list.
# 2. If current node value equals next node value, skip next (cur.next = cur.next.next).
# 3. Else move forward. Continue until end.
# Time: O(n), Space: O(1).

# LeetCode provides ListNode; included here for completeness in local runs:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
