from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        time = n // 3
        idx = n - 2
        summary = 0
        while time != 0:
            summary+= piles[idx]
            idx-=2
            time -= 1
        return summary