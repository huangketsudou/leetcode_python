from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10000000)

        import functools
        @functools.lru_cache(None)
        def dfs(i, j):
            res = float('inf')
            for c in cuts:
                if i < c < j:
                    res = min(res, dfs(i, c) + dfs(c, j) + j - i)
            if res == float('inf'):
                return 0
            return res

        return dfs(0, n)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        MAP = [0] + cuts + [n]
        MAP.sort()
        m = len(MAP)
        dp = [[float('inf')] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                for c in range(i+1,j):
                    dp[i][j] = min(dp[i][j], dp[i][c] + dp[c][j] + MAP[j] - MAP[i])
                if dp[i][j] == float('inf'):
                    dp[i][j] = 0
        return dp[0][m - 1]