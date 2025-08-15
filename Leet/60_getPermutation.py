class Solution:
    def getPermutation(self, n, k):
        # Approach (notes):
        # Use factorial number system (Lehmer code):
        # 1) Precompute factorials and a list of digits [1..n].
        # 2) Convert (k-1) to factorial-base and pick digits by index, removing each from the pool.
        # Time: O(n^2) due to list pops, Space: O(n)
        from math import factorial

        digits = [str(i) for i in range(1, n + 1)]
        k -= 1  # zero-indexed rank
        ans = []

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            k %= f
            ans.append(digits.pop(idx))

        return ''.join(ans)
