from typing import List


class Solution:
    ##二维完全背包问题，且包内物品只能用一次
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros=s.count('0')
            ones=s.count('1')
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(1+dp[i-zeros][j-ones],dp[i][j])
        return dp[-1][-1]
    