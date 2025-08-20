# Approach:
# 1. Backtracking: build subsets by deciding to include/exclude each element.
# 2. At each index i, choose nums[i] and recurse; then backtrack and skip it.
# 3. Add current path to result at every step (every prefix is a valid subset).
# Time: O(n * 2^n) to generate and copy all subsets, Space: O(n) recursion depth.

class Solution:
    def subsets(self, nums):
        res, path = [], []

        def backtrack(start):
            res.append(path[:])             # record current subset
            for i in range(start, len(nums)):
                path.append(nums[i])        # choose
                backtrack(i + 1)            # explore
                path.pop()                  # un-choose

        backtrack(0)
        return res
