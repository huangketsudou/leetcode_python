from typing import List


class Solution:
    def __init__(self):
        self.ans = 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        def dfs(idx, number):
            if idx == n:
                if number == S:
                    self.ans += 1
                return
            for j in [+1, -1]:
                dfs(idx + 1, number + j * nums[idx])

        dfs(0, 0)
        return self.ans


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        c = collections.defaultdict(int)
        c[0] = 1
        for num in nums:
            nxt = collections.defaultdict(int)
            for k, v in c.items():
                nxt[k - num] += v
                nxt[k + num] += v
            c = nxt
        return c[S]


class Solution:
    # 这道题是完全背包问题
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1  # 可能nums[0]==0
        for i in range(1, n):
            for j in range(-1000, 1001):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000]
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000]
        return 0 if S > 1000 else dp[-1][S]


class Solution:
    # 这道题是完全背包问题
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = [0] * 2001
        dp[0] = 1
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(n):
            nxt = [0] * 2001
            for j in range(-1000, 1001):
                if dp[j + 1000] > 0:
                    nxt[j + 1000 + nums[i]] += dp[j + 1000]
                    nxt[j + 1000 - nums[i]] += dp[j + 1000]
            dp = nxt
        return 0 if S > 1000 else dp[S + 1000]


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        t=sum(nums)
        target = S + t
        if t < S or target < 0 or target % 2: return 0
        target //= 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                if i - num >=  0:
                    dp[i] += dp[i - num]
        return dp[-1]


k = Solution()
print(k.findTargetSumWays([1, 1, 1, 1, 1], 3))
