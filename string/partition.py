from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def core(s, i, tmp):
            if i == n:
                answer.append(tmp)
            for j in range(i + 1, n + 1):  # 这里的i，n取值范围要注意
                if s[i:j] == s[i:j][::-1]:
                    core(s, j, tmp + [s[i:j]])

        if not s: return []
        n = len(s)
        answer = []
        core(s, 0, [])
        return answer


class Solution2:
    #大佬的代码，处理边界更简便
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res




class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        answer = []

        def core(dp, i, tmp):
            if i == n:
                answer.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    core(dp, j + 1, tmp + [s[i:j + 1]])
        core(dp,0,[])
        return answer


class Solutionlongest:
    # 最长回文串的dp解法
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j: i + 1]
                    max_len = i + 1 - j
        return res


k = Solution3()
print(k.partition('aab'))
