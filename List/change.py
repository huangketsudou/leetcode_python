from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (1 + amount)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
