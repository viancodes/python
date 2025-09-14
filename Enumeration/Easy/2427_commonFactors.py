import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Find GCD of a and b
        g = math.gcd(a, b)
        
        count = 0
        # Count divisors of gcd
        for i in range(1, int(g ** 0.5) + 1):
            if g % i == 0:
                count += 1  # i is a divisor
                if i != g // i:
                    count += 1  # g // i is a divisor (distinct)
        return count
