# Approach:
# 1. Merge in-place from the end to avoid overwriting unused slots in nums1.
# 2. Use three pointers:
#    - i = m - 1 (last valid index in nums1)
#    - j = n - 1 (last index in nums2)
#    - k = m + n - 1 (write position in nums1)
# 3. While i >= 0 and j >= 0, write the larger of nums1[i], nums2[j] to nums1[k], move pointers.
# 4. If nums2 has leftovers (j >= 0), copy them to nums1 (nums1 leftovers are already in place).
# Time: O(m+n), Space: O(1).

class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy any remaining nums2 elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
