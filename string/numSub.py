class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        prev = 0
        MOD = 10**9+7
        for i in range(len(s)):
            if s[i]=='0':
                prev = 0
            else:
                prev+=1
            result += prev
            result %=MOD
        return result


