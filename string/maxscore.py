class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(1,n):
            left=s[:i].count('0')
            right=s[i:].count('1')
            ans=max(ans,left+right)
        return ans


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans,t=0,s.count('1')
        for c in s[:-1]:
            if c=='0':
                t+=1
                ans=max(ans,t)
            else:
                t-=1
                ans=max(ans,t)
        return ans