class Solution:
    def maxPower(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        ans = 1
        cur = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans=max(ans,cur)
                cur = 1
        ans=max(ans,cur)
        return ans

