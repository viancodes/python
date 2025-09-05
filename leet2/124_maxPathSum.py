# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        # Global maximum path sum found so far; start at -inf to handle all-negative trees
        self.ans = float('-inf')

        def gain(node: Optional['TreeNode']) -> int:
            if node is None:
                return 0

            # Max gain from left and right; ignore negatives
            left_gain = gain(node.left)
            if left_gain < 0:
                left_gain = 0

            right_gain = gain(node.right)
            if right_gain < 0:
                right_gain = 0

            # Path that turns at 'node' (could use both children)
            path_sum_through_node = node.val + left_gain + right_gain

            # Update global best
            if path_sum_through_node > self.ans:
                self.ans = path_sum_through_node

            # Return gain to parent: node plus the better single side
            if left_gain > right_gain:
                return node.val + left_gain
            else:
                return node.val + right_gain

        _ = gain(root)
        return self.ans

