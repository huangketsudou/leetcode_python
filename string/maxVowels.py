class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cur = 0
        for i in range(k):
            if s[i] in 'aiueo':
                cur += 1
        ans = cur
        r = k - 1
        l = 0
        while r < n - 1:
            if s[l] in 'aiueo':
                cur -= 1
            l += 1
            r += 1
            if s[r] in 'aiueo':
                cur += 1
            ans = max(ans, cur)
        return ans

