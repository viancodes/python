class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        ans = float('inf')

        for i in range(n - 2):       # first cut
            for j in range(i + 1, n - 1):  # second cut
                cost = nums[0] + nums[i + 1] + nums[j + 1]
                ans = min(ans, cost)

        return ans
