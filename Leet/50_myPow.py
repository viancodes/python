class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        return self.fastPow(x, n)
    
    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        
        half = self.fastPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
