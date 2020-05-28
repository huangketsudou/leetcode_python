class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1] if n else 0


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(i, j):
            if s[i:j + 1] == s[i:j + 1][::-1]: return j - i + 1
            if i > j: return 0
            res = 0
            if s[i] == s[j]:
                res = max(res, 2 + dfs(i + 1, j - 1))
            return max(res, dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, len(s) - 1)
