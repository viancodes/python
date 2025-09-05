from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case
        if len(prices) < 2:
            return 0

        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in prices:
            # Update the four states in order
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2

