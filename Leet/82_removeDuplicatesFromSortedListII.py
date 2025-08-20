# Approach:
# 1. Use a dummy node before head to handle deletions at the start.
# 2. Traverse with `prev` (last node in result) and `cur` (scanner).
# 3. If `cur` begins a run of duplicates (cur.val == cur.next.val), advance `cur`
#    to skip the entire run, then link `prev.next` to the node after the run.
# 4. Otherwise (single node, no duplicate), move `prev` forward to `cur`.
# 5. Continue until the end; return dummy.next.
# Time: O(n), Space: O(1).

# LeetCode provides ListNode; included here for completeness in local runs:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            dup = False
            # Move cur to the end of the current duplicate run
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                dup = True

            if dup:
                # Skip all duplicates
                prev.next = cur.next
            else:
                # Keep this unique node
                prev = prev.next

            cur = cur.next

        return dummy.next
