class Solution:
    def isPowerOfFour(self, n):
        # Approach:
        # 1. Powers of 4 are positive: return False if n <= 0
        # 2. Keep dividing by 4 while divisible
        # 3. If final value is 1 → True, else False
        # Time: O(log₄n), Space: O(1)
        
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
        
        return n == 1
