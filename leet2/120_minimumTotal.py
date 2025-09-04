from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom-up DP with O(R) extra space.
        dp[c] represents the min path sum from current row r, col c down to the base.
        We build it starting from the last row.
        """
        # Number of rows
        rows = len(triangle)

        # Defensive check (not strictly needed due to constraints)
        if rows == 0:
            return 0

        # dp size = last row length = rows
        dp = [0] * rows

        # Initialize dp with the last row
        r = rows - 1
        c = 0
        while c < len(triangle[r]):
            dp[c] = triangle[r][c]
            c += 1

        # Process rows from second-last up to the top
        r = rows - 2
        while r >= 0:
            c = 0
            # For row r, valid columns are [0 .. r]
            while c <= r:
                # For each position, choose the cheaper of staying in same column or moving to c+1
                down_same = dp[c]
                down_right = dp[c + 1]
                dp[c] = triangle[r][c] + (down_same if down_same < down_right else down_right)
                c += 1
            r -= 1

        # dp[0] now holds the minimum total from the top
        return dp[0]

