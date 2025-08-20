# Approach:
# 1. Modified Binary Search with duplicates:
#    - If nums[mid] == target → True.
#    - If nums[left] == nums[mid] == nums[right], we can't tell which half is sorted → shrink both ends.
#    - Else if left half is sorted (nums[left] <= nums[mid]):
#         * If target in [nums[left], nums[mid)), search left; else search right.
#    - Else right half is sorted:
#         * If target in (nums[mid], nums[right]], search right; else search left.
# 2. Repeat until pointers cross.
# Time: Average O(log n), Worst O(n) when many duplicates; Space: O(1).

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            # Ambiguous due to duplicates: shrink bounds
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue

            # Left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # Right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
