class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        
        cols = set()          # columns under attack
        diag1 = set()         # r - c (top-left to bottom-right)
        diag2 = set()         # r + c (top-right to bottom-left)

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                # place
                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                backtrack(r + 1)
                # remove
                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res
