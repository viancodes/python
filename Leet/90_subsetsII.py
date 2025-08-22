# Approach:
# 1. Sort nums to group duplicates together.
# 2. Backtracking:
#    - At each index, decide to include nums[i] or skip.
#    - To avoid duplicate subsets: if nums[i] == nums[i-1] and i > start, skip.
# 3. Add every path to result.
# Time: O(n * 2^n), Space: O(n) recursion depth.

class Solution:
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()

        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res
