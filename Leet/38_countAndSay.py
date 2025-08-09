class Solution:
    def countAndSay(self, n):
        # Base case
        if n == 1:
            return "1"

        # Get the previous term
        prev = self.countAndSay(n - 1)

        # Build the current term using run-length encoding
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1

        # Append the last group
        result += str(count) + prev[-1]

        return result
