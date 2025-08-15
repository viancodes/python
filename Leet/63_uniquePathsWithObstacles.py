# Approach:
# 1. Use DP table where dp[i][j] = number of ways to reach cell (i,j)
# 2. If cell has an obstacle (1) → dp[i][j] = 0
# 3. Else dp[i][j] = dp[i-1][j] + dp[i][j-1] (top + left paths)
# 4. Initialize dp[0][0] = 1 if no obstacle at start
# Time: O(m*n), Space: O(m*n) → can be optimized to O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Edge case: start or end blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # starting point
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # blocked cell
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]
