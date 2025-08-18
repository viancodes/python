# Approach:
# 1. Classic Dynamic Programming (Levenshtein distance).
# 2. Define dp[i][j] = minimum operations to convert word1[:i] → word2[:j].
# 3. Base cases:
#    - dp[0][j] = j (convert empty string to word2[:j] by inserting j chars).
#    - dp[i][0] = i (convert word1[:i] to empty string by deleting i chars).
# 4. Transition:
#    - If word1[i-1] == word2[j-1] → dp[i][j] = dp[i-1][j-1]
#    - Else:
#        dp[i][j] = 1 + min(
#            dp[i-1][j],   # delete from word1
#            dp[i][j-1],   # insert into word1
#            dp[i-1][j-1]  # replace
#        )
# 5. Answer = dp[m][n] where m = len(word1), n = len(word2).
# Time: O(m*n), Space: O(m*n) → can be optimized to O(min(m,n)).

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )

        return dp[m][n]
