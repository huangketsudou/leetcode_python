class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K,min(N,K+W+-1)+1):
            dp[i] = 1
        for i in range(K-1,-1,-1):
            for j in range(1,W+1):
                dp[i] += dp[i+j]/W
        return dp[0]


class Solution2:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


class Solution3:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W:
            return 1.0
        sums = [0.0 for i in range(K + W)]
        sums[0] = 1.0
        for i in range(1, K + W):
            t = min(i-1, K-1)
            if i <= W:
                sums[i] = sums[i - 1] + sums[t] / W
            else:
                sums[i] = sums[i - 1] + (sums[t] - sums[i - W - 1]) / W
        return (sums[N] - sums[K - 1]) / (sums[K + W - 1] - sums[K - 1])