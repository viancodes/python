# Approach:
# 1) If len(s1)+len(s2)!=len(s3) → False.
# 2) DP (1D): dp[j] = can we form s3[:i+j] using s1[:i] and s2[:j]?
#    Transition:
#      dp[j] = (dp[j] and s1[i-1]==s3[i+j-1])   # take from s1
#            or (dp[j-1] and s2[j-1]==s3[i+j-1])# take from s2
# 3) Initialize first row using only s2.
# Time: O(m*n), Space: O(n).

class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # Ensure s2 is the shorter for smaller space if desired (optional)
        # but not necessary; we'll proceed as is.
        dp = [False] * (n + 1)

        # Initialize for i = 0 (using only s2)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill rows for i >= 1
        for i in range(1, m + 1):
            # First col: using only s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                take_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                take_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = take_s1 or take_s2

            # Optional minor pruning: if no True in this row, could early-exit
            # but leaving it simple for clarity.

        return dp[n]
