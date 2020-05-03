from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        modp = 10 ** 9 + 7
        n = len(hats)
        pn = 2 ** n
        dp = [[None for j in range(pn)] for i in range(0, 41)]
        back = [[] for i in range(0, 41)]
        for i in range(n):
            for hat in hats[i]:
                back[hat].append(i)
        dp[0][0] = 1
        for i in range(1, 41):
            for j in range(0, pn):
                dp[i][j] = dp[i - 1][j]
                for k in back[i]:
                    pk = 1 << k
                    if pk & j == 0:
                        continue
                    if dp[i - 1][j - pk] is None:
                        continue
                    if dp[i][j] is None:
                        dp[i][j] = 0
                    dp[i][j] += dp[i - 1][j - pk]
                    dp[i][j] %= modp
        if dp[-1][-1] is None:
            return 0
        else:
            return dp[-1][-1]


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = 40
        M = 1 << len(hats)
        MOD = int(1e9 + 7)

        ht = [set(x) for x in hats]
        pos = [[]]
        for i in range(1, N + 1):
            p = set()
            for j, x in enumerate(hats):
                if i in x:
                    p.add(j)
            pos.append(p)

        print(M, pos)

        @lru_cache(None)
        def dp(st=0, i=1):
            if st + 1 == M:
                return 1
            if i > N:
                return 0
            res = dp(st, i + 1)
            for j in pos[i]:
                if 0 == ((st >> j) & 1):
                    res = res + dp(st | (1 << j), i + 1)
                    res = res % MOD
            return res

        return dp()