from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        counts = Counter(digits)   # Count how many times each digit appears
        result = []

        # Iterate over all possible 3-digit numbers
        for h in range(1, 10):          # Hundreds place (no leading zero)
            if counts[h] == 0:
                continue
            counts[h] -= 1              # Use one occurrence of h

            for t in range(0, 10):      # Tens place (can be zero)
                if counts[t] == 0:
                    continue
                counts[t] -= 1          # Use one occurrence of t

                for u in range(0, 10, 2):  # Units place (must be even)
                    if counts[u] > 0:
                        num = h * 100 + t * 10 + u
                        result.append(num)

                counts[t] += 1          # Backtrack: put t back

            counts[h] += 1              # Backtrack: put h back

        return result
