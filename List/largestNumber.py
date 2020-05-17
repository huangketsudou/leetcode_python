from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[] for _ in range(target+1)]
        for i in range(1, target + 1):
            for j, c in enumerate(cost):
                if i == c:

                    dp[i]=self.cmp(dp[i],[j+1]).copy()
                elif i > c:
                    if len(dp[i - c]):
                        b = dp[i - c].copy()
                        b.append(j + 1)
                        dp[i] = self.cmp(dp[i], b).copy()
        for i in dp:
            print(i)
        return ''.join(map(str,dp[-1]))

    def cmp(self, a, b):
        a.sort(reverse=True)
        b.sort(reverse=True)
        if len(a) == len(b):
            return a if a > b else b
        elif len(a) < len(b):
            return b
        else:
            return a


class Solution:
    #@SQRPI
    def largestNumber(self, cost: List[int], tar: int) -> str:
        mi = min(cost)
        @lru_cache(None)
        def dp(target): # target 下的最大值
            if target == 0: return 0
            if target < mi: return -float('inf')
            res = -float('inf')
            for x in range(9):
                res = max(dp(target - cost[x])*10 + x + 1, res)
            return res
        res = dp(tar)
        return str(res) if res > 0 else "0"

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-1 for j in range(target + 1)]
        dp[0] = 0
        for i in range(8, -1, -1):
            for j in range(cost[i], target + 1):
                if dp[j - cost[i]] < 0:
                    continue
                dp[j] = max(dp[j], dp[j - cost[i]] * 10 + (i + 1))
        if dp[target] >= 0:
            return str(dp[target])
        else:
            return '0'

k = Solution()
print(k.largestNumber([1,1,1,1,1,1,1,1,1], 5000))
