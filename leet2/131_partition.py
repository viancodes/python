from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # precompute palindrome table: pal[i][j] = True iff s[i:j+1] is palindrome
        pal = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i+1][j-1]):
                    pal[i][j] = True

        res, path = [], []

        def dfs(start: int):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if pal[start][end]:
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res
