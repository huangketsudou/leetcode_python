from typing import List
import functools


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        remain = [[0 for j in range(len(pizza[0]) + 1)] for i in range(len(pizza) + 1)]
        for i in range(len(pizza) - 1, -1, -1):
            for j in range(len(pizza[0]) - 1, -1, -1):
                remain[i][j] = remain[i + 1][j] + remain[i][j + 1] - remain[i + 1][j + 1] + int(pizza[i][j] == 'A')
                # remain[i][j]表示i，j构成的右下角的矩形有多少苹果
        print(remain)
        mod = int(1e9 + 7)

        @functools.lru_cache(None)
        def way(x, y, kk):
            if remain[x][y] == 0:
                return 0
            if kk == 0:
                return 1
            ans = 0
            for xx in range(x + 1, len(pizza)):
                if remain[x][y] - remain[xx][y] > 0:
                    ans += way(xx, y, kk - 1)
                    ans %= mod
            for yy in range(y + 1, len(pizza[0])):
                if remain[x][y] - remain[x][yy] > 0:
                    ans += way(x, yy, kk - 1)
                    ans %= mod
            return ans

        return way(0, 0, k - 1)


k = Solution()
print(k.ways(pizza=["A..", "AAA", "..."], k=3))


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        remain = [[0] * (len(pizza[0]) + 1) for _ in range(len(pizza) + 1)]
        for i in range(len(pizza) - 1, -1, -1):
            for j in range(len(pizza[0]) - 1, -1, -1):
                remain[i][j] = remain[i + 1][j] + remain[i][j + 1] - remain[i + 1][j + 1] + int(pizza[i][j] == 'A')
        MOD = 10 ** 9 + 7

        def dfs(x, y, kk):
            #再一次切分里，横切与纵切是独立的
            if remain[x][y] == 0:
                return 0
            if kk == 0: return 1
            ans = 0
            for xx in range(x + 1, len(pizza)):
                if remain[x][y] - remain[xx][y] > 0:
                    ans += dfs(xx, y, kk - 1)
                    ans &= MOD
            for yy in range(y + 1, len(pizza[0])):
                if remain[x][y] - remain[x][yy] > 0:
                    ans += dfs(x, yy, kk - 1)
                    ans %= MOD
            return ans

        return dfs(0, 0, k - 1)


