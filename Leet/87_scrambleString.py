# Approach:
# 1. Recursion + Memoization:
#    - Try every split point k (1..n-1) and check two cases:
#      a) No-swap:  s1[:k]  vs s2[:k]   AND  s1[k:]  vs s2[k:]
#      b) Swap:     s1[:k]  vs s2[-k:]  AND  s1[k:]  vs s2[:-k]
# 2. Prune early:
#    - If lengths differ → False
#    - If strings equal → True
#    - If character counts differ → False (cannot scramble to each other)
# 3. Memoize (s1, s2) to avoid recomputation.
# Time: Exponential worst-case, but pruning + memo make it pass; Space: O(n^2) for memo/recursion.

from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dfs(a: str, b: str) -> bool:
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                memo[(a, b)] = True
                return True
            if len(a) != len(b):
                memo[(a, b)] = False
                return False
            # Character multiset must match
            if Counter(a) != Counter(b):
                memo[(a, b)] = False
                return False

            n = len(a)
            for k in range(1, n):
                # no-swap case
                if dfs(a[:k], b[:k]) and dfs(a[k:], b[k:]):
                    memo[(a, b)] = True
                    return True
                # swap case
                if dfs(a[:k], b[n - k:]) and dfs(a[k:], b[:n - k]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
