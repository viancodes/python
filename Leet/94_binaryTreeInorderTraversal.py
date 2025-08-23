# Approach 1 (Recursive):
#   - Traverse left subtree → root → right subtree.
#   - Simple and clear, but uses O(h) stack space.
#
# Approach 2 (Iterative with explicit stack):
#   - Use a stack to simulate recursion.
#   - Push nodes while going left, then pop and visit, then go right.
#   - Time: O(n), Space: O(h), h = tree height.

# LeetCode provides TreeNode class:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        curr = root

        while curr or stack:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # Visit node
            curr = stack.pop()
            res.append(curr.val)
            # Move right
            curr = curr.right

        return res
