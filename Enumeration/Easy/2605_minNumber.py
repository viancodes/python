class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        # Find common digits
        common = set(nums1) & set(nums2)
        if common:
            return min(common)   # smallest common digit
        
        # Otherwise form the smallest two-digit number
        min1, min2 = min(nums1), min(nums2)
        return min(min1 * 10 + min2, min2 * 10 + min1)
