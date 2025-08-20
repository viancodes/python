# Approach:
# 1. Two pointers (write index `w` and read index `i`).
# 2. Keep at most two of each number by allowing write when:
#    - w < 2 (first two elements always allowed), or
#    - nums[i] != nums[w-2] (current differs from the element two spots back).
# 3. Write nums[i] to nums[w], increment w.
# Time: O(n), Space: O(1), in-place.

class Solution:
    def removeDuplicates(self, nums):
        w = 0
        for x in nums:
            if w < 2 or x != nums[w - 2]:
                nums[w] = x
                w += 1
        return w
