from typing import List


class Solution(object):
    def minCost(self, hs, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        self.n = n

        dp = {}

        def dfs(index, curc, pre):
            if index == len(hs):
                if curc == target: return 0
                return float('inf')
            if (index, curc, pre) in dp:
                return dp[index, curc, pre]
            if hs[index] != 0:
                return dfs(index + 1, curc + (hs[index] != pre), hs[index])
            res = float('inf')
            for color in range(1, self.n + 1):
                res = min(res, cost[index][color - 1] + dfs(index + 1, curc + (color != pre), color))
            dp[index, curc, pre] = res
            return res

        r = dfs(0, 0, -1)
        return r if r != float('inf') else -1


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        le = len(houses)
        INF = float('inf')

        dp = [[[INF]*(n+1) for _ in range(target+1)] for _ in range(le+1)]
        dp[0][0] = [0]*(n+1)

        for i in range(1, le+1):
            for j in range(1, target+1):
                for k in range(1, n+1):
                    nowc = houses[i-1]

                    if nowc==0:
                        for kk in range(1, n+1):
                            if kk!=k:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][kk]+cost[i-1][k-1])
                            else:
                                dp[i][j][k] = min(dp[i-1][j][kk]+cost[i-1][k-1], dp[i][j][k])


                    else:
                        if k!=nowc:
                            dp[i][j][nowc] = min(dp[i-1][j-1][k], dp[i][j][nowc])
                        else:
                            dp[i][j][nowc] = min(dp[i][j][nowc], dp[i-1][j][nowc])
        res = min(dp[-1][-1])
        return res if res!=INF else -1