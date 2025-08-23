# Approach:
# 1) Recursion + Memoization on ranges:
#    - build(lo, hi) returns all unique BSTs using values [lo..hi].
#    - For each root r in [lo..hi], combine every left tree from build(lo, r-1)
#      with every right tree from build(r+1, hi).
# 2) Base case: if lo > hi → return [None] (empty subtree).
# 3) Memoize (lo, hi) to avoid recomputation.
# Time: Catalan-number growth ~ O(Cn), Space: O(Cn) trees; n ≤ 8 so this passes comfortably.

# LeetCode provides TreeNode; included for local runs:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        memo = {}

        def build(lo, hi):
            if lo > hi:
                return [None]
            key = (lo, hi)
            if key in memo:
                return memo[key]

            res = []
            for root_val in range(lo, hi + 1):
                left_trees = build(lo, root_val - 1)
                right_trees = build(root_val + 1, hi)
                for L in left_trees:
                    for R in right_trees:
                        node = TreeNode(root_val)
                        node.left = L
                        node.right = R
                        res.append(node)

            memo[key] = res
            return res

        return build(1, n)
