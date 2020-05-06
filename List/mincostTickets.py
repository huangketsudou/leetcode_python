from typing import List
import bisect


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * (n + 1)
        valid = [1, 7, 30]
        for i, d in enumerate(days):
            for j,ticket in enumerate(costs):
                idx = bisect.bisect_right(days, d - valid[j])
                dp[i + 1] = min(dp[i + 1], dp[idx] + ticket)
        print(dp)
        return dp[-1]
