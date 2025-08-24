# Approach:
# 1) This is the Catalan number Cn: number of unique BSTs with n nodes.
# 2) DP: dp[i] = sum_{root=1..i} dp[root-1] * dp[i-root]
#    - dp[0] = 1 (empty tree), dp[1] = 1
# 3) Answer: dp[n]
# Time: O(n^2), Space: O(n)

class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for nodes in range(1, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = dp[root - 1]
                right = dp[nodes - root]
                total += left * right
            dp[nodes] = total
        return dp[n]
