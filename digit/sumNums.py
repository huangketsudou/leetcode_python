class Solution:
    def sumNums(self, n: int) -> int:
        if n == 1:
            return 1
        return n + self.sumNums(n - 1)


class Solution:
    def sumNums(self, n: int) -> int:
        a, b = n, n + 1
        ans = 0
        k = 0
        while k < 14:
            ans += (b & 1) * a
            a <<= 1
            b >>= 1
            k += 1
        return ans >> 1
