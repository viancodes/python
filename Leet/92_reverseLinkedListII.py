# Approach:
# 1. Use a dummy node to simplify edge cases (like reversing from head).
# 2. Traverse to node just before `left` (prev).
# 3. Reverse sublist from left to right using standard reversal.
# 4. Reconnect:
#    - prev.next points to new sublist head.
#    - tail of reversed sublist connects to the node after `right`.
# 5. Return dummy.next.
# One-pass: do traversal and reversal in the same loop.
# Time: O(n), Space: O(1).

# LeetCode provides ListNode; included here for local testing:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Step 1: reach node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse sublist [left..right]
        curr = prev.next
        nxt = None
        prev_sublist = None

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_sublist
            prev_sublist = curr
            curr = nxt

        # Step 3: reconnect
        prev.next.next = curr      # tail of reversed list connects to right+1
        prev.next, prev_sublist = prev_sublist, prev.next
        # prev.next becomes new head of reversed part

        return dummy.next
