from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i-1] == B[j-1] else 0
                ans = max(ans, dp[i][j])
        return ans