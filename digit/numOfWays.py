class Solution5:
    def numOfWays(self, n: int) -> int:
        x, y = 6, 6
        MOD = 10 ** 9 + 7
        for i in range(1, n):
            prex, prey = x, y
            x = (prex * 3 + prey * 2) % MOD
            y = (prex * 2 + prey * 2) % MOD
        return (x + y) % MOD


k = Solution5()
print(k.numOfWays(5000))
