from collections import deque

class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def bfs(r, c):
            q = deque([(r, c)])
            board[r][c] = 'E'  # mark as escaped/safe
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'E'
                        q.append((nx, ny))

        # 1) Mark border-connected 'O's as 'E'
        for i in range(m):
            if board[i][0] == 'O': bfs(i, 0)
            if board[i][n-1] == 'O': bfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': bfs(0, j)
            if board[m-1][j] == 'O': bfs(m-1, j)

        # 2) Flip surrounded 'O' -> 'X', restore 'E' -> 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'
