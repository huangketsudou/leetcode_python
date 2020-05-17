class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = set()
        for i in range(1, n+1):
            for j in range(1, i):
                r = self.gcd(i, j)
                ans.add('{}/{}'.format(j//r,i//r))
        return list(ans)

    def gcd(self, a, b):
        r = a % b
        while r != 0:
            a, b = b, r
            r = a % b
        return b
