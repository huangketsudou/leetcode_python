class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if not length:
            return 0
        fail={}
        MAX=0
        k=0
        for i in range(length):
            if  s[i] in fail:
                k=max(fail[s[i]],k)
            MAX=max(MAX,i-k+1)
            fail[s[i]]=i+1
        return MAX

c=Solution()
print(c.lengthOfLongestSubstring('abba'))
