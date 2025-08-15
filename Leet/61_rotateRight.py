# Approach:
# 1. Handle edge cases: if list is empty, has 1 node, or k = 0 → return head
# 2. Find length of the linked list
# 3. Connect the tail to the head (make it circular)
# 4. Calculate new tail position: length - (k % length) - 1
# 5. Break the circle at the new tail and set new head
# Time: O(n), Space: O(1)

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and get tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Make it circular
        tail.next = head
        
        # Step 3: Find new tail
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 4: Set new head and break circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
