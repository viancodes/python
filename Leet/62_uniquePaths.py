# Approach:
# 1. Total moves = (m-1) downs + (n-1) rights = m+n-2 moves total
# 2. Choose (m-1) positions for downs → C(m+n-2, m-1)
# 3. Formula: factorial(m+n-2) // (factorial(m-1) * factorial(n-1))
# Time: O(1) factorial calls, Space: O(1)

import math

class Solution:
    def uniquePaths(self, m, n):
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))
