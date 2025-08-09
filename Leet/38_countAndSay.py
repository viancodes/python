class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"

        # Get the previous term in the sequence
        prev = self.countAndSay(n - 1)

        # Build the current term using run-length encoding
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                # Append count and digit
                result += str(count) + prev[i - 1]
                count = 1  # reset count

        # Append the last group
        result += str(count) + prev[-1]

        return result
