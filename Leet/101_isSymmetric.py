# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return is_mirror(a.left, b.right) and is_mirror(a.right, b.left)

        return is_mirror(root.left, root.right) if root else True
