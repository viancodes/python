# Approach (Dynamic Programming):
# 1. Let dp[i] = number of ways to decode s[:i].
# 2. Base cases:
#    - dp[0] = 1 (empty string has one way)
#    - dp[1] = 0 if s[0] == '0', else 1
# 3. Transition:
#    - If s[i-1] != '0', then dp[i] += dp[i-1] (use single digit).
#    - If 10 <= int(s[i-2:i]) <= 26, then dp[i] += dp[i-2] (use two digits).
# 4. Answer = dp[n], where n = len(s).
# Time: O(n), Space: O(n) → can be optimized to O(1).

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            one = int(s[i-1:i])
            two = int(s[i-2:i])

            if 1 <= one <= 9:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[n]
