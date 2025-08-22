# Approach:
# 1. Formula-based generation: n-bit Gray code at index i is i ^ (i >> 1).
# 2. Iterate i from 0 to (2^n - 1), compute gray code using the formula.
# 3. Properties:
#    - Adjacent numbers differ by one bit due to xor with right-shift.
#    - Sequence starts with 0, covers all 2^n codes.
# Time: O(2^n), Space: O(1) extra.

class Solution:
    def grayCode(self, n):
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res
