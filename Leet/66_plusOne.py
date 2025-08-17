# Approach:
# 1. Start from the last digit, add 1.
# 2. If digit becomes 10, set to 0 and carry 1 to the left; otherwise stop.
# 3. If carry remains after the most significant digit (e.g., all 9s), insert 1 at front.
# Time: O(n), Space: O(1) in-place (ignoring output list growth when all 9s).

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry continues
        
        # If we’re here, all digits were 9 (e.g., 999 -> 1000)
        return [1] + digits
