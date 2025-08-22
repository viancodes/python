# Approach:
# 1. Use two lists with dummies: "before" (< x) and "after" (>= x).
# 2. Traverse original list; append each node to the appropriate list.
# 3. Connect before tail to after head; set after tail.next = None.
# 4. Return before_dummy.next to preserve original relative order.
# Time: O(n), Space: O(1) extra nodes.

# LeetCode provides ListNode; included here for local runs:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy

        cur = head
        while cur:
            nxt = cur.next  # save next
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next
            cur.next = None  # detach to avoid accidental cycles
            cur = nxt

        before.next = after_dummy.next
        return before_dummy.next
