from functools import lru_cache


class Solution:
    def __init__(self):
        self.ans = float('inf')

    def minDays(self, n: int) -> int:

        @lru_cache()
        def dfs(number, day):
            if number == 0:
                self.ans = min(self.ans, day)
                return
            if day > self.ans:
                return
            dfs(number - 1, day + 1)
            if number % 2 == 0:
                dfs(number - (number // 2), day + 1)
            if n % 3 == 0:
                dfs(number - 2 * (number // 3), day + 1)

        dfs(n, 0)
        return self.ans


class Solution2:

    def minDays(self, n: int) -> int:
        import time
        start = time.time()
        dp = [n] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + 1, dp[i])
            if i % 2 == 0:
                dp[i] = min(dp[i - (i // 2)] + 1, dp[i])
            if i % 3 == 0:
                dp[i] = min(dp[i - 2 * (i // 3)] + 1, dp[i])
        end = time.time()
        print(end - start)
        return dp[n]


from collections import deque
import heapq


class Solution3:

    def minDays(self, n: int) -> int:
        pair = (n, 0)
        stack = deque()
        stack.append(pair)
        visited = set()
        while stack:
            left, day = stack.popleft()
            if left == 0:
                return day
            if left - 1 not in visited:
                stack.append((left - 1, day + 1))
                visited.add(left - 1)
            if left % 2 == 0 and left - left // 2 not in visited:
                stack.append((left - left // 2, day + 1))
                visited.add(left - left // 2)
            if left % 3 == 0 and left - 2 * (left // 3) not in visited:
                stack.append((left - 2 * (left // 3), day + 1))
                visited.add(left - 2 * (left // 3))


k = Solution3()
print(k.minDays(182))
