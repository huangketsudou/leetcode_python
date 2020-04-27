from typing import List


class Solution:
    # (a*b)%c=(a%c)(b%c)%c
    # (a**b)%c=((a%c)**b)%c
    # (a+b)%c=(a%c+b%c)%c
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m
            n >>= 1
        return ans

    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337


class Solution:
    #6**1234可以写成
    '''
    ((((6^1)^10)*6^2)^10*6^3)^10*6^4
    '''
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.powa(res, 10, 1337) * self.powa(a, i, 1337)
        return res % 1337

    def powa(self, x, n, MOD):
        ans = 1
        while n > 0:
            if n & 1:
                ans = (ans * x) % MOD
            x = (x * x) % MOD
            n >>= 1
        return ans
