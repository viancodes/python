class Solution:
    def totalNQueens(self, n):
        mask = (1 << n) - 1
        self.count = 0

        def backtrack(cols, diag1, diag2):
            if cols == mask:
                self.count += 1
                return

            available = ~(cols | diag1 | diag2) & mask
            while available:
                bit = available & -available
                available -= bit
                backtrack(cols | bit, ((diag1 | bit) << 1) & mask, (diag2 | bit) >> 1)

        backtrack(0, 0, 0)
        return self.count
