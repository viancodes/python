class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in left half
                else:
                    left = mid + 1   # Target in right half

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target in right half
                else:
                    right = mid - 1  # Target in left half

        return -1
