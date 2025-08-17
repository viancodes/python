# Approach:
# 1. We need floor(sqrt(x)) without using built-in sqrt.
# 2. Use Binary Search:
#    - Search between [0, x] (or [0, x//2+1] for optimization).
#    - Mid = (low + high) // 2
#    - If mid*mid <= x < (mid+1)*(mid+1), return mid.
#    - Adjust search bounds accordingly.
# Time: O(log x), Space: O(1).

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the floor(sqrt(x))
