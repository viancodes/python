from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bitwise_or = 0
        for num in nums:
            bitwise_or |= num   # OR all numbers
        return bitwise_or * (1 << (len(nums) - 1))  # multiply by 2^(n-1)
