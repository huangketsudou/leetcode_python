class Solution:
    def countArrangement(self, N: int) -> int:
        dp = [0] * (1 << N)
        for i in range(N):
            dp[1 << i] = 1
        for i in range(1 << N):
            tmp = i
            index = 1
            while tmp:
                tmp &= (tmp - 1)
                index += 1
            for j in range(N):
                if (1 << j & i) == 0 and (index % (j + 1) or (j + 1) % index):
                    dp[1 << j | i] += dp[i]
            return dp[(1 << N) - 1]
