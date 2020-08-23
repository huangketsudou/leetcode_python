from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]
        summary = [0] * n
        summary[0] = stoneValue[0]
        for i in range(1, len(stoneValue)):
            summary[i] = stoneValue[i] + summary[i - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = -1
                for k in range(i + 1, j + 1):
                    r = summary[j] - summary[k - 1]
                    l = summary[k - 1] - summary[i] + stoneValue[i]
                    if r > l:
                        dp[i][j] = max(dp[i][j], l + dp[i][k - 1])
                    elif r < l:
                        dp[i][j] = max(dp[i][j], r + dp[k][j])
                    else:
                        dp[i][j] = max(dp[i][j], r + max(dp[k][j], dp[i][k - 1]))
        return dp[0][n-1]
