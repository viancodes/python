# Approach (Dutch National Flag Algorithm):
# 1. Use three pointers: low, mid, high.
#    - low: boundary for 0s
#    - mid: current element being processed
#    - high: boundary for 2s
# 2. Rules:
#    - If nums[mid] == 0 → swap(nums[low], nums[mid]), low++, mid++
#    - If nums[mid] == 1 → mid++
#    - If nums[mid] == 2 → swap(nums[mid], nums[high]), high-- (don't increment mid yet)
# 3. Loop until mid > high.
# 4. Ensures in one pass all 0s are at left, 1s in middle, 2s at right.
# Time: O(n), Space: O(1).

class Solution:
    def sortColors(self, nums) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
