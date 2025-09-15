class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -1
        
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                length = 2
                j = i + 1
                diff = -1
                while j + 1 < n and nums[j + 1] - nums[j] == diff:
                    length += 1
                    j += 1
                    diff *= -1
                ans = max(ans, length)
        
        return ans
