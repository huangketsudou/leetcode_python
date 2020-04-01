class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = {'0':[0,0],'1': [1, 1], '2': [2, 1], '3': [2, 1], '4': [2, 1], '5': [3, 1], '6': [4, 1], '7': [4, 1], '8': [5, 2],
             '9': [8, 2]}
        strN = str(N)
        n = len(strN)
        ans = 0
        for i, v in enumerate(strN):
            all, out = d[v]
            if i == n - 1:
                ans += (all - out)
                continue
            ans += (all * (7 ** (n - i - 1)) - out * (3 ** (n - i - 1)))
        return ans


class Solution2(object):
    def rotatedDigits(self, N):
        A = list(map(int, str(N)))

        memo = {}
        def dp(i, equality_flag, involution_flag):
            if i == len(A): return +(involution_flag)
            if (i, equality_flag, involution_flag) not in memo:
                ans = 0
                for d in range(A[i] + 1 if equality_flag else 10):
                    if d in {3, 4, 7}: continue
                    ans += dp(i+1, equality_flag and d == A[i],
                              involution_flag or d in {2, 5, 6, 9})
                memo[i, equality_flag, involution_flag] = ans
            return memo[i, equality_flag, involution_flag]

        return dp(0, True, False)

class Solution3:
    def rotatedDigits(self, N: int) -> int:
        ans, d = 0, [0] * (N + 1)
        d[: 10] = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        for i in range(N + 1):
            #计算后缀后保存下来
            d[i] = -1 in (d[i // 10], d[i % 10]) and -1 or d[i // 10] | d[i % 10]
            ans += d[i] == 1
        return ans



k = Solution2()
print(k.rotatedDigits(666))
