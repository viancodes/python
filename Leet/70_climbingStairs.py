# Approach:
# 1. This is a Fibonacci-like problem.
# 2. To reach step n:
#    - Last move could be 1 step → ways(n-1)
#    - Or last move could be 2 steps → ways(n-2)
#    => ways(n) = ways(n-1) + ways(n-2)
# 3. Base cases:
#    - n = 1 → 1 way
#    - n = 2 → 2 ways
# 4. Use iterative DP for O(n) time and O(1) space.
# Time: O(n), Space: O(1).

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        
        return second
