# Approach:
# 1. Use backtracking to build combinations.
# 2. Each recursive call decides:
#    - Add current number → recurse with k-1 left.
#    - Skip current number → move to next.
# 3. Stop when combination size = k → add to result.
# 4. Optimization: prune recursion if not enough numbers left.
# Time: O(C(n,k) * k), Space: O(k) recursion depth.

class Solution:
    def combine(self, n: int, k: int):
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            # Prune: stop if not enough numbers left to complete comb
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
        
        backtrack(1)
        return res
