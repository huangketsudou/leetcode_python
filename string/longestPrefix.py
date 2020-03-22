#前缀后缀比较

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n < 2: return ''

        return s[:self.next(s, n)[-1]]

    def next(self, s, n):
        l = [0] * (n + 1)
        l[0] = -1
        j = -1
        k = 0
        while k < n:
            if j == -1 or s[j] == s[k]:
                k += 1
                j += 1
                l[k] = j
            else:
                j = l[j]

        return l
