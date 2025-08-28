# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Returns height if subtree is balanced, otherwise returns -1 as a sentinel.
        def height_or_fail(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_height = height_or_fail(node.left)
            if left_height == -1:
                return -1  # left subtree unbalanced

            right_height = height_or_fail(node.right)
            if right_height == -1:
                return -1  # right subtree unbalanced

            if left_height - right_height > 1 or right_height - left_height > 1:
                return -1  # current node unbalanced

            # height of current node = 1 + max(left, right)
            if left_height >= right_height:
                return 1 + left_height
            else:
                return 1 + right_height

        return height_or_fail(root) != -1
