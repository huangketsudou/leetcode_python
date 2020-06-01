from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)  # row
        n = len(grid[0])  # col
        dp = [[[-1 for k in range(n)] for j in range(n)] for i in range(m)]
        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
        for i in range(0, m - 1):
            for j in range(n):
                for k in range(n):
                    if dp[i][j][k] < 0:
                        continue
                    for jj in range(j - 1, j + 2):
                        if jj < 0 or jj >= n:
                            continue
                        for kk in range(k - 1, k + 2):
                            if kk < 0 or kk >= n:
                                continue
                            cur = dp[i][j][k] + grid[i + 1][jj] + grid[i + 1][kk]
                            if jj == kk:
                                cur -= grid[i + 1][jj]
                            if dp[i + 1][jj][kk] < 0 or cur > dp[i + 1][jj][kk]:
                                dp[i + 1][jj][kk] = cur
        ans = 0
        for j in range(n):
            for k in range(n):
                ans = max(ans, dp[-1][j][k])
        return ans


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dp(r, c1, c2):
            if r == R - 1:
                return grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]
            else:
                return (grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]) + max(
                    dp(r + 1, a, b) for a in range(max(0, c1 - 1), min(C, c1 + 2)) for b in
                    range(max(0, c2 - 1), min(C, c2 + 2)))

        return dp(0, 0, C - 1)
