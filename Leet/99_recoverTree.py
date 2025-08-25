class Solution:
    def recoverTree(self, root: Optional['TreeNode']) -> None:
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node
            self.prev = node

            inorder(node.right)

        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
