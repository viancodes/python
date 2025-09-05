# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional['TreeNode']) -> int:
        # Helper: returns the sum of all root-to-leaf numbers under "node",
        # given the number formed so far as "path_value".
        def dfs(node: Optional['TreeNode'], path_value: int) -> int:
            if node is None:
                return 0

            # Append current digit: shift left by 10 and add node.val
            new_value = path_value * 10 + node.val

            # If leaf, this path contributes exactly new_value
            if node.left is None and node.right is None:
                return new_value

            # Otherwise, sum from children
            left_sum = dfs(node.left, new_value)
            right_sum = dfs(node.right, new_value)
            return left_sum + right_sum

        return dfs(root, 0)

