class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        maxpro = 3 * pow(2, n - 1)
        if k > maxpro: return ''
        d = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}
        first = ['a', 'b', 'c']
        id, left = divmod(k - 1, pow(2, n - 1))
        g = n - 1
        ans = first[id]
        prev = first[id]
        while len(ans) < n:
            id, left = divmod(left, pow(2, g - 1))
            g = g - 1
            prev = d[prev][id]
            ans += prev

        return ans

k=Solution()
print(k.getHappyString(10,100))