# Approach:
# 1. Backtracking + DFS from each cell that matches word[0].
# 2. At (r,c,k): if board[r][c] != word[k] → fail; if k == len(word)-1 → success.
# 3. Mark visited in-place (temporarily set to '#') to avoid reuse; explore 4 dirs.
# 4. Restore cell on backtrack. Early prune: if word has a char more frequent than board, return False.
# Time: O(m*n*4^L), Space: O(L) recursion (L = len(word)).

from collections import Counter

class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])

        # Early frequency pruning
        cnt_board = Counter(ch for row in board for ch in row)
        cnt_word = Counter(word)
        for ch, need in cnt_word.items():
            if cnt_board[ch] < need:
                return False

        # Optional direction pruning: reverse word if last char rarer than first
        # (heuristic to fail faster)
        if cnt_board[word[0]] > cnt_board[word[-1]]:
            word = word[::-1]

        def dfs(r, c, k):
            if board[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = '#'  # mark visited

            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    if dfs(nr, nc, k + 1):
                        return True

            board[r][c] = temp  # restore
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] or board[i][j] == word[-1]:  # aligns with possible reversal
                    if dfs(i, j, 0):
                        return True
        return False
