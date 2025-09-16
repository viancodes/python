class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        
        for i in range(1, n + 1):  # 1-indexed loop
            if n % i == 0:
                total += nums[i - 1] ** 2  # adjust for 0-indexed array
                
        return total
