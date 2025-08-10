class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Place each number x in [1..n] at index x-1
        i = 0
        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        # First index i where nums[i] != i+1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
