# Approach:
# 1. Classic backtracking (DFS):
#    - Pick any two numbers a, b from the list.
#    - Replace them with result of applying one of the 4 operators (+, -, *, /).
#    - Recurse with the new list (size reduces by 1).
# 2. Base case: when only one number remains, check if it's close enough to 24.
# 3. Use a small epsilon (1e-6) to handle floating-point precision for division.
# 4. Return True if any sequence of operations results in 24.
# Time: Exponential but limited since only 4 numbers.

class Solution:
    def judgePoint24(self, cards) -> bool:
        EPSILON = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = []
                    # build next list without nums[i], nums[j]
                    for k in range(len(nums)):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    # try all operations
                    for val in self.compute(nums[i], nums[j]):
                        next_nums.append(val)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()  # backtrack
            return False

        return dfs([float(x) for x in cards])

    def compute(self, a, b):
        results = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:
            results.append(a / b)
        if abs(a) > 1e-6:
            results.append(b / a)
        return results
