# Approach:
# 1. Use DP where dp[i][j] stores the minimum sum to reach cell (i,j)
# 2. Transition:
#    - First cell dp[0][0] = grid[0][0]
#    - First row: can only come from the left → dp[0][j] = dp[0][j-1] + grid[0][j]
#    - First col: can only come from above → dp[i][0] = dp[i-1][0] + grid[i][0]
#    - Other cells: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
# 3. Return dp[m-1][n-1] as the result
# Time: O(m*n), Space: O(m*n) → can be optimized to O(n)

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
