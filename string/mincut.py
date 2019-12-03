from typing import List
import functools





class Solution5:
    #超时
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        answer = float('inf')

        def core(dp, i, tmp):
            # 对回溯的优化，这个编程方案，对每一种走到底的方案都要
            # 求执行一次判断，所有的方案都会被执行一次
            nonlocal answer
            if i == n:
                answer = min(tmp, answer)
            for j in range(i, n):
                if dp[i][j]:
                    core(dp, j + 1, tmp + 1)

        core(dp, 0, 0)
        return answer - 1


class Solution4:
    #也超时
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]:  # 代码快在这一步，当字符是回文串时，不需要分割
            return 0
        ans = float("inf")
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans


class Solution:
    def minCut(self, s: str) -> int:
        min_s = list(range(len(s)))
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    # 说明不用分割
                    if j == 0:
                        min_s[i] = 0
                    else:
                        min_s[i] = min(min_s[i], min_s[j - 1] + 1)
        return min_s[-1]



g = Solution()
print(g.minCut("ababababababababababababcbabababababababababababa"))
