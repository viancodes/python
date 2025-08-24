# Approach:
# 1) Recursion with valid range (min_val, max_val) for each node.
# 2) For a valid BST: min_val < node.val < max_val strictly.
# 3) Recurse left with (min_val, node.val) and right with (node.val, max_val).
# 4) If any node violates the range, return False; else True.
# Time: O(n), Space: O(h) recursion stack (h = tree height).

# LeetCode provides TreeNode; included for local runs:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node:
                return True
            # must be strictly within (low, high)
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, None, None)
